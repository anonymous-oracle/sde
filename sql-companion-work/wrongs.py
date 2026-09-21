WRONG = {
"E1.1": ("BETWEEN with the last calendar day", """SELECT user_id, email FROM lab.app_user WHERE country IN ('GB','DE') AND created_at BETWEEN '2024-04-01' AND '2024-06-30'"""),
"E1.3": ("`<>` instead of IS DISTINCT FROM", """SELECT user_id FROM lab.app_user WHERE country <> 'US'"""),
"E2.5": ("integer division", """SELECT tenant_id, count(*) AS n_orders, count(*) FILTER (WHERE status='refunded') AS n_refunded,
 round((count(*) FILTER (WHERE status='refunded') / count(*))::numeric, 4) AS refund_rate FROM lab.customer_order GROUP BY tenant_id"""),
"E3.2": ("NOT IN over a column containing NULL", """SELECT user_id FROM lab.app_user WHERE user_id NOT IN (SELECT referred_by FROM lab.app_user)"""),
"E3.5": ("plain JOIN fans out orders with two shipments", """SELECT sum(o.total_minor) AS revenue_minor FROM lab.customer_order o JOIN lab.shipment s USING (order_id) WHERE o.status='fulfilled' AND s.delivered_at IS NOT NULL"""),
"E3.7": ("rating filter in WHERE after the LEFT JOIN", """SELECT p.product_id, count(r.review_id) AS one_star FROM lab.product p LEFT JOIN lab.review r ON r.product_id = p.product_id WHERE p.tenant_id = 1 AND r.rating = 1 GROUP BY p.product_id"""),
"E4.5": ("orders JOIN payments then SUM(total_minor)", """SELECT o.tenant_id, sum(o.total_minor) AS gmv_minor, coalesce(sum(p.amount_minor) FILTER (WHERE p.kind='refund' AND p.status='succeeded'),0) AS refunded_minor,
 sum(o.total_minor) - coalesce(sum(p.amount_minor) FILTER (WHERE p.kind='refund' AND p.status='succeeded'),0) AS net_minor
 FROM lab.customer_order o JOIN lab.payment p USING (order_id) WHERE o.status IN ('fulfilled','refunded') AND o.placed_at >= '2025-01-01' AND o.placed_at < '2026-01-01' GROUP BY o.tenant_id"""),
"E4.6": ("forgetting that ALL over an empty set is TRUE", """SELECT p.product_id FROM lab.product p WHERE p.price_minor > ALL (SELECT q.price_minor FROM lab.product q WHERE q.category_id = p.category_id AND q.product_id <> p.product_id)"""),
"E5.7": ("last_value with the default frame", """SELECT DISTINCT product_id, first_value(price_minor) OVER w AS first_price, last_value(price_minor) OVER w AS last_price, last_value(price_minor) OVER w - first_value(price_minor) OVER w AS delta
 FROM lab.product_price_history WHERE product_id BETWEEN 1 AND 20 WINDOW w AS (PARTITION BY product_id ORDER BY valid_from)"""),
"E6.4": ("plain equi-join returns all three price rows", """SELECT l.order_id, l.line_no, l.unit_price_minor, h.price_minor AS price_at_order FROM lab.order_line l JOIN lab.customer_order o USING (order_id) JOIN lab.product_price_history h ON h.product_id = l.product_id WHERE o.placed_at < '2025-01-04' AND l.unit_price_minor <> h.price_minor"""),
"E8.3": ("comparing UTC to UTC (wrong AT TIME ZONE direction)", """SELECT count(*) AS n FROM lab.customer_order WHERE (placed_at::timestamp AT TIME ZONE 'America/New_York')::date <> placed_at::date"""),
}
