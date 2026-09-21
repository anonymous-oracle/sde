
EX = []
def ex(**kw):
    kw.setdefault("ordered", False)
    EX.append(kw)

# ---------------------------------------------------------------- LEVEL 5 : window functions
ex(id="E5.1", level=5, title="Top-3 price ranks per category", tags="dense_rank · rank vs row_number",
   prompt="For every category (ignore uncategorised products): products whose **dense** price rank (highest price = 1) is 1, 2 or 3 within the category.",
   out="`category_id, product_id, price_minor, rnk`",
   trap="`rank` leaves gaps after ties, `dense_rank` doesn't, `row_number` breaks ties arbitrarily. You cannot filter on a window function in WHERE — wrap in a subquery/CTE.",
   key="""SELECT category_id, product_id, price_minor, rnk FROM (
  SELECT category_id, product_id, price_minor,
         dense_rank() OVER (PARTITION BY category_id ORDER BY price_minor DESC) AS rnk
  FROM lab.product WHERE category_id IS NOT NULL) x
WHERE rnk <= 3""")

ex(id="E5.2", level=5, title="Running GMV, tenant 1, March 2025", tags="running total · frame · aggregate then window",
   prompt="Tenant 1, fulfilled orders placed in March 2025: per UTC day the GMV, plus the cumulative GMV since 1 March.",
   out="`day, gmv_minor, cum_gmv_minor` (ordered by day)",
   trap="Aggregate to days **first** (CTE), then window over the days. The default frame with `ORDER BY` is `RANGE UNBOUNDED PRECEDING … CURRENT ROW` — peers (ties) are included; spell `ROWS` when you mean rows.",
   ordered=True,
   key="""WITH d AS (SELECT placed_at::date AS day, sum(total_minor) AS gmv_minor FROM lab.customer_order
            WHERE tenant_id = 1 AND status = 'fulfilled' AND placed_at >= '2025-03-01' AND placed_at < '2025-04-01' GROUP BY 1)
SELECT day, gmv_minor, sum(gmv_minor) OVER (ORDER BY day ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cum_gmv_minor
FROM d ORDER BY day""")

ex(id="E5.3", level=5, title="Days since the previous order", tags="lag · partitions",
   prompt="For users 1–20: each order with the number of whole days since the same user's previous order (NULL for their first). Use calendar days (`placed_at::date`).",
   out="`user_id, order_id, placed_at, gap_days`",
   trap="`lag` needs a total order inside the partition — add `order_id` as tie-break. `date - date` is an integer in Postgres; timestamp − timestamp is an interval.",
   key="""SELECT user_id, order_id, placed_at,
       placed_at::date - lag(placed_at::date) OVER (PARTITION BY user_id ORDER BY placed_at, order_id) AS gap_days
FROM lab.customer_order WHERE user_id BETWEEN 1 AND 20""")

ex(id="E5.4", level=5, title="Top-2 orders per user", tags="row_number · top-N per group",
   prompt="For users 1–50: their two largest orders by `total_minor` (ties → lower `order_id`), with the position 1 or 2.",
   out="`user_id, order_id, total_minor, rn`",
   trap="`LIMIT 2` gives two rows overall, not per user. The tie-break is part of the spec — without it two correct answers differ.",
   key="""SELECT user_id, order_id, total_minor, rn FROM (
  SELECT user_id, order_id, total_minor,
         row_number() OVER (PARTITION BY user_id ORDER BY total_minor DESC, order_id) AS rn
  FROM lab.customer_order WHERE user_id BETWEEN 1 AND 50) x WHERE rn <= 2""")

ex(id="E5.5", level=5, title="Tenant share of 2025 GMV", tags="sum() OVER () · ratio to total",
   prompt="Per tenant: fulfilled GMV in 2025 and its percentage of the all-tenant total, rounded to 2 decimals.",
   out="`tenant_id, gmv_minor, pct`",
   trap="Window over the *aggregated* result: `sum(sum(x)) OVER ()`. Cast to numeric before dividing.",
   key="""SELECT tenant_id, sum(total_minor) AS gmv_minor,
       round(100.0 * sum(total_minor) / sum(sum(total_minor)) OVER (), 2) AS pct
FROM lab.customer_order
WHERE status = 'fulfilled' AND placed_at >= '2025-01-01' AND placed_at < '2026-01-01'
GROUP BY tenant_id""")

ex(id="E5.6", level=5, title="Price quartiles, tenant 2", tags="ntile · bucket boundaries",
   prompt="Live products of tenant 2 split into 4 price quartiles with `ntile(4)` ordered by price ascending then `product_id`.",
   out="`product_id, price_minor, quartile`",
   trap="`ntile` splits by **row count**, not by value — equal prices can land in different tiles; and if N is not divisible by 4 the first tiles get the extra rows.",
   key="""SELECT product_id, price_minor, ntile(4) OVER (ORDER BY price_minor, product_id) AS quartile
FROM lab.product WHERE tenant_id = 2 AND discontinued_at IS NULL""")

ex(id="E5.7", level=5, title="First and last price", tags="first_value · last_value · frame trap",
   prompt="For products 1–20: the first and last `price_minor` in `product_price_history` (by `valid_from`) and the change (last − first).",
   out="`product_id, first_price, last_price, delta`",
   trap="`last_value(x) OVER (ORDER BY t)` returns the *current* row when the default frame stops at CURRENT ROW. You need `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING`, or use `first_value` with a reversed ORDER BY.",
   key="""SELECT DISTINCT product_id,
       first_value(price_minor) OVER w AS first_price,
       last_value(price_minor)  OVER w AS last_price,
       last_value(price_minor) OVER w - first_value(price_minor) OVER w AS delta
FROM lab.product_price_history WHERE product_id BETWEEN 1 AND 20
WINDOW w AS (PARTITION BY product_id ORDER BY valid_from ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)""")

ex(id="E5.8", level=5, title="7-day moving average of daily orders", tags="ROWS frame · moving average · warm-up rows",
   prompt="Tenant 2, orders placed in February 2025: per day the order count and the average of the current and previous 6 days' counts, rounded to 2 decimals. Emit the average only when a full 7-day window exists inside February (from 7 Feb).",
   out="`day, n, avg7` (ordered by day)",
   trap="A `ROWS 6 PRECEDING` frame silently shrinks at the start — you must suppress the warm-up rows yourself. `ROWS` counts rows, so missing days (gaps) would silently stretch the window; here there are no empty days — say why you checked.",
   ordered=True,
   key="""SELECT day, n, avg7 FROM (
  SELECT day, n, row_number() OVER (ORDER BY day) AS rn,
         round(avg(n) OVER (ORDER BY day ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) AS avg7
  FROM (SELECT placed_at::date AS day, count(*) AS n FROM lab.customer_order
        WHERE tenant_id = 2 AND placed_at >= '2025-02-01' AND placed_at < '2025-03-01' GROUP BY 1) d) x
WHERE rn >= 7 ORDER BY day""")

# ---------------------------------------------------------------- LEVEL 6 : advanced windows
ex(id="E6.1", level=6, title="Longest login streak", tags="gaps and islands · row_number difference",
   prompt="From `login_day` (users 1–200, 120 days): each user's longest run of **consecutive** days and the day it started (earliest start on ties).",
   out="`user_id, streak_len, streak_start`",
   trap="Consecutive days share a constant `day − row_number()`. Do not use `count(*)` per user, and do not forget that the PK already guarantees no duplicate days (if it didn't, dedupe before numbering).",
   key="""WITH g AS (SELECT user_id, day, day - (row_number() OVER (PARTITION BY user_id ORDER BY day))::int AS grp FROM lab.login_day),
runs AS (SELECT user_id, min(day) AS streak_start, count(*) AS streak_len FROM g GROUP BY user_id, grp),
ranked AS (SELECT *, row_number() OVER (PARTITION BY user_id ORDER BY streak_len DESC, streak_start) AS rn FROM runs)
SELECT user_id, streak_len, streak_start FROM ranked WHERE rn = 1""")

ex(id="E6.2", level=6, title="Sessionise the event stream", tags="sessionization · lag · cumulative sum",
   prompt="For identified users (`user_id IS NOT NULL`): a new session starts when the gap to the user's previous event is **> 30 minutes** (or there is no previous event). Return one row per session: user, session number (1-based per user, by time), event count, first and last event time.",
   out="`user_id, session_no, n_events, started_at, ended_at`",
   trap="Three steps: (1) `lag` to get the gap, (2) flag `gap > interval '30 minutes' OR gap IS NULL`, (3) running `sum(flag)` as the session id. Ties on `occurred_at` need an `event_id` tie-break.",
   key="""WITH e AS (SELECT user_id, event_id, occurred_at,
                   occurred_at - lag(occurred_at) OVER (PARTITION BY user_id ORDER BY occurred_at, event_id) AS gap
            FROM lab.event WHERE user_id IS NOT NULL),
f AS (SELECT *, CASE WHEN gap IS NULL OR gap > interval '30 minutes' THEN 1 ELSE 0 END AS is_start FROM e),
s AS (SELECT *, sum(is_start) OVER (PARTITION BY user_id ORDER BY occurred_at, event_id) AS session_no FROM f)
SELECT user_id, session_no, count(*) AS n_events, min(occurred_at) AS started_at, max(occurred_at) AS ended_at
FROM s GROUP BY user_id, session_no""")

ex(id="E6.3", level=6, title="Ordered funnel", tags="conditional aggregation · ordered steps",
   prompt="How many identified users performed `add_to_cart`, later `checkout_start`, later `purchase` — in that order (each step strictly after the previous, using each user's **first** occurrence of the step)? One number, plus the counts that reached step 1 and step 2 as a funnel.",
   out="`n_cart, n_checkout, n_purchase` (one row)",
   trap="`count(DISTINCT user_id) WHERE event_type = …` per step ignores order. Compute each user's first time per step with `min(…) FILTER`, then compare the timestamps.",
   key="""WITH t AS (SELECT user_id,
       min(occurred_at) FILTER (WHERE event_type = 'add_to_cart')    AS t_cart,
       min(occurred_at) FILTER (WHERE event_type = 'checkout_start') AS t_co,
       min(occurred_at) FILTER (WHERE event_type = 'purchase')       AS t_buy
     FROM lab.event WHERE user_id IS NOT NULL GROUP BY user_id)
SELECT count(*) FILTER (WHERE t_cart IS NOT NULL) AS n_cart,
       count(*) FILTER (WHERE t_cart < t_co) AS n_checkout,
       count(*) FILTER (WHERE t_cart < t_co AND t_co < t_buy) AS n_purchase
FROM t""")

ex(id="E6.4", level=6, title="Price in effect at order time (as-of join)", tags="as-of join · LATERAL · temporal correctness",
   prompt="For order lines of orders placed **before 2025-01-04**: the list price that was in effect at `placed_at` (the history row with the greatest `valid_from <= placed_at`), and the lines where the price actually charged (`unit_price_minor`) differs from it.",
   out="`order_id, line_no, unit_price_minor, price_at_order`",
   trap="A plain equi-join on `product_id` returns three rows per line. Use `LATERAL … ORDER BY valid_from DESC LIMIT 1` (or `DISTINCT ON`, or a window). The `<=` boundary is inclusive: an order at exactly `valid_from` sees the *new* price. This is the same shape as gcp-curriculum **9c.1** point-in-time joins.",
   key="""SELECT l.order_id, l.line_no, l.unit_price_minor, h.price_minor AS price_at_order
FROM lab.order_line l JOIN lab.customer_order o USING (order_id)
CROSS JOIN LATERAL (SELECT price_minor FROM lab.product_price_history h
                    WHERE h.product_id = l.product_id AND h.valid_from <= o.placed_at
                    ORDER BY h.valid_from DESC LIMIT 1) h
WHERE o.placed_at < '2025-01-04' AND l.unit_price_minor <> h.price_minor""")

ex(id="E6.5", level=6, title="Orders in the previous 30 days", tags="RANGE frame with interval · self-window",
   prompt="For users 1–20: each order and how many **other** orders the same user placed in the 30 days before it (`placed_at − 30 days` up to and including this order's time, excluding itself).",
   out="`user_id, order_id, prior_30d`",
   trap="A `RANGE BETWEEN INTERVAL '30 days' PRECEDING AND CURRENT ROW` frame includes the current row *and its peers*; subtract 1 and think about equal timestamps. `ROWS 30 PRECEDING` would count rows, not days.",
   key="""SELECT user_id, order_id,
       (count(*) OVER (PARTITION BY user_id ORDER BY placed_at RANGE BETWEEN INTERVAL '30 days' PRECEDING AND CURRENT ROW) - 1) AS prior_30d
FROM lab.customer_order WHERE user_id BETWEEN 1 AND 20""")

ex(id="E6.6", level=6, title="Signup-cohort activation", tags="cohort analysis · date_trunc · conditional counts",
   prompt="Cohort = signup month (`date_trunc('month', created_at)`). For each cohort: size, and how many of its users placed at least one order in the **calendar month after** their signup month.",
   out="`cohort_month, size, active_next_month`",
   trap="Two grains at once (users, then orders). Compute *per-user* activation first (`EXISTS`), then aggregate by cohort — do not join users to orders and `count(*)`.",
   key="""SELECT date_trunc('month', u.created_at)::date AS cohort_month, count(*) AS size,
       count(*) FILTER (WHERE EXISTS (
          SELECT 1 FROM lab.customer_order o WHERE o.user_id = u.user_id
            AND o.placed_at >= date_trunc('month', u.created_at) + interval '1 month'
            AND o.placed_at <  date_trunc('month', u.created_at) + interval '2 months')) AS active_next_month
FROM lab.app_user u GROUP BY 1""")

ex(id="E6.7", level=6, title="Dedupe events, keep the first", tags="row_number · deduplication · planted test data",
   prompt="Some pipelines deliver twice. Treat two events as the same delivery when `(user_id, event_type, occurred_at)` are equal (NULL users count as equal to each other). Run your query against this **planted** input `e` (the real table plus 6,000 duplicate deliveries with ids +1,000,000): `SELECT * FROM lab.event UNION ALL SELECT event_id + 1000000, tenant_id, user_id, event_type, occurred_at, payload FROM lab.event WHERE event_id % 10 = 0`. Return the `event_id`s that are **not** the lowest id in their duplicate group.",
   out="`event_id`",
   trap="`PARTITION BY` treats NULLs as one group (unlike `=`). Run the query on the *un-planted* table too: it must return 0 rows — an empty result is a valid, testable answer, but only if you have also seen it return the planted rows.",
   key="""SELECT event_id FROM (
  SELECT event_id, row_number() OVER (PARTITION BY user_id, event_type, occurred_at ORDER BY event_id) AS rn
  FROM (SELECT * FROM lab.event UNION ALL
        SELECT event_id + 1000000, tenant_id, user_id, event_type, occurred_at, payload FROM lab.event WHERE event_id % 10 = 0) e) x
WHERE rn > 1""")

# ---------------------------------------------------------------- LEVEL 7 : recursion
ex(id="E7.1", level=7, title="Category paths", tags="recursive CTE · tree · path",
   prompt="For tenant 1's category tree: every category with its depth (root = 0) and the `' > '`-joined path of **names** from the root.",
   out="`category_id, depth, path`",
   trap="A recursive CTE = anchor (roots: `parent_id IS NULL`) `UNION ALL` recursive step joining on `parent_id`. Termination is guaranteed only if the data has no cycles — the seed does, a hostile import might not (E7.5).",
   key="""WITH RECURSIVE t AS (
  SELECT category_id, 0 AS depth, name::text AS path FROM lab.category WHERE tenant_id = 1 AND parent_id IS NULL
  UNION ALL
  SELECT c.category_id, t.depth + 1, t.path || ' > ' || c.name
  FROM lab.category c JOIN t ON c.parent_id = t.category_id)
SELECT category_id, depth, path FROM t""")

ex(id="E7.2", level=7, title="Products in a subtree", tags="recursive CTE · rollup up the tree",
   prompt="For every category of tenant 1: the number of products attached to it **or any descendant**.",
   out="`category_id, subtree_products`",
   trap="Materialise (ancestor, descendant) pairs, then join products to *descendant* and group by *ancestor*. A category with no products still needs a row — LEFT JOIN.",
   key="""WITH RECURSIVE a AS (
  SELECT category_id AS anc, category_id AS des FROM lab.category WHERE tenant_id = 1
  UNION ALL
  SELECT a.anc, c.category_id FROM a JOIN lab.category c ON c.parent_id = a.des)
SELECT a.anc AS category_id, count(p.product_id) AS subtree_products
FROM a LEFT JOIN lab.product p ON p.category_id = a.des GROUP BY a.anc""")

ex(id="E7.3", level=7, title="Referral roots and depth", tags="recursive CTE · forest · depth",
   prompt="Users form a referral forest (`referred_by` → parent). For every user: the root user of their tree and their depth (root = 0).",
   out="`user_id, root_id, depth`",
   trap="Roots are the rows with `referred_by IS NULL`; carry `root_id` through the recursion instead of recomputing it. Prove termination: `referred_by < user_id` holds in this seed, so no cycle — state that invariant, don't assume it.",
   key="""WITH RECURSIVE f AS (
  SELECT user_id, user_id AS root_id, 0 AS depth FROM lab.app_user WHERE referred_by IS NULL
  UNION ALL
  SELECT u.user_id, f.root_id, f.depth + 1 FROM lab.app_user u JOIN f ON u.referred_by = f.user_id)
SELECT user_id, root_id, depth FROM f""")

ex(id="E7.4", level=7, title="Biggest referral tree", tags="recursive CTE · aggregate over recursion",
   prompt="The root user whose tree (including the root) has the most members; ties → lowest `user_id`.",
   out="`root_id, tree_size`",
   trap="Aggregate *after* the recursion. `ORDER BY tree_size DESC, root_id LIMIT 1`.",
   probe="""WITH RECURSIVE f AS (
  SELECT user_id, user_id AS root_id FROM lab.app_user WHERE referred_by IS NULL
  UNION ALL SELECT u.user_id, f.root_id FROM lab.app_user u JOIN f ON u.referred_by = f.user_id)
SELECT root_id, count(*) AS tree_size FROM f GROUP BY root_id ORDER BY tree_size DESC, root_id LIMIT 1""",
   ordered=True, show=3,
   key="""WITH RECURSIVE f AS (
  SELECT user_id, user_id AS root_id FROM lab.app_user WHERE referred_by IS NULL
  UNION ALL SELECT u.user_id, f.root_id FROM lab.app_user u JOIN f ON u.referred_by = f.user_id)
SELECT root_id, count(*) AS tree_size FROM f GROUP BY root_id ORDER BY tree_size DESC, root_id LIMIT 1""")

ex(id="E7.5", level=7, title="Find the cycle", tags="recursive CTE · cycle detection · path array",
   prompt="Directed edges are given inline: `(1,2),(2,3),(3,1),(4,5),(5,6)`. Return every node that lies on a cycle.",
   out="`node`",
   trap="Carry a `path` array and stop when the next node is already in it (`NOT next = ANY(path)`); a node is on a cycle if it can reach itself. PostgreSQL 14+ also has `CYCLE … SET … USING` — write it both ways.",
   show=5,
   key="""WITH RECURSIVE e(a, b) AS (VALUES (1,2),(2,3),(3,1),(4,5),(5,6)),
w AS (
  SELECT a AS start, b AS node, ARRAY[a, b] AS path FROM e
  UNION ALL
  SELECT w.start, e.b, w.path || e.b FROM w JOIN e ON e.a = w.node WHERE e.b <> ALL (w.path[2:]))
SELECT DISTINCT start AS node FROM w WHERE node = start""")

# ---------------------------------------------------------------- LEVEL 8 : time, JSON, text, cleaning
ex(id="E8.1", level=8, title="Average delivery time by carrier", tags="interval arithmetic · extract(epoch)",
   prompt="For delivered shipments: per carrier, the count and the mean transit time in **days** (shipped → delivered) rounded to 2 decimals.",
   out="`carrier, n, avg_days`",
   trap="`avg(interval)` is legal but unreadable; convert with `extract(epoch FROM …) / 86400` — as `numeric`, not float, before rounding. NULL `delivered_at` rows are excluded by the filter, not by luck.",
   key="""SELECT carrier, count(*) AS n,
       round(avg(extract(epoch FROM (delivered_at - shipped_at)) / 86400)::numeric, 2) AS avg_days
FROM lab.shipment WHERE delivered_at IS NOT NULL GROUP BY carrier""")

ex(id="E8.2", level=8, title="Stuck shipments as of a fixed instant", tags="reproducible time · never now()",
   prompt="Shipments not delivered more than 14 days after shipping, **as of `2026-01-01 00:00 UTC`** (undelivered and shipped before 2025-12-18).",
   out="`shipment_id`",
   trap="Never call `now()` in a graded query — the answer changes daily. Parameterise the 'as-of' instant. Same principle as the gcp-curriculum ledger's determinism rules.",
   key="""SELECT shipment_id FROM lab.shipment
WHERE delivered_at IS NULL AND shipped_at < timestamptz '2026-01-01 00:00+00' - interval '14 days'""")

ex(id="E8.3", level=8, title="UTC day vs New York day", tags="AT TIME ZONE · DST",
   prompt="How many orders have a **different calendar date** in `America/New_York` than in UTC? One number.",
   out="`n`",
   trap="`ts AT TIME ZONE 'x'` on a `timestamptz` returns a *timestamp without zone* in that zone; on a plain `timestamp` it does the reverse. Get the direction right and test across the 2025-03-09 DST change.",
   key="""SELECT count(*) AS n FROM lab.customer_order
WHERE (placed_at AT TIME ZONE 'America/New_York')::date <> (placed_at AT TIME ZONE 'UTC')::date""")

ex(id="E8.4", level=8, title="Orders per ISO week", tags="date_trunc('week') · week boundaries",
   prompt="Orders placed in 2025 grouped by ISO week (Monday start): week start date and count.",
   out="`week_start, n`",
   trap="`date_trunc('week')` starts on Monday (ISO); BigQuery's `DATE_TRUNC(d, WEEK)` starts on Sunday. The first/last week straddles the year boundary.",
   key="""SELECT date_trunc('week', placed_at)::date AS week_start, count(*) AS n
FROM lab.customer_order WHERE placed_at >= '2025-01-01' AND placed_at < '2026-01-01' GROUP BY 1""")

ex(id="E8.5", level=8, title="Red eco products", tags="JSONB · @> · ? operator",
   prompt="Products whose `attrs` has `color = 'red'` **and** whose `attrs.tags` array contains `'eco'`.",
   out="`product_id`",
   trap="`attrs->>'color'` returns text; `attrs @> '{\"color\":\"red\"}'` is index-friendly (GIN). `attrs->'tags' ? 'eco'` tests membership in an array of strings. A missing key yields NULL, not false.",
   key="""SELECT product_id FROM lab.product WHERE attrs @> '{"color":"red"}' AND attrs->'tags' ? 'eco'""")

ex(id="E8.6", level=8, title="Search latency by query term", tags="JSONB extraction · casts",
   prompt="For `search` events: per query term (`payload->>'q'`) the number of events and the average `payload->>'ms'` rounded to 1 decimal.",
   out="`q, n, avg_ms`",
   trap="`->>` returns text — cast before averaging: `(payload->>'ms')::int`. A non-numeric value would fail the whole query — in production, validate on write.",
   key="""SELECT payload->>'q' AS q, count(*) AS n, round(avg((payload->>'ms')::int), 1) AS avg_ms
FROM lab.event WHERE event_type = 'search' GROUP BY 1""")

ex(id="E8.7", level=8, title="Products per tag", tags="jsonb_array_elements_text · unnesting",
   prompt="Explode `attrs.tags` and count products per tag.",
   out="`tag, n`",
   trap="A set-returning function in FROM (`CROSS JOIN LATERAL jsonb_array_elements_text(attrs->'tags')`) drops products with no tags — usually what you want; say so. In BigQuery this is `UNNEST`.",
   key="""SELECT tag, count(*) AS n FROM lab.product p
CROSS JOIN LATERAL jsonb_array_elements_text(p.attrs->'tags') AS tag GROUP BY tag""")

ex(id="E8.8", level=8, title="Clean and dedupe emails", tags="trim · lower · regex · dedupe",
   prompt="From `lab.stg_import`: normalise `email_text` with `lower(trim(…))`, keep only values that match `^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$`, and keep the **lowest `row_id`** for each normalised address.",
   out="`row_id, email_norm`",
   trap="Empty string and NULL are both invalid; `frank@example` has no dot. Normalise **before** deduping, or 'Ann@Example.com ' and 'ann@example.com' survive as two people.",
   show=15,
   key="""SELECT row_id, email_norm FROM (
  SELECT row_id, lower(trim(email_text)) AS email_norm,
         row_number() OVER (PARTITION BY lower(trim(email_text)) ORDER BY row_id) AS rn
  FROM lab.stg_import
  WHERE lower(trim(email_text)) ~ '^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$') x
WHERE rn = 1""")

ex(id="E8.9", level=8, title="Parse money text into minor units", tags="regexp · CASE · safe casts",
   prompt="Convert `amount_text` to integer **minor units** (×100, rounded half up). Accept an optional leading `-`, optional `$`, thousands separators `,` (only in groups of exactly three) and an optional decimal part with `.`; surrounding spaces are ignored. Anything else — `12,50`, `abc`, `1e3`, NULL — becomes NULL.",
   out="`row_id, amount_minor`",
   trap="Decide the rule for `12,50` (European decimal comma) explicitly — here it is *invalid*, never guessed. Validate with a regex **before** casting; a bare `::numeric` on bad text aborts the whole statement.",
   show=15,
   key="""SELECT row_id,
  CASE WHEN c ~ '^-?([0-9]{1,3}(,[0-9]{3})+|[0-9]+)(\\.[0-9]+)?$'
       THEN round(replace(c, ',', '')::numeric * 100)::bigint END AS amount_minor
FROM (SELECT row_id, replace(trim(amount_text), '$', '') AS c FROM lab.stg_import) s""")

ex(id="E8.10", level=8, title="Write a total date parser", tags="user-defined function · exception handling · dialect",
   prompt="Create `work.try_date(text) RETURNS date` that returns a date for: ISO `YYYY-MM-DD` (after trimming, and also when followed by a `T…` time), `MM/DD/YYYY`, and `D Mon YYYY` (e.g. `1 Mar 2025`); **NULL** for anything else, including impossible dates like `2025-13-40` and `2025-02-29`. Then `SELECT row_id, work.try_date(signup_text)` over `stg_import`.",
   out="`row_id, d`",
   trap="A cast error aborts the statement; catch it in a `BEGIN … EXCEPTION WHEN others THEN RETURN NULL` block (PL/pgSQL). Postgres 16 adds `pg_input_is_valid()`; BigQuery has `SAFE.PARSE_DATE`, SQL Server `TRY_CONVERT`. `2025-02-29` must fail — 2025 is not a leap year.",
   setup="""CREATE OR REPLACE FUNCTION work.try_date(t text) RETURNS date LANGUAGE plpgsql IMMUTABLE AS $$
DECLARE s text := btrim(t);
BEGIN
  IF s IS NULL OR s = '' THEN RETURN NULL; END IF;
  IF s ~ '^\\d{4}-\\d{2}-\\d{2}(T.*)?$' THEN RETURN to_date(left(s, 10), 'YYYY-MM-DD')::date;
  ELSIF s ~ '^\\d{1,2}/\\d{1,2}/\\d{4}$' THEN RETURN to_date(s, 'MM/DD/YYYY');
  ELSIF s ~ '^\\d{1,2} [A-Za-z]{3} \\d{4}$' THEN RETURN to_date(s, 'DD Mon YYYY');
  END IF;
  RETURN NULL;
EXCEPTION WHEN others THEN RETURN NULL;
END $$;""",
   probe="SELECT row_id, work.try_date(signup_text) AS d FROM lab.stg_import",
   show=15,
   key="""-- function body as in the setup above; then:
SELECT row_id, work.try_date(signup_text) AS d FROM lab.stg_import""")
