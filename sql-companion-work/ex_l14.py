EX = []
def ex(**kw):
    kw.setdefault("ordered", False)
    EX.append(kw)

INJECT = """CREATE SCHEMA audit;
CREATE TABLE audit.o  AS SELECT * FROM lab.customer_order;
CREATE TABLE audit.l  AS SELECT * FROM lab.order_line;
CREATE TABLE audit.p  AS SELECT * FROM lab.payment;
CREATE TABLE audit.st AS SELECT * FROM lab.stock;
CREATE TABLE audit.sh AS SELECT * FROM lab.shipment;
UPDATE audit.o SET total_minor = total_minor + 1 WHERE order_id IN (111, 2222, 3333);
INSERT INTO audit.l VALUES (999999, 1, 1, 1, 500);
DELETE FROM audit.p WHERE kind = 'charge' AND status = 'succeeded' AND order_id IN (12, 13);
UPDATE audit.p SET amount_minor = amount_minor * 3 WHERE kind = 'refund' AND order_id IN (18, 38);
UPDATE audit.st SET reserved = on_hand + 1 WHERE product_id IN (7, 8);
UPDATE audit.o SET idempotency_key = 'idem-DUP' WHERE order_id IN
  (SELECT order_id FROM audit.o WHERE tenant_id = (SELECT tenant_id FROM audit.o WHERE order_id = 2) AND idempotency_key IS NOT NULL ORDER BY order_id LIMIT 2);
UPDATE audit.sh SET delivered_at = shipped_at - interval '1 hour' WHERE shipment_id IN (10, 20);
DELETE FROM audit.sh WHERE order_id IN (SELECT order_id FROM audit.o WHERE status = 'fulfilled' ORDER BY order_id LIMIT 2);"""

AUD = [
 ("C1.1", "Order total ≠ sum of its lines", "`order_id`",
  "SELECT o.order_id FROM {o} o JOIN (SELECT order_id, sum(qty::bigint * unit_price_minor) AS s FROM {l} GROUP BY order_id) x USING (order_id) WHERE o.total_minor <> x.s",
  "Orders **with no lines** would slip through an inner join — is that a separate invariant? (yes: add it if you consider 'empty order' illegal)."),
 ("C1.2", "Order lines with no order (orphans)", "`order_id, line_no`",
  "SELECT l.order_id, l.line_no FROM {l} l WHERE NOT EXISTS (SELECT 1 FROM {o} o WHERE o.order_id = l.order_id)",
  "The real schema has an FK, so this can't happen there — this audit is for *imported* or FK-less (warehouse) data."),
 ("C1.3", "Paid/fulfilled/refunded order with no succeeded charge", "`order_id`",
  "SELECT o.order_id FROM {o} o WHERE o.status IN ('paid','fulfilled','refunded') AND NOT EXISTS (SELECT 1 FROM {p} p WHERE p.order_id = o.order_id AND p.kind = 'charge' AND p.status = 'succeeded')",
  "A *failed* charge followed by a succeeded one is legal (every 15th order). Test the anti-join on `status = 'succeeded'`, not on 'has any charge'."),
 ("C1.4", "Refunds exceed charges", "`order_id`",
  "SELECT order_id FROM {p} GROUP BY order_id HAVING coalesce(sum(amount_minor) FILTER (WHERE kind='refund' AND status='succeeded'),0) > coalesce(sum(amount_minor) FILTER (WHERE kind='charge' AND status='succeeded'),0)",
  "Aggregate the payments table **alone** (one grain), never join it to lines first."),
 ("C1.5", "Reserved stock above on-hand", "`product_id`",
  "SELECT product_id FROM {st} WHERE reserved > on_hand",
  "The real table forbids this with a CHECK; `CREATE TABLE AS` copies data, not constraints — a classic way audit copies lose their guard rails."),
 ("C1.6", "Duplicate idempotency keys within a tenant", "`tenant_id, idempotency_key, n`",
  "SELECT tenant_id, idempotency_key, count(*) AS n FROM {o} WHERE idempotency_key IS NOT NULL GROUP BY 1, 2 HAVING count(*) > 1",
  "NULL keys are legitimately repeated (a UNIQUE index allows many NULLs). Exclude them explicitly."),
 ("C1.7", "Delivered before shipped", "`shipment_id`",
  "SELECT shipment_id FROM {sh} WHERE delivered_at < shipped_at",
  "NULL `delivered_at` compares UNKNOWN → correctly excluded."),
 ("C1.8", "Fulfilled order with no shipment", "`order_id`",
  "SELECT o.order_id FROM {o} o WHERE o.status = 'fulfilled' AND NOT EXISTS (SELECT 1 FROM {sh} s WHERE s.order_id = o.order_id)",
  "Anti-join again. Contrast with E3.5 (semi-join)."),
]
M = dict(o="audit.o", l="audit.l", p="audit.p", st="audit.st", sh="audit.sh")
for i, t, out, q, trap in AUD:
    ex(id=i, level=14, title=t, tags="audit invariant · anti-join / aggregate · data quality",
       prompt=f"On the fault-injected copies in schema `audit` (Appendix B.6): find every violation of the invariant *{t.lower()}*. Also run it against the clean `lab.*` tables — it must return **0 rows** there.",
       out=out, trap=trap, setup=INJECT, key=q.format(**M), baseline=q.format(o="lab.customer_order", l="lab.order_line", p="lab.payment", st="lab.stock", sh="lab.shipment"))

ex(id="C2", level=14, title="Cash-basis monthly revenue report", tags="capstone · payments · accrual vs cash",
   prompt="Per tenant and **payment** month (UTC, by `payment.created_at`): sum of **succeeded charges**, sum of **succeeded refunds**, and net = charges − refunds. Failed and pending payments never count. Then write two sentences reconciling this *cash* report with the *accrual* report of E4.5 (orders by placement date).",
   out="`tenant_id, month, charged_minor, refunded_minor, net_minor`",
   trap="A refund posted five days after an order can land in the next month — cash vs accrual differences are **timing**, not error. Aggregate `payment` on its own (no join to lines/orders except to get `tenant_id`). Money never leaves integer minor units.",
   key="""SELECT o.tenant_id, date_trunc('month', p.created_at)::date AS month,
       coalesce(sum(p.amount_minor) FILTER (WHERE p.kind = 'charge' AND p.status = 'succeeded'), 0) AS charged_minor,
       coalesce(sum(p.amount_minor) FILTER (WHERE p.kind = 'refund' AND p.status = 'succeeded'), 0) AS refunded_minor,
       coalesce(sum(p.amount_minor) FILTER (WHERE p.kind = 'charge' AND p.status = 'succeeded'), 0)
     - coalesce(sum(p.amount_minor) FILTER (WHERE p.kind = 'refund' AND p.status = 'succeeded'), 0) AS net_minor
FROM lab.payment p JOIN lab.customer_order o USING (order_id)
GROUP BY 1, 2""")

ex(id="C4", level=14, title="Explain and fix the slow query", tags="capstone · performance · correlated subquery → join",
   prompt="""For every identified user who ever made a `purchase` event: the number of `page_view` events in the 24 hours **before their first purchase**. The baseline query (Appendix B.7) uses three correlated subqueries per user and takes ~1.5 s on this seed. Deliverable: (1) `EXPLAIN (ANALYZE)` of the baseline with your written diagnosis, (2) a rewrite that returns the **identical fingerprint** in under 50 ms without adding an index, (3) a second fix that keeps the baseline text and adds an index — name it.""",
   out="`user_id, views_24h`",
   trap="Fingerprint first, speed second: a fast wrong answer is worthless. The rewrite computes each user's first-purchase time **once** (CTE, `min … GROUP BY user_id`) and joins; the index alternative is `(user_id, event_type, occurred_at)` or `(user_id, occurred_at)`.",
   key="""WITH fp AS (SELECT user_id, min(occurred_at) AS t FROM lab.event WHERE event_type = 'purchase' AND user_id IS NOT NULL GROUP BY user_id)
SELECT fp.user_id, count(e.event_id) AS views_24h
FROM fp LEFT JOIN lab.event e
  ON e.user_id = fp.user_id AND e.event_type = 'page_view' AND e.occurred_at < fp.t AND e.occurred_at >= fp.t - interval '24 hours'
GROUP BY fp.user_id""")
