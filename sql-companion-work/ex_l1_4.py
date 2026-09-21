
# Each exercise: id, title, tags, prompt, out, trap, key, ordered, [setup, stmts, probe, show, ext, stitch]
EX = []
def ex(**kw):
    kw.setdefault("ordered", False)
    EX.append(kw)

# ---------------------------------------------------------------- LEVEL 1 : SELECT, filter, NULL, CASE
ex(id="E1.1", level=1, title="Q2-2024 signups from GB or DE", tags="WHERE · half-open ranges",
   prompt="Users whose country is GB or DE and who were created in the second quarter of 2024 (April, May and June, UTC).",
   out="`user_id, email`",
   trap="`BETWEEN '2024-04-01' AND '2024-06-30'` silently drops most of 30 June for a `timestamptz`. Use `>= start AND < next_start`.",
   key="""SELECT user_id, email
FROM lab.app_user
WHERE country IN ('GB','DE')
  AND created_at >= '2024-04-01' AND created_at < '2024-07-01'""")

ex(id="E1.2", level=1, title="Unknown country", tags="NULL · IS NULL",
   prompt="Users whose country is unknown (stored as NULL).",
   out="`user_id`",
   trap="`country = NULL` is never true — it is UNKNOWN. Also note `char(2)` pads; do not compare with `''`.",
   key="SELECT user_id FROM lab.app_user WHERE country IS NULL")

ex(id="E1.3", level=1, title="Everyone not known to be in the US", tags="NULL · 3VL · IS DISTINCT FROM",
   prompt="All users who are not known to be in the US — this **includes** users whose country is unknown.",
   out="`user_id`",
   trap="`country <> 'US'` drops the NULL-country users (UNKNOWN is not TRUE). Use `IS DISTINCT FROM`, or `country <> 'US' OR country IS NULL`. Write the 3VL truth table for `NOT (country = 'US')` first.",
   key="SELECT user_id FROM lab.app_user WHERE country IS DISTINCT FROM 'US'")

ex(id="E1.4", level=1, title="Mid-priced live catalogue, top 20", tags="WHERE · ORDER BY · LIMIT · determinism",
   prompt="Products with `price_minor` from 1000 to 2000 inclusive that are not discontinued, most expensive first, ties broken by lowest `product_id`; first 20 rows only.",
   out="`product_id, price_minor` (ordered)",
   trap="`LIMIT` without a total order is non-deterministic. `discontinued_at IS NULL`, not `= NULL`. Both bounds are inclusive here (integer money, so `BETWEEN` is safe).",
   ordered=True,
   key="""SELECT product_id, price_minor
FROM lab.product
WHERE price_minor BETWEEN 1000 AND 2000 AND discontinued_at IS NULL
ORDER BY price_minor DESC, product_id
LIMIT 20""")

ex(id="E1.5", level=1, title="Reviews with no text", tags="NULL vs empty string · COALESCE",
   prompt="Reviews whose body is missing — treat NULL and the empty string as the same thing.",
   out="`review_id`",
   trap="NULL and `''` are different values; a test for one silently misses the other. In Oracle they collapse into one — a dialect trap (see the Rosetta table).",
   key="SELECT review_id FROM lab.review WHERE coalesce(body, '') = ''")

ex(id="E1.6", level=1, title="Order status buckets", tags="CASE · expressions",
   prompt="Label every order: `open` for created/paid, `done` for fulfilled, `closed` for cancelled/refunded.",
   out="`order_id, bucket`",
   trap="A `CASE` without `ELSE` yields NULL for unmatched values — add a defensive `ELSE 'unknown'` and say why it should never fire (the `CHECK` constraint).",
   key="""SELECT order_id,
       CASE status WHEN 'created' THEN 'open' WHEN 'paid' THEN 'open'
                   WHEN 'fulfilled' THEN 'done'
                   WHEN 'cancelled' THEN 'closed' WHEN 'refunded' THEN 'closed'
                   ELSE 'unknown' END AS bucket
FROM lab.customer_order""")

ex(id="E1.7", level=1, title="Ten priciest live products", tags="ORDER BY · LIMIT · tie-break",
   prompt="The ten most expensive products that are not discontinued (ties → lowest `product_id`).",
   out="`product_id, price_minor` (ordered)",
   trap="Sorting by price alone and hoping. State the tie-break in the spec *before* you write the query.",
   ordered=True,
   key="""SELECT product_id, price_minor FROM lab.product
WHERE discontinued_at IS NULL
ORDER BY price_minor DESC, product_id LIMIT 10""")

ex(id="E1.8", level=1, title="Pattern search", tags="LIKE · ILIKE · escaping",
   prompt="Products whose SKU starts with `SKU-01` and ends with `7`.",
   out="`product_id`",
   trap="`_` and `%` are wildcards — to match a literal underscore you need `ESCAPE`. A leading-wildcard pattern (`'%7'`) cannot use a B-tree index (see the P3 prediction card).",
   key="SELECT product_id FROM lab.product WHERE sku LIKE 'SKU-01%' AND sku LIKE '%7'")

# ---------------------------------------------------------------- LEVEL 2 : aggregation
ex(id="E2.1", level=2, title="Orders and revenue by status", tags="GROUP BY · SUM",
   prompt="For each order status: number of orders and the sum of `total_minor`.",
   out="`status, n_orders, sum_minor`",
   trap="Every non-aggregated SELECT column must be in GROUP BY (or functionally dependent on the PK). Money is an integer of minor units — never `float`.",
   key="SELECT status, count(*) AS n_orders, sum(total_minor) AS sum_minor FROM lab.customer_order GROUP BY status")

ex(id="E2.2", level=2, title="Monthly fulfilled GMV, 2025", tags="date_trunc · GROUP BY · time zones",
   prompt="For fulfilled orders placed in calendar 2025 (UTC): month start, order count, and GMV (`sum(total_minor)`).",
   out="`month, n_orders, gmv_minor`",
   trap="`date_trunc('month', timestamptz)` uses the **session** time zone. The lab pins `UTC`; production rarely does — always state the zone.",
   key="""SELECT date_trunc('month', placed_at) AS month, count(*) AS n_orders, sum(total_minor) AS gmv_minor
FROM lab.customer_order
WHERE status = 'fulfilled' AND placed_at >= '2025-01-01' AND placed_at < '2026-01-01'
GROUP BY 1""")

ex(id="E2.3", level=2, title="Well-reviewed products", tags="HAVING · WHERE vs HAVING · ROUND",
   prompt="Products with at least 10 reviews: review count and average rating rounded to 2 decimals.",
   out="`product_id, n, avg_rating`",
   trap="`WHERE` filters rows *before* grouping, `HAVING` filters groups *after*. `avg(smallint)` is `numeric`, so `round(avg(rating), 2)` works; in engines with integer division check the type.",
   key="""SELECT product_id, count(*) AS n, round(avg(rating), 2) AS avg_rating
FROM lab.review GROUP BY product_id HAVING count(*) >= 10""")

ex(id="E2.4", level=2, title="Buyers per tenant", tags="COUNT(DISTINCT) · count(*) vs count(col)",
   prompt="Per tenant: number of orders and number of *distinct* users who placed at least one order.",
   out="`tenant_id, n_orders, n_buyers`",
   trap="`count(*)` counts rows, `count(col)` skips NULLs, `count(DISTINCT col)` de-duplicates. Say which one each output column needs.",
   key="""SELECT tenant_id, count(*) AS n_orders, count(DISTINCT user_id) AS n_buyers
FROM lab.customer_order GROUP BY tenant_id""")

ex(id="E2.5", level=2, title="Refund rate by tenant", tags="FILTER · conditional aggregation · integer division",
   prompt="Per tenant: total orders, refunded orders, and refund rate = refunded / total rounded to 4 decimals.",
   out="`tenant_id, n_orders, n_refunded, refund_rate`",
   trap="`1/3` in integer arithmetic is 0. Cast one side to `numeric` *before* dividing. `count(*) FILTER (WHERE …)` is the standard-SQL way; `SUM(CASE …)` is the portable way.",
   key="""SELECT tenant_id, count(*) AS n_orders,
       count(*) FILTER (WHERE status = 'refunded') AS n_refunded,
       round(count(*) FILTER (WHERE status = 'refunded')::numeric / count(*), 4) AS refund_rate
FROM lab.customer_order GROUP BY tenant_id""")

ex(id="E2.6", level=2, title="Users by country including unknown", tags="GROUP BY NULL · COALESCE",
   prompt="Number of users per country; label unknown as `'??'`.",
   out="`country, n`",
   trap="GROUP BY puts all NULLs in **one** group (unlike `=`). `country` is `char(2)` so `'US'` and `'US '` compare equal — but `coalesce(country,'??')` must be a valid `char(2)`.",
   key="SELECT coalesce(country, '??') AS country, count(*) AS n FROM lab.app_user GROUP BY 1")

ex(id="E2.7", level=2, title="Median order value per tenant", tags="ordered-set aggregates · percentile_disc",
   prompt="Per tenant, the median `total_minor` of fulfilled orders, defined as `percentile_disc(0.5)` (an actual value from the data).",
   out="`tenant_id, median_minor`",
   trap="`avg` is not the median. `percentile_cont` interpolates and returns `double precision` — a float in a money pipeline. State which definition you use.",
   key="""SELECT tenant_id, percentile_disc(0.5) WITHIN GROUP (ORDER BY total_minor) AS median_minor
FROM lab.customer_order WHERE status = 'fulfilled' GROUP BY tenant_id""")

ex(id="E2.8", level=2, title="Price histogram", tags="bucketing · integer division",
   prompt="Bucket **live** products (not discontinued) into price bands of width 1000 minor units: band start (0, 1000, 2000, …) and product count.",
   out="`band_start, n`",
   trap="`price_minor / 1000 * 1000` relies on integer division truncation — fine in Postgres, wrong in engines that return decimals (dialect trap). `width_bucket` is the explicit alternative.",
   key="""SELECT (price_minor / 1000) * 1000 AS band_start, count(*) AS n
FROM lab.product WHERE discontinued_at IS NULL GROUP BY 1""")

# ---------------------------------------------------------------- LEVEL 3 : joins
ex(id="E3.1", level=3, title="Paid orders with buyer and tenant", tags="INNER JOIN · multi-table",
   prompt="Orders with status `paid` placed in March 2025, tenant 2: order id, buyer email, tenant name, total.",
   out="`order_id, email, tenant_name, total_minor`",
   trap="Filter on the *driving* table in WHERE; join keys go in ON. Three tables, two ON clauses — write the join graph as a picture first.",
   key="""SELECT o.order_id, u.email, t.name AS tenant_name, o.total_minor
FROM lab.customer_order o
JOIN lab.app_user u ON u.user_id = o.user_id
JOIN lab.tenant   t ON t.tenant_id = o.tenant_id
WHERE o.tenant_id = 2 AND o.status = 'paid'
  AND o.placed_at >= '2025-03-01' AND o.placed_at < '2025-04-01'""")

ex(id="E3.2", level=3, title="Users who never referred anyone", tags="anti-join · NOT IN + NULL trap",
   prompt="Users who are not the referrer of any other user.",
   out="`user_id`",
   trap="`WHERE user_id NOT IN (SELECT referred_by FROM app_user)` returns **zero rows** because `referred_by` contains NULLs (`x NOT IN (…, NULL)` is never TRUE). Write it three ways: NOT EXISTS, LEFT JOIN … IS NULL, and NOT IN with a NULL filter — all three must give the same fingerprint.",
   key="""SELECT u.user_id FROM lab.app_user u
WHERE NOT EXISTS (SELECT 1 FROM lab.app_user r WHERE r.referred_by = u.user_id)""")

ex(id="E3.3", level=3, title="Users who never ordered", tags="LEFT JOIN … IS NULL · anti-join",
   prompt="Users with no order at all (any status).",
   out="`user_id`",
   trap="Test the *right-hand primary key* for NULL, not a column that can legitimately be NULL on the right.",
   key="""SELECT u.user_id FROM lab.app_user u
LEFT JOIN lab.customer_order o ON o.user_id = u.user_id
WHERE o.order_id IS NULL""")

ex(id="E3.4", level=3, title="Products not sold in a week", tags="anti-join · date ranges",
   prompt="Products that appear on **no** order line of a fulfilled order placed during 2025-01-01 … 2025-01-07 (inclusive, UTC).",
   out="`product_id`",
   trap="Where does the date filter go? Inside the `NOT EXISTS` subquery (or the `ON` of the LEFT JOIN) — not in the outer WHERE, where it would turn the anti-join into an inner join.",
   key="""SELECT p.product_id FROM lab.product p
WHERE NOT EXISTS (
  SELECT 1 FROM lab.order_line l JOIN lab.customer_order o USING (order_id)
  WHERE l.product_id = p.product_id AND o.status = 'fulfilled'
    AND o.placed_at >= '2025-01-01' AND o.placed_at < '2025-01-08')""")

ex(id="E3.5", level=3, title="Revenue of delivered orders", tags="semi-join · fan-out trap",
   prompt="Total `total_minor` of fulfilled orders that have **at least one** delivered shipment (`delivered_at IS NOT NULL`). One number.",
   out="`revenue_minor`",
   trap="`JOIN shipment` fans out: orders with two shipments are counted twice. Semi-join (`EXISTS`) never multiplies rows. Compute the naive join answer too and explain the difference in one sentence.",
   key="""SELECT sum(o.total_minor) AS revenue_minor FROM lab.customer_order o
WHERE o.status = 'fulfilled'
  AND EXISTS (SELECT 1 FROM lab.shipment s WHERE s.order_id = o.order_id AND s.delivered_at IS NOT NULL)""")

ex(id="E3.6", level=3, title="Cross-tenant referrals", tags="self-join · data-quality find",
   prompt="Users whose referrer belongs to a **different tenant**. This is a multi-tenancy integrity leak, not a feature.",
   out="`user_id, referrer_id`",
   trap="Alias the same table twice (`u`, `r`) and name the join direction aloud. Then: which constraint would have prevented this? (A composite FK `(tenant_id, referred_by) → (tenant_id, user_id)`.)",
   key="""SELECT u.user_id, r.user_id AS referrer_id
FROM lab.app_user u JOIN lab.app_user r ON r.user_id = u.referred_by
WHERE r.tenant_id <> u.tenant_id""")

ex(id="E3.7", level=3, title="One-star counts including zeros", tags="LEFT JOIN · filter in ON · empty groups",
   prompt="For **every** product of tenant 1 (all of them), the number of 1-star reviews it has — 0 where none.",
   out="`product_id, one_star`",
   trap="`LEFT JOIN review r … WHERE r.rating = 1` deletes the zero rows (the WHERE re-filters the NULL-extended rows). Put the predicate in `ON`, or use `count(*) FILTER`. `count(r.review_id)`, not `count(*)`.",
   key="""SELECT p.product_id, count(r.review_id) AS one_star
FROM lab.product p LEFT JOIN lab.review r ON r.product_id = p.product_id AND r.rating = 1
WHERE p.tenant_id = 1 GROUP BY p.product_id""")

ex(id="E3.8", level=3, title="Who ordered vs who reviewed (Q1 2025)", tags="FULL OUTER JOIN · reconciliation",
   prompt="For 2025 Q1 (Jan–Mar UTC): every user who placed **or** reviewed, with two booleans — did they order, did they review.",
   out="`user_id, ordered, reviewed`",
   trap="`COALESCE` the two join keys; a FULL JOIN yields NULL on the missing side. Pre-aggregate each side to one row per user *before* joining.",
   key="""WITH o AS (SELECT DISTINCT user_id FROM lab.customer_order WHERE placed_at >= '2025-01-01' AND placed_at < '2025-04-01'),
     r AS (SELECT DISTINCT user_id FROM lab.review WHERE created_at >= '2025-01-01' AND created_at < '2025-04-01')
SELECT coalesce(o.user_id, r.user_id) AS user_id, o.user_id IS NOT NULL AS ordered, r.user_id IS NOT NULL AS reviewed
FROM o FULL JOIN r ON r.user_id = o.user_id""")

ex(id="E3.9", level=3, title="Deletions per month with zero-fill", tags="calendar spine · generate_series · LEFT JOIN",
   prompt="For every month from 2024-05 through 2025-06 (inclusive, 14 rows), the number of users deleted (`deleted_at`) in that month — including months with zero.",
   out="`month, n_deleted`",
   trap="Group the fact table alone and empty months vanish. Generate the spine first (`generate_series`), then LEFT JOIN facts onto it.",
   key="""SELECT m::date AS month, count(u.user_id) AS n_deleted
FROM generate_series('2024-05-01'::date, '2025-06-01'::date, interval '1 month') m
LEFT JOIN lab.app_user u ON date_trunc('month', u.deleted_at) = m
GROUP BY m""")

ex(id="E3.10", level=3, title="Duplicate-safe reviewers per product", tags="multiplicity · DISTINCT vs GROUP BY",
   prompt="Per product: distinct reviewers and total reviews, only products where those two numbers differ.",
   out="`product_id, n_reviewers, n_reviews`",
   trap="A user may review the same product several times in this seed (see E9.4). `count(*)` ≠ `count(DISTINCT user_id)` exactly there.",
   key="""SELECT product_id, count(DISTINCT user_id) AS n_reviewers, count(*) AS n_reviews
FROM lab.review GROUP BY product_id HAVING count(DISTINCT user_id) <> count(*)""")

# ---------------------------------------------------------------- LEVEL 4 : subqueries, CTEs, set ops
ex(id="E4.1", level=4, title="Above-average spenders", tags="scalar subquery · CTE",
   prompt="Users whose total fulfilled spend is strictly greater than the average spend **across users who spent anything** (exclude users with no fulfilled orders from the average).",
   out="`user_id, spend_minor`",
   trap="What is the denominator? Users with zero orders shift the average if you `LEFT JOIN` them in. Write down which population you average over.",
   key="""WITH s AS (SELECT user_id, sum(total_minor) AS spend_minor FROM lab.customer_order WHERE status = 'fulfilled' GROUP BY user_id)
SELECT user_id, spend_minor FROM s WHERE spend_minor > (SELECT avg(spend_minor) FROM s)""")

ex(id="E4.2", level=4, title="Latest review rating per product", tags="correlated subquery · DISTINCT ON",
   prompt="For each product that has reviews: the rating of its most recent review (newest `created_at`; ties → highest `review_id`).",
   out="`product_id, rating`",
   trap="`max(created_at)` alone does not give you the rating from that row. Use a correlated subquery, `DISTINCT ON`, or a window (E5.4) — then prove they agree.",
   key="""SELECT DISTINCT ON (product_id) product_id, rating
FROM lab.review ORDER BY product_id, created_at DESC, review_id DESC""")

ex(id="E4.3", level=4, title="Both fulfilled and refunded", tags="EXISTS · INTERSECT",
   prompt="Users who have at least one fulfilled order **and** at least one refunded order.",
   out="`user_id`",
   trap="Two `EXISTS` clauses (or `INTERSECT`). A single `JOIN` with `status IN ('fulfilled','refunded')` finds users with *either*.",
   key="""SELECT user_id FROM lab.customer_order WHERE status = 'fulfilled'
INTERSECT
SELECT user_id FROM lab.customer_order WHERE status = 'refunded'""")

ex(id="E4.4", level=4, title="Reviewed but never bought", tags="EXCEPT · NOT EXISTS · set semantics",
   prompt="Distinct `(user_id, product_id)` pairs where the user reviewed the product but has **no** order line for it (in any of their orders, any status).",
   out="`user_id, product_id`",
   trap="`EXCEPT` removes duplicates and needs identical column lists; `EXCEPT ALL` is the bag version. Solve with both `EXCEPT` and `NOT EXISTS`.",
   key="""SELECT user_id, product_id FROM lab.review
EXCEPT
SELECT o.user_id, l.product_id FROM lab.customer_order o JOIN lab.order_line l USING (order_id)""")

ex(id="E4.5", level=4, title="Net revenue per tenant without double counting", tags="CTE · pre-aggregation · fan-out",
   prompt="Per tenant: GMV of fulfilled and refunded orders placed in 2025 (`sum(total_minor)`), sum of **succeeded refund** payments on those orders, and net = gmv − refunds.",
   out="`tenant_id, gmv_minor, refunded_minor, net_minor`",
   trap="orders → payments is 1:N. Joining orders to payments and summing `total_minor` counts each order once per payment row. Aggregate each side **separately in CTEs**, then join on the key.",
   key="""WITH g AS (
  SELECT tenant_id, sum(total_minor) AS gmv_minor FROM lab.customer_order
  WHERE status IN ('fulfilled','refunded') AND placed_at >= '2025-01-01' AND placed_at < '2026-01-01' GROUP BY tenant_id),
r AS (
  SELECT o.tenant_id, sum(p.amount_minor) AS refunded_minor
  FROM lab.payment p JOIN lab.customer_order o USING (order_id)
  WHERE p.kind = 'refund' AND p.status = 'succeeded' AND o.status IN ('fulfilled','refunded')
    AND o.placed_at >= '2025-01-01' AND o.placed_at < '2026-01-01' GROUP BY o.tenant_id)
SELECT g.tenant_id, g.gmv_minor, coalesce(r.refunded_minor, 0) AS refunded_minor,
       g.gmv_minor - coalesce(r.refunded_minor, 0) AS net_minor
FROM g LEFT JOIN r USING (tenant_id)""")

ex(id="E4.6", level=4, title="Strictly the priciest in its category", tags="ALL · empty-set trap",
   prompt="Products strictly more expensive than every *other* product in the same category. Uncategorised products (NULL category) are excluded.",
   out="`product_id`",
   trap="`x > ALL (empty set)` is TRUE. For a NULL category the peer set is empty, so every uncategorised product qualifies unless you exclude them explicitly. Also: ties give no winner.",
   key="""SELECT p.product_id FROM lab.product p
WHERE p.category_id IS NOT NULL
  AND p.price_minor > ALL (SELECT q.price_minor FROM lab.product q
                           WHERE q.category_id = p.category_id AND q.product_id <> p.product_id)""")

ex(id="E4.7", level=4, title="Latest order per user (tenant 3)", tags="LATERAL · top-1 per group",
   prompt="For each user of tenant 3 who has orders: their most recent order (`placed_at DESC`, tie → higher `order_id`).",
   out="`user_id, order_id, placed_at`",
   trap="`LATERAL` runs the subquery once per outer row and can reference it — the SQL for-each loop. Missing index on `(user_id, placed_at)` makes it a seq scan per user (E12.1).",
   key="""SELECT u.user_id, o.order_id, o.placed_at
FROM lab.app_user u
CROSS JOIN LATERAL (SELECT order_id, placed_at FROM lab.customer_order c WHERE c.user_id = u.user_id
                    ORDER BY placed_at DESC, order_id DESC LIMIT 1) o
WHERE u.tenant_id = 3""")

ex(id="E4.8", level=4, title="Relational division: bought all three", tags="division · GROUP BY / HAVING · double NOT EXISTS",
   prompt="Users who have ordered **all** of products 1, 6 and 11 (any status).",
   out="`user_id`",
   trap="Division has two standard forms: `HAVING count(DISTINCT product_id) = 3` (fast, needs the count) and double `NOT EXISTS` (works for a *set stored in a table*). Write both.",
   key="""SELECT o.user_id FROM lab.customer_order o JOIN lab.order_line l USING (order_id)
WHERE l.product_id IN (1, 6, 11)
GROUP BY o.user_id HAVING count(DISTINCT l.product_id) = 3""")
