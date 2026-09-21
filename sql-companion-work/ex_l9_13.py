
EX = []
def ex(**kw):
    kw.setdefault("ordered", False)
    EX.append(kw)

TRY = """CREATE OR REPLACE FUNCTION lab.try(stmt text) RETURNS boolean LANGUAGE plpgsql AS $f$
BEGIN EXECUTE stmt; RETURN true; EXCEPTION WHEN others THEN RETURN false; END $f$;"""

# ---------------------------------------------------------------- LEVEL 9 : DML
ex(id="E9.1", level=9, title="Materialise a daily GMV table", tags="CREATE TABLE · INSERT … SELECT · PK",
   prompt="In schema `work`, create `tenant_daily_gmv(tenant_id int, day date, gmv_minor bigint NOT NULL, PRIMARY KEY (tenant_id, day))` and fill it with fulfilled-order GMV per tenant per UTC day for **January 2025**.",
   out="table contents `tenant_id, day, gmv_minor`",
   trap="Column list on `INSERT` (never rely on positional order across a migration). Create the constraint *with* the table so a re-run fails loudly instead of duplicating. All DML in this level is graded inside a transaction that is rolled back — you can retry freely.",
   stmts="""CREATE TABLE work.tenant_daily_gmv (tenant_id int, day date, gmv_minor bigint NOT NULL, PRIMARY KEY (tenant_id, day));
INSERT INTO work.tenant_daily_gmv (tenant_id, day, gmv_minor)
SELECT tenant_id, placed_at::date, sum(total_minor) FROM lab.customer_order
WHERE status = 'fulfilled' AND placed_at >= '2025-01-01' AND placed_at < '2025-02-01' GROUP BY 1, 2;""",
   probe="SELECT * FROM work.tenant_daily_gmv",
   key="""CREATE TABLE work.tenant_daily_gmv (tenant_id int, day date, gmv_minor bigint NOT NULL, PRIMARY KEY (tenant_id, day));
INSERT INTO work.tenant_daily_gmv (tenant_id, day, gmv_minor)
SELECT tenant_id, placed_at::date, sum(total_minor) FROM lab.customer_order
WHERE status = 'fulfilled' AND placed_at >= '2025-01-01' AND placed_at < '2025-02-01' GROUP BY 1, 2;""")

ex(id="E9.2", level=9, title="Repair corrupted totals", tags="UPDATE … FROM · IS DISTINCT FROM",
   prompt="Setup gives you `work.o`, a copy of `customer_order` in which every 100th order (`order_id % 100 = 0`, 200 rows) has `total_minor = 0`. Repair **only the wrong rows** so that `total_minor` equals the sum of `qty × unit_price_minor` of its lines. The statement must report `UPDATE 200`.",
   out="`work.o` equals `lab.customer_order` on `(order_id, total_minor)`",
   trap="Updating *every* row (no `WHERE … IS DISTINCT FROM`) rewrites 20,000 tuples — table bloat and WAL for no reason. `IS DISTINCT FROM`, not `<>`, so a NULL total would be repaired too.",
   setup="""CREATE TABLE work.o AS SELECT * FROM lab.customer_order;
UPDATE work.o SET total_minor = 0 WHERE order_id % 100 = 0;""",
   stmts="""UPDATE work.o o SET total_minor = s.t
FROM (SELECT order_id, sum(qty::bigint * unit_price_minor) AS t FROM lab.order_line GROUP BY order_id) s
WHERE s.order_id = o.order_id AND o.total_minor IS DISTINCT FROM s.t;""",
   probe="SELECT order_id, total_minor FROM work.o",
   key="""UPDATE work.o o SET total_minor = s.t
FROM (SELECT order_id, sum(qty::bigint * unit_price_minor) AS t FROM lab.order_line GROUP BY order_id) s
WHERE s.order_id = o.order_id AND o.total_minor IS DISTINCT FROM s.t;""")

ex(id="E9.3", level=9, title="Idempotent daily load (upsert)", tags="INSERT … ON CONFLICT DO UPDATE · idempotency",
   prompt="Create `work.daily_orders(day date PRIMARY KEY, n int NOT NULL)`. Write one statement that loads the count of orders per UTC day for all of 2025 and can be **run twice with the same result**.",
   out="`day, n`",
   trap="`SET n = daily_orders.n + EXCLUDED.n` is *not* idempotent (a re-run doubles). `SET n = EXCLUDED.n` is. If your source query returned two rows for one day in a single statement you would get `ON CONFLICT DO UPDATE command cannot affect row a second time` — aggregate first. Idempotent writes are the whole point of gcp-curriculum 3.4/3.5.",
   stmts="""CREATE TABLE work.daily_orders (day date PRIMARY KEY, n int NOT NULL);
INSERT INTO work.daily_orders (day, n) SELECT placed_at::date, count(*) FROM lab.customer_order GROUP BY 1
ON CONFLICT (day) DO UPDATE SET n = EXCLUDED.n;
INSERT INTO work.daily_orders (day, n) SELECT placed_at::date, count(*) FROM lab.customer_order GROUP BY 1
ON CONFLICT (day) DO UPDATE SET n = EXCLUDED.n;""",
   probe="SELECT * FROM work.daily_orders",
   key="""INSERT INTO work.daily_orders (day, n)
SELECT placed_at::date, count(*) FROM lab.customer_order GROUP BY 1
ON CONFLICT (day) DO UPDATE SET n = EXCLUDED.n;""")

ex(id="E9.4", level=9, title="Delete the double-submitted reviews", tags="DELETE … USING · self-join delete · RETURNING",
   prompt="Setup gives `work.r`, a copy of `review`. Delete duplicate `(product_id, user_id)` reviews, **keeping the newest** (highest `review_id`). Report how many were deleted (`DELETE 400`).",
   out="`work.r` keeps 6,000 rows",
   trap="Test the *keep* rule on a tiny sample first. `DELETE` on a self-join needs `USING`; without a total order you can delete both copies. Run it inside `BEGIN … ROLLBACK` in real life until the count matches your prediction.",
   setup="CREATE TABLE work.r AS SELECT * FROM lab.review;",
   stmts="""DELETE FROM work.r a USING work.r b
WHERE a.product_id = b.product_id AND a.user_id = b.user_id AND a.review_id < b.review_id;""",
   probe="SELECT review_id FROM work.r",
   key="""DELETE FROM work.r a USING work.r b
WHERE a.product_id = b.product_id AND a.user_id = b.user_id AND a.review_id < b.review_id;""")

ex(id="E9.5", level=9, title="Sync stock with MERGE", tags="MERGE (PG15+) · three-way sync",
   prompt="Setup gives `work.stock_t` (products 1–10 with `on_hand`) and `work.stock_feed` (a partner feed). With **one `MERGE`**: rows in both → update `on_hand`, **except** feed `on_hand = 0` → delete the target row; feed rows not in target → insert.",
   out="`work.stock_t` afterwards (small — check by eye)",
   trap="`MERGE` arrived in PostgreSQL 15; `WHEN NOT MATCHED BY SOURCE` only in 17 — so 'delete rows missing from the feed' cannot be done in one 15/16 MERGE. Many-to-one source rows raise a cardinality error. SQL Server, Oracle, BigQuery all have `MERGE` with dialect differences (Rosetta table).",
   setup="""CREATE TABLE work.stock_t AS SELECT product_id, on_hand FROM lab.stock WHERE product_id <= 10;
CREATE TABLE work.stock_feed (product_id int PRIMARY KEY, on_hand int NOT NULL);
INSERT INTO work.stock_feed VALUES (1, 500), (2, 0), (3, 7), (11, 33), (12, 44);""",
   stmts="""MERGE INTO work.stock_t t USING work.stock_feed f ON t.product_id = f.product_id
WHEN MATCHED AND f.on_hand = 0 THEN DELETE
WHEN MATCHED THEN UPDATE SET on_hand = f.on_hand
WHEN NOT MATCHED THEN INSERT (product_id, on_hand) VALUES (f.product_id, f.on_hand);""",
   probe="SELECT product_id, on_hand FROM work.stock_t ORDER BY product_id",
   ordered=True, show=12,
   key="""MERGE INTO work.stock_t t USING work.stock_feed f ON t.product_id = f.product_id
WHEN MATCHED AND f.on_hand = 0 THEN DELETE
WHEN MATCHED THEN UPDATE SET on_hand = f.on_hand
WHEN NOT MATCHED THEN INSERT (product_id, on_hand) VALUES (f.product_id, f.on_hand);""")

ex(id="E9.6", level=9, title="Chunked backfill", tags="batching · SKIP LOCKED · WAL/bloat awareness",
   prompt="Setup gives `work.o` (copy of `customer_order`) with a new nullable column `total_major numeric(12,2)`. Backfill `total_minor / 100.0` in chunks of **1,000 rows**, looping until no rows are left. (Here one transaction; in production every chunk commits separately — gcp-curriculum 2.6 expand/contract.)",
   out="all 20,000 rows have `total_major` set",
   trap="`WHERE total_major IS NULL … LIMIT` inside a CTE + `UPDATE … RETURNING` is the loop body. One giant `UPDATE` holds locks and WAL for minutes on a real table and blocks vacuum. Chunk size is a *tuning knob*, not a constant.",
   setup="""CREATE TABLE work.o AS SELECT * FROM lab.customer_order;
ALTER TABLE work.o ADD COLUMN total_major numeric(12,2);""",
   stmts="""DO $$ DECLARE n int; BEGIN
  LOOP
    WITH c AS (SELECT order_id FROM work.o WHERE total_major IS NULL ORDER BY order_id LIMIT 1000 FOR UPDATE SKIP LOCKED)
    UPDATE work.o o SET total_major = o.total_minor / 100.0 FROM c WHERE o.order_id = c.order_id;
    GET DIAGNOSTICS n = ROW_COUNT;
    EXIT WHEN n = 0;
  END LOOP;
END $$;""",
   probe="SELECT order_id, total_major FROM work.o",
   key="""DO $$ DECLARE n int; BEGIN
  LOOP
    WITH c AS (SELECT order_id FROM work.o WHERE total_major IS NULL ORDER BY order_id LIMIT 1000 FOR UPDATE SKIP LOCKED)
    UPDATE work.o o SET total_major = o.total_minor / 100.0 FROM c WHERE o.order_id = c.order_id;
    GET DIAGNOSTICS n = ROW_COUNT;
    EXIT WHEN n = 0;
  END LOOP;
END $$;""")

ex(id="E9.7", level=9, title="Archive refunded orders atomically", tags="writable CTE · DELETE … RETURNING",
   prompt="Setup gives `work.o` (copy of `customer_order`) and an empty `work.o_archive (LIKE work.o)`. In **one statement**, move every refunded order from `work.o` into `work.o_archive`.",
   out="`live, archived` counts (18000, 2000)",
   trap="`DELETE … RETURNING *` inside a CTE feeding an `INSERT` is atomic — no window where the row is in both or neither. Doing it as two statements needs a transaction; doing it in the application needs an outbox.",
   setup="""CREATE TABLE work.o AS SELECT * FROM lab.customer_order;
CREATE TABLE work.o_archive (LIKE work.o);""",
   stmts="""WITH moved AS (DELETE FROM work.o WHERE status = 'refunded' RETURNING *)
INSERT INTO work.o_archive SELECT * FROM moved;""",
   probe="SELECT (SELECT count(*) FROM work.o) AS live, (SELECT count(*) FROM work.o_archive) AS archived",
   show=2,
   key="""WITH moved AS (DELETE FROM work.o WHERE status = 'refunded' RETURNING *)
INSERT INTO work.o_archive SELECT * FROM moved;""")

# ---------------------------------------------------------------- LEVEL 10 : DDL & constraints (battery = ordered list of pass/fail)
BAT = "SELECT n, lab.try(sql) AS ok FROM (VALUES {rows}) v(n, sql)"

ex(id="E10.1", level=10, title="Coupon table: constraints as a specification", tags="CHECK · UNIQUE · exactly-one-of · citext-free case-insensitive unique",
   prompt="""Create `work.coupon` so that this **battery of 8 inserts gives exactly the pass/fail vector `T T F F F F F T`**:
1. `('SAVE10', percent_off=10, amount_off_minor=NULL, 2025-01-01 → 2025-02-01)` succeeds · 2. a percent coupon with `percent_off=100` succeeds · 3. `percent_off=0` fails · 4. `percent_off=101` fails · 5. **both** `percent_off` and `amount_off_minor` set fails · 6. **neither** set fails · 7. a second code `'save10'` (different case) fails · 8. an amount coupon `amount_off_minor=500` with `valid_until` NULL succeeds.
(Battery statements are in Appendix B.1.)""",
   out="vector of booleans, ordered by test number",
   trap="'Exactly one of' = `num_nonnulls(percent_off, amount_off_minor) = 1`. Case-insensitive uniqueness needs a *functional* unique index on `lower(code)` (or `citext`). CHECK passes when the expression is NULL — write NOT NULL where you mean it.",
   setup=TRY + """
CREATE TABLE work.coupon (
  coupon_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  code text NOT NULL,
  percent_off int CHECK (percent_off BETWEEN 1 AND 100),
  amount_off_minor int CHECK (amount_off_minor > 0),
  valid_from date, valid_until date,
  CHECK (num_nonnulls(percent_off, amount_off_minor) = 1),
  CHECK (valid_until IS NULL OR valid_from IS NULL OR valid_from < valid_until));
CREATE UNIQUE INDEX coupon_code_ci ON work.coupon (lower(code));""",
   probe="""SELECT n, lab.try(sql) AS ok FROM (VALUES
 (1,$$INSERT INTO work.coupon(code,percent_off,valid_from,valid_until) VALUES ('SAVE10',10,'2025-01-01','2025-02-01')$$),
 (2,$$INSERT INTO work.coupon(code,percent_off) VALUES ('FULL',100)$$),
 (3,$$INSERT INTO work.coupon(code,percent_off) VALUES ('ZERO',0)$$),
 (4,$$INSERT INTO work.coupon(code,percent_off) VALUES ('OVER',101)$$),
 (5,$$INSERT INTO work.coupon(code,percent_off,amount_off_minor) VALUES ('BOTH',10,500)$$),
 (6,$$INSERT INTO work.coupon(code) VALUES ('NONE')$$),
 (7,$$INSERT INTO work.coupon(code,percent_off) VALUES ('save10',5)$$),
 (8,$$INSERT INTO work.coupon(code,amount_off_minor) VALUES ('FIVE',500)$$)) v(n, sql) ORDER BY n""",
   ordered=True, show=8,
   key="""CREATE TABLE work.coupon (
  coupon_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  code text NOT NULL,
  percent_off int CHECK (percent_off BETWEEN 1 AND 100),
  amount_off_minor int CHECK (amount_off_minor > 0),
  valid_from date, valid_until date,
  CHECK (num_nonnulls(percent_off, amount_off_minor) = 1),
  CHECK (valid_until IS NULL OR valid_from IS NULL OR valid_from < valid_until));
CREATE UNIQUE INDEX coupon_code_ci ON work.coupon (lower(code));""")

ex(id="E10.2", level=10, title="Tenant-safe foreign key", tags="composite FK · multi-tenancy · integrity at the schema level",
   prompt="""Create `work.note(note_id bigint PK, tenant_id int NOT NULL, user_id bigint NOT NULL, body text)` so that a note can only reference a user **of the same tenant**. Battery (Appendix B.2) must give `T F F F`: (1) tenant 1 / user 1 ok · (2) tenant 2 / user 1 fails (user 1 is tenant 1's) · (3) tenant 1 / user 999999 fails · (4) NULL tenant fails.""",
   out="vector of booleans",
   trap="`user_id REFERENCES app_user` alone only proves the user *exists*. The composite `FOREIGN KEY (tenant_id, user_id) REFERENCES app_user (tenant_id, user_id)` needs a matching unique constraint on the parent — that is why the lab's `app_user` carries `UNIQUE (tenant_id, user_id)`. This is defence in depth beneath RLS (gcp-curriculum 8.1).",
   setup=TRY + """
CREATE TABLE work.note (note_id bigint PRIMARY KEY, tenant_id int NOT NULL, user_id bigint NOT NULL, body text,
  FOREIGN KEY (tenant_id, user_id) REFERENCES lab.app_user (tenant_id, user_id));""",
   probe="""SELECT n, lab.try(sql) AS ok FROM (VALUES
 (1,$$INSERT INTO work.note VALUES (1,1,1,'x')$$),
 (2,$$INSERT INTO work.note VALUES (2,2,1,'x')$$),
 (3,$$INSERT INTO work.note VALUES (3,1,999999,'x')$$),
 (4,$$INSERT INTO work.note VALUES (4,NULL,1,'x')$$)) v(n, sql) ORDER BY n""",
   ordered=True, show=4,
   key="""CREATE TABLE work.note (note_id bigint PRIMARY KEY, tenant_id int NOT NULL, user_id bigint NOT NULL, body text,
  FOREIGN KEY (tenant_id, user_id) REFERENCES lab.app_user (tenant_id, user_id));""")

ex(id="E10.3", level=10, title="One active subscription per user", tags="partial unique index · state machine invariants",
   prompt="""`work.subscription(sub_id bigint PK, user_id bigint NOT NULL, status text CHECK (status IN ('active','cancelled')))`. Enforce **at most one `active` row per user**, any number of cancelled. Battery (Appendix B.3) expects `T T T F T`: (1) user 1 active · (2) user 1 cancelled · (3) user 1 cancelled again · (4) user 1 second active — fails · (5) user 2 active.""",
   out="vector of booleans",
   trap="A plain `UNIQUE (user_id, status)` would forbid a second *cancelled* row. The invariant is conditional — a **partial unique index** `… (user_id) WHERE status = 'active'`. Race-free by construction, unlike an application-side check.",
   setup=TRY + """
CREATE TABLE work.subscription (sub_id bigint PRIMARY KEY, user_id bigint NOT NULL, status text NOT NULL CHECK (status IN ('active','cancelled')));
CREATE UNIQUE INDEX one_active ON work.subscription (user_id) WHERE status = 'active';""",
   probe="""SELECT n, lab.try(sql) AS ok FROM (VALUES
 (1,$$INSERT INTO work.subscription VALUES (1,1,'active')$$),
 (2,$$INSERT INTO work.subscription VALUES (2,1,'cancelled')$$),
 (3,$$INSERT INTO work.subscription VALUES (3,1,'cancelled')$$),
 (4,$$INSERT INTO work.subscription VALUES (4,1,'active')$$),
 (5,$$INSERT INTO work.subscription VALUES (5,2,'active')$$)) v(n, sql) ORDER BY n""",
   ordered=True, show=5,
   key="""CREATE UNIQUE INDEX one_active ON work.subscription (user_id) WHERE status = 'active';""")

ex(id="E10.4", level=10, title="No overlapping price validity", tags="EXCLUDE constraint · range types · btree_gist",
   prompt="""`work.price_period(product_id bigint, during daterange, price_minor int)`. Forbid two rows of the **same product** whose periods overlap. Battery (Appendix B.4) expects `T T F T F`: (1) p1 `[2025-01-01,2025-02-01)` · (2) p1 `[2025-02-01,2025-03-01)` (touching is fine) · (3) p1 `[2025-01-15,2025-01-20)` overlaps → fails · (4) p2 same dates as (1) fine · (5) p1 `[2025-02-28,2025-04-01)` overlaps (2) → fails.""",
   out="vector of booleans",
   trap="Uniqueness of `(product_id, valid_from)` does **not** stop overlaps. `EXCLUDE USING gist (product_id WITH =, during WITH &&)` needs `btree_gist` for the `=` part. Half-open ranges `[a,b)` make 'touching' legal. Spanner and BigQuery have no exclusion constraints — you'd enforce in a transaction (Rosetta table).",
   setup=TRY + """
CREATE EXTENSION IF NOT EXISTS btree_gist;
CREATE TABLE work.price_period (product_id bigint NOT NULL, during daterange NOT NULL, price_minor int NOT NULL,
  EXCLUDE USING gist (product_id WITH =, during WITH &&));""",
   probe="""SELECT n, lab.try(sql) AS ok FROM (VALUES
 (1,$$INSERT INTO work.price_period VALUES (1,'[2025-01-01,2025-02-01)',100)$$),
 (2,$$INSERT INTO work.price_period VALUES (1,'[2025-02-01,2025-03-01)',110)$$),
 (3,$$INSERT INTO work.price_period VALUES (1,'[2025-01-15,2025-01-20)',120)$$),
 (4,$$INSERT INTO work.price_period VALUES (2,'[2025-01-01,2025-02-01)',100)$$),
 (5,$$INSERT INTO work.price_period VALUES (1,'[2025-02-28,2025-04-01)',130)$$)) v(n, sql) ORDER BY n""",
   ordered=True, show=5,
   key="""CREATE EXTENSION IF NOT EXISTS btree_gist;
CREATE TABLE work.price_period (product_id bigint NOT NULL, during daterange NOT NULL, price_minor int NOT NULL,
  EXCLUDE USING gist (product_id WITH =, during WITH &&));""")

ex(id="E10.5", level=10, title="Circular references with DEFERRABLE", tags="DEFERRABLE INITIALLY DEFERRED · constraint timing",
   prompt="""Two tables reference each other: `work.a(id PK, b_id → b)` and `work.b(id PK, a_id → a)`. Make it possible to insert `a(1, b_id=1)` and `b(1, a_id=1)` **in one transaction** but impossible to commit a dangling reference. Battery (Appendix B.5) is a `DO` block — expected: block succeeds; then a lone `INSERT INTO a VALUES (2, 99)` inside its own transaction **fails at COMMIT** (not at the INSERT).""",
   out="commit-time failure demonstrated",
   trap="Without `DEFERRABLE INITIALLY DEFERRED` the first insert fails immediately. Deferred checks run at `COMMIT` — so the error surfaces *after* your `INSERT` returned success; app code must handle a failed commit. `SET CONSTRAINTS … DEFERRED` scopes it per transaction.",
   setup=TRY + """
CREATE TABLE work.a (id int PRIMARY KEY, b_id int);
CREATE TABLE work.b (id int PRIMARY KEY, a_id int);
ALTER TABLE work.a ADD FOREIGN KEY (b_id) REFERENCES work.b (id) DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE work.b ADD FOREIGN KEY (a_id) REFERENCES work.a (id) DEFERRABLE INITIALLY DEFERRED;
INSERT INTO work.a VALUES (1, 1); INSERT INTO work.b VALUES (1, 1);
SET CONSTRAINTS ALL IMMEDIATE;""",
   probe="SELECT (SELECT count(*) FROM work.a) AS a_rows, (SELECT count(*) FROM work.b) AS b_rows",
   show=1,
   key="""ALTER TABLE work.a ADD FOREIGN KEY (b_id) REFERENCES work.b (id) DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE work.b ADD FOREIGN KEY (a_id) REFERENCES work.a (id) DEFERRABLE INITIALLY DEFERRED;""")

ex(id="E10.6", level=10, title="Row-level security by tenant", tags="RLS · policies · current_setting · roles",
   prompt="""Enable RLS on `work.o` (a copy of `customer_order`) so that a role `app_rls` sees **only rows where `tenant_id = current_setting('app.tenant_id')::int`**. Then, as `app_rls` with `app.tenant_id = '2'`, count rows per tenant. Predict first: how many rows, which tenants? What happens if the setting is unset?""",
   out="`tenant_id, n` (a single row for tenant 2)",
   trap="RLS does **not** apply to the table owner or superusers unless `FORCE ROW LEVEL SECURITY`. `current_setting('x', true)` returns NULL when unset (no rows), without `true` it raises. Connection-pool reuse means the setting must be `SET LOCAL` per transaction — gcp-curriculum 8.1 RLS.",
   setup="""CREATE TABLE work.o AS SELECT * FROM lab.customer_order;
ALTER TABLE work.o ENABLE ROW LEVEL SECURITY;
CREATE POLICY tenant_iso ON work.o USING (tenant_id = current_setting('app.tenant_id', true)::int);
CREATE ROLE app_rls NOLOGIN;
GRANT USAGE ON SCHEMA work, lab TO app_rls; GRANT SELECT ON work.o TO app_rls;
SET LOCAL ROLE app_rls; SET LOCAL app.tenant_id = '2';""",
   probe="SELECT tenant_id, count(*) AS n FROM work.o GROUP BY tenant_id",
   show=5,
   key="""ALTER TABLE work.o ENABLE ROW LEVEL SECURITY;
CREATE POLICY tenant_iso ON work.o USING (tenant_id = current_setting('app.tenant_id', true)::int);
-- as the app role:  SET LOCAL app.tenant_id = '2';  SELECT tenant_id, count(*) FROM work.o GROUP BY 1;""")

# ---------------------------------------------------------------- LEVEL 13 : analytics SQL
ex(id="E13.1", level=13, title="Subtotals with ROLLUP", tags="GROUP BY ROLLUP · GROUPING() · subtotals",
   prompt="Fulfilled 2025 orders: GMV by `(tenant_id, currency)` with **per-tenant subtotals** and a **grand total** row. Add a column `level` = `'detail'`, `'tenant'` or `'grand'` computed with `GROUPING()`.",
   out="`tenant_id, currency, gmv_minor, level`",
   trap="A subtotal row has NULL in the rolled-up column — indistinguishable from a real NULL. `GROUPING(col)` is 1 for rolled-up NULLs. Adding two currencies into one grand total is only meaningful if you say so (tenant 4 is EUR) — a business-rule trap.",
   key="""SELECT tenant_id, currency, sum(total_minor) AS gmv_minor,
       CASE GROUPING(tenant_id, currency) WHEN 0 THEN 'detail' WHEN 1 THEN 'tenant' ELSE 'grand' END AS level
FROM lab.customer_order
WHERE status = 'fulfilled' AND placed_at >= '2025-01-01' AND placed_at < '2026-01-01'
GROUP BY ROLLUP (tenant_id, currency)""")

ex(id="E13.2", level=13, title="Pivot statuses into columns", tags="conditional aggregation · pivot",
   prompt="One row per tenant with five count columns `created, paid, fulfilled, refunded, cancelled` (orders placed in 2025).",
   out="`tenant_id, created, paid, fulfilled, refunded, cancelled`",
   trap="Standard SQL has no `PIVOT` (SQL Server/Oracle/BigQuery do). The portable idiom is `count(*) FILTER (WHERE …)` or `sum(CASE …)`. The column list is fixed at write time — dynamic pivots need dynamic SQL.",
   key="""SELECT tenant_id,
  count(*) FILTER (WHERE status='created') AS created, count(*) FILTER (WHERE status='paid') AS paid,
  count(*) FILTER (WHERE status='fulfilled') AS fulfilled, count(*) FILTER (WHERE status='refunded') AS refunded,
  count(*) FILTER (WHERE status='cancelled') AS cancelled
FROM lab.customer_order WHERE placed_at >= '2025-01-01' AND placed_at < '2026-01-01' GROUP BY tenant_id""")

ex(id="E13.3", level=13, title="Build a star schema", tags="dimensional modelling · fact/dim · surrogate keys",
   prompt="""In `work`, build `dim_product(product_id, name, category_name)` (category name or `'(none)'`), `dim_date(date_key, year, month)` for 2025 and `fact_sales(order_id, line_no, date_key, product_id, qty, revenue_minor)` from **fulfilled** order lines. Then answer with the star: *revenue by category name and month for 2025*.""",
   out="`category_name, month, revenue_minor`",
   trap="Facts hold measures + foreign keys at one **grain** (an order line); dimensions hold descriptions. Decide grain first, write it in one sentence. In BigQuery you would partition the fact by date and cluster by product (gcp-curriculum 9b.1) and often *denormalise* the dimensions in.",
   stmts="""CREATE TABLE work.dim_product AS SELECT p.product_id, p.name, coalesce(c.name, '(none)') AS category_name FROM lab.product p LEFT JOIN lab.category c USING (category_id);
CREATE TABLE work.dim_date AS SELECT d::date AS date_key, extract(year FROM d)::int AS year, extract(month FROM d)::int AS month FROM generate_series('2025-01-01'::date, '2025-12-31', '1 day') d;
CREATE TABLE work.fact_sales AS SELECT l.order_id, l.line_no, o.placed_at::date AS date_key, l.product_id, l.qty, l.qty::bigint * l.unit_price_minor AS revenue_minor
  FROM lab.order_line l JOIN lab.customer_order o USING (order_id)
  WHERE o.status = 'fulfilled' AND o.placed_at >= '2025-01-01' AND o.placed_at < '2026-01-01';""",
   probe="""SELECT p.category_name, d.month, sum(f.revenue_minor) AS revenue_minor
FROM work.fact_sales f JOIN work.dim_product p USING (product_id) JOIN work.dim_date d USING (date_key) GROUP BY 1, 2""",
   key="""-- DDL as in the setup above, then:
SELECT p.category_name, d.month, sum(f.revenue_minor) AS revenue_minor
FROM work.fact_sales f JOIN work.dim_product p USING (product_id) JOIN work.dim_date d USING (date_key) GROUP BY 1, 2""")

ex(id="E13.4", level=13, title="Price history as a Type-2 dimension", tags="SCD2 · lead() · valid_to",
   prompt="From `product_price_history` build a Type-2 slowly-changing dimension: `product_id, price_minor, valid_from, valid_to, is_current` where `valid_to` is the next row's `valid_from` (NULL for the current row). Products 1–10 only.",
   out="`product_id, price_minor, valid_from, valid_to, is_current`",
   trap="`valid_to` = `lead(valid_from)` — half-open `[from, to)`. Keep `is_current` derived (`valid_to IS NULL`), never hand-set. Overlap is prevented by E10.4's exclusion constraint.",
   key="""SELECT product_id, price_minor, valid_from,
       lead(valid_from) OVER (PARTITION BY product_id ORDER BY valid_from) AS valid_to,
       lead(valid_from) OVER (PARTITION BY product_id ORDER BY valid_from) IS NULL AS is_current
FROM lab.product_price_history WHERE product_id BETWEEN 1 AND 10""")

ex(id="E13.5", level=13, title="Revenue at the price in effect", tags="as-of join · SCD2 join · range join",
   prompt="Using the SCD2 shape of E13.4, re-derive each fulfilled order line of **January 2025** at the *list price in effect at `placed_at`* and return the total difference `sum(qty × (list_price_at_order − unit_price_minor))` per tenant. (Expect a large positive number: the seed charged the *current* price, not the historical one.)",
   out="`tenant_id, price_gap_minor`",
   trap="Join on the *range* `valid_from <= placed_at AND (valid_to IS NULL OR placed_at < valid_to)` — the half-open form makes every order match exactly one row. Check that: `count(*)` of the join must equal `count(*)` of the lines.",
   key="""WITH h AS (SELECT product_id, price_minor, valid_from,
                     lead(valid_from) OVER (PARTITION BY product_id ORDER BY valid_from) AS valid_to
              FROM lab.product_price_history)
SELECT o.tenant_id, sum(l.qty::bigint * (h.price_minor - l.unit_price_minor)) AS price_gap_minor
FROM lab.order_line l JOIN lab.customer_order o USING (order_id)
JOIN h ON h.product_id = l.product_id AND h.valid_from <= o.placed_at AND (h.valid_to IS NULL OR o.placed_at < h.valid_to)
WHERE o.status = 'fulfilled' AND o.placed_at >= '2025-01-01' AND o.placed_at < '2025-02-01'
GROUP BY o.tenant_id""")
