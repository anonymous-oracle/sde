-- Northstar SQL Lab — deterministic seed v1. No random(): every value is a pure function of its ids.
SET search_path = lab;
SET TIME ZONE 'UTC';

INSERT INTO tenant
SELECT t, 'tenant-' || t,
       (ARRAY['free','pro','enterprise','pro','free'])[t],
       timestamptz '2024-01-01' + t * interval '1 day'
FROM generate_series(1,5) t;

INSERT INTO app_user (user_id, tenant_id, email, display_name, country, referred_by, created_at, deleted_at)
SELECT i,
       (i-1) % 5 + 1,
       'user' || i || '@t' || ((i-1) % 5 + 1) || '.example.com',
       'User ' || i,
       CASE WHEN i % 11 = 0 THEN NULL ELSE (ARRAY['US','GB','DE','IN','BR','JP','FR'])[i % 7 + 1] END,
       CASE WHEN i <= 50 OR i % 4 = 0 THEN NULL ELSE ((i::bigint * 2654435761) % 4294967296) % (i - 1) + 1 END,
       timestamptz '2024-02-01' + (i % 300) * interval '1 day' + (i % 24) * interval '1 hour',
       CASE WHEN i % 97 = 0
            THEN timestamptz '2024-02-01' + (i % 300) * interval '1 day' + interval '100 days' END
FROM generate_series(1,2000) i;

INSERT INTO category (category_id, tenant_id, parent_id, name)
SELECT t*100 + k, t,
       CASE WHEN k = 1 THEN NULL
            WHEN k BETWEEN 2 AND 4 THEN t*100 + 1
            ELSE t*100 + 2 + (k-5)/2 END,
       'cat-' || t || '-' || k
FROM generate_series(1,5) t, generate_series(1,10) k;

INSERT INTO product (product_id, tenant_id, sku, name, category_id, price_minor, currency, attrs, created_at, discontinued_at)
SELECT i,
       (i-1) % 5 + 1,
       'SKU-' || lpad(i::text, 4, '0'),
       'Product ' || i,
       CASE WHEN i % 13 = 0 THEN NULL ELSE ((i-1) % 5 + 1) * 100 + 5 + (i % 6) END,
       500 + (i * 137) % 9500,
       CASE WHEN (i-1) % 5 + 1 = 4 THEN 'EUR' ELSE 'USD' END,
       jsonb_build_object('color', (ARRAY['red','green','blue','black'])[i % 4 + 1],
                          'weight_g', 100 + i % 900)
         || CASE WHEN i % 3 = 0 THEN jsonb_build_object('tags', jsonb_build_array('eco', 'gift')) ELSE '{}'::jsonb END,
       timestamptz '2024-01-15' + (i % 60) * interval '1 day',
       CASE WHEN i % 17 = 0 THEN timestamptz '2025-06-01' END
FROM generate_series(1,500) i;

INSERT INTO product_price_history (product_id, valid_from, price_minor)
SELECT p.product_id, p.created_at + h.d * interval '1 day', p.price_minor + h.delta
FROM product p
CROSS JOIN (VALUES (0, 200), (200, 100), (400, 0)) AS h(d, delta);

INSERT INTO stock (product_id, on_hand, reserved, updated_at)
SELECT i, (i * 31) % 200, ((i * 31) % 200) / 10, timestamptz '2025-12-31 12:00:00'
FROM generate_series(1,500) i;

-- 20,000 orders; user drawn from a skewed (power-law-ish) deterministic hash: user 1 is hot, users 1801-2000 never order;
-- tenant follows the user so the composite FK holds
INSERT INTO customer_order (order_id, tenant_id, user_id, status, placed_at, currency, total_minor, idempotency_key)
SELECT i,
       (u - 1) % 5 + 1,
       u,
       CASE WHEN i % 20 <= 11 THEN 'fulfilled'
            WHEN i % 20 <= 14 THEN 'paid'
            WHEN i % 20 <= 16 THEN 'cancelled'
            WHEN i % 20 = 17  THEN 'created'
            ELSE 'refunded' END,
       timestamptz '2025-01-01' + ((i * 37) % 365) * interval '1 day' + ((i * 7919) % 86400) * interval '1 second',
       CASE WHEN (u - 1) % 5 + 1 = 4 THEN 'EUR' ELSE 'USD' END,
       0,
       CASE WHEN i % 2 = 0 THEN 'idem-' || i END
FROM (SELECT i, 1 + floor(1800 * power(((i * 7919) % 10007)::numeric / 10007, 1.5))::int AS u FROM generate_series(1,20000) i) s;

INSERT INTO order_line (order_id, line_no, product_id, qty, unit_price_minor)
SELECT o.order_id, n, o.tenant_id + 5 * (((o.order_id::bigint * 2654435761 + n * 40503) % 4294967296) % 100), 1 + (o.order_id + n) % 3, 0
FROM customer_order o
JOIN LATERAL generate_series(1, 1 + o.order_id % 4) n ON true;

UPDATE order_line l SET unit_price_minor = p.price_minor FROM product p WHERE p.product_id = l.product_id;

UPDATE customer_order o SET total_minor = s.t
FROM (SELECT order_id, sum(qty::bigint * unit_price_minor) AS t FROM order_line GROUP BY order_id) s
WHERE s.order_id = o.order_id;

INSERT INTO payment (payment_id, order_id, kind, amount_minor, status, created_at)
SELECT row_number() OVER (ORDER BY order_id, created_at, kind), order_id, kind, amount_minor, status, created_at
FROM (
  -- failed first attempt for every 15th paid-ish order
  SELECT order_id, 'charge' AS kind, total_minor AS amount_minor, 'failed' AS status, placed_at + interval '30 seconds' AS created_at
  FROM customer_order WHERE order_id % 15 = 0 AND status IN ('paid','fulfilled','refunded')
  UNION ALL
  SELECT order_id, 'charge', total_minor, 'succeeded', placed_at + interval '1 minute'
  FROM customer_order WHERE status IN ('paid','fulfilled','refunded')
  UNION ALL
  SELECT order_id, 'charge', total_minor, 'pending', placed_at + interval '10 seconds'
  FROM customer_order WHERE status = 'created'
  UNION ALL
  SELECT order_id, 'charge', total_minor, 'failed', placed_at + interval '20 seconds'
  FROM customer_order WHERE status = 'cancelled' AND order_id % 2 = 0
  UNION ALL
  SELECT order_id, 'refund', CASE WHEN order_id % 2 = 0 THEN total_minor ELSE total_minor / 2 END, 'succeeded', placed_at + interval '5 days'
  FROM customer_order WHERE status = 'refunded'
) x;

INSERT INTO shipment (shipment_id, order_id, carrier, shipped_at, delivered_at)
SELECT row_number() OVER (ORDER BY o.order_id, n), o.order_id,
       (ARRAY['UPS','DHL','FedEx'])[(o.order_id + n) % 3 + 1],
       o.placed_at + interval '1 day' + n * interval '2 hours',
       CASE WHEN o.order_id % 7 = 0 THEN NULL
            ELSE o.placed_at + interval '1 day' + n * interval '2 hours' + (2 + o.order_id % 5 + (o.order_id + n) % 3 - 1) * interval '1 day' END
FROM customer_order o
JOIN LATERAL generate_series(1, CASE WHEN o.order_id % 9 = 0 THEN 2 ELSE 1 END) n ON true
WHERE o.status = 'fulfilled';

INSERT INTO review (review_id, product_id, user_id, rating, body, created_at)
SELECT i, p, t + 5 * ((i * 31) % 400),
       CASE (i * 7 + i / 5) % 10 WHEN 0 THEN 1 WHEN 1 THEN 2 WHEN 2 THEN 3 WHEN 3 THEN 3
            WHEN 4 THEN 4 WHEN 5 THEN 4 WHEN 6 THEN 4 ELSE 5 END,
       CASE WHEN i % 5 = 0 THEN NULL WHEN i % 11 = 0 THEN '' ELSE 'Review text ' || i END,
       timestamptz '2025-02-01' + (i % 300) * interval '1 day'
FROM (SELECT i, pp AS p, (pp - 1) % 5 + 1 AS t
      FROM (SELECT i, 1 + floor(500 * power(((i * 7919) % 6007)::numeric / 6007, 1.3))::int AS pp FROM generate_series(1,6000) i) q) s;

-- double-submit bug: every 15th review was posted a second time a day later (400 duplicate (product,user) pairs)
INSERT INTO review (review_id, product_id, user_id, rating, body, created_at)
SELECT review_id + 6000, product_id, user_id, rating, body, created_at + interval '1 day'
FROM review WHERE review_id % 15 = 0;

-- 60,000 events = 7,500 blocks of 8. A block is one visit by one user on one day; every 3rd block has a 40-min gap at k=4.
INSERT INTO event (event_id, tenant_id, user_id, event_type, occurred_at, payload)
SELECT i,
       CASE WHEN b % 6 = 0 THEN b % 5 + 1 ELSE (u - 1) % 5 + 1 END,
       CASE WHEN b % 6 = 0 THEN NULL ELSE u END,
       CASE k WHEN 2 THEN 'search'
              WHEN 4 THEN CASE WHEN b % 2 = 0 THEN 'add_to_cart' ELSE 'page_view' END
              WHEN 5 THEN CASE WHEN b % 4 = 0 THEN 'checkout_start' ELSE 'page_view' END
              WHEN 6 THEN CASE WHEN b % 8 = 0 THEN 'purchase' ELSE 'page_view' END
              ELSE 'page_view' END,
       timestamptz '2025-01-01' + ((b * 37) % 365) * interval '1 day' + ((b * 7919) % 70000) * interval '1 second'
         + (k * 120 + CASE WHEN b % 3 = 0 AND k >= 4 THEN 2400 ELSE 0 END) * interval '1 second',
       jsonb_build_object('path', '/p/' || (1 + (b * 13 + k) % 500), 'ms', (b * k * 53) % 3000)
         || CASE WHEN k = 2 THEN jsonb_build_object('q', (ARRAY['shoe','lamp','desk','mug'])[b % 4 + 1]) ELSE '{}'::jsonb END
FROM (SELECT i, (i - 1) / 8 AS b, (i - 1) % 8 AS k,
             (((i - 1) / 8) * 7919) % 2000 + 1 AS u
      FROM generate_series(1,60000) i) s;

-- messy staging rows for the cleaning ladder
INSERT INTO stg_import VALUES
 (1,  'Ann@Example.com ',   '2025-03-01',   '12.50'),
 (2,  'ann@example.com',    '03/01/2025',   '$1,200.00'),
 (3,  'bob@example.com',    '1 Mar 2025',   '12,50'),
 (4,  '',                   '2025-03-02',   ' 7 '),
 (5,  NULL,                 '2025-03-02',   '0'),
 (6,  'carol@example.com',  'not a date',   'abc'),
 (7,  'CAROL@EXAMPLE.COM',  '2025-03-03',   '3.999'),
 (8,  'dave@example.com',   '',             NULL),
 (9,  'dave@example.com',   '2025-13-40',   '-5.00'),
 (10, ' erin@example.com',  '2025-03-04',   '1e3'),
 (11, 'frank@example',      '2025-03-05',   '15'),
 (12, 'gina@example.com',   '2025-02-29',   '9.99'),
 (13, 'gina@example.com',   '2025-03-06',   '9.99'),
 (14, 'hal@example.com',    '2025-03-06T10:15:00Z', '100'),
 (15, 'ivy@example.com',    '  2025-03-07  ', '1,000.5');

-- gaps-and-islands fodder: which days each of the first 200 users logged in (120 days from 2025-03-01)
CREATE TABLE login_day (
  user_id bigint NOT NULL REFERENCES app_user,
  day     date   NOT NULL,
  PRIMARY KEY (user_id, day)
);
INSERT INTO login_day (user_id, day)
SELECT u, date '2025-03-01' + d
FROM generate_series(1,200) u, generate_series(0,119) d
WHERE (d + u) % 9 < 6 AND d % 23 <> u % 23;

ANALYZE;

-- Lab kit: order-insensitive and order-sensitive result fingerprints (row count : 8 hex chars of md5)
CREATE FUNCTION chk(q text) RETURNS text LANGUAGE plpgsql AS $f$
DECLARE r text;
BEGIN
  EXECUTE format('SELECT count(*) || '':'' || left(md5(coalesce(string_agg(t::text, ''|'' ORDER BY t::text), '''')), 8) FROM (%s) t', q) INTO r;
  RETURN r;
END $f$;

CREATE FUNCTION chk_o(q text) RETURNS text LANGUAGE plpgsql AS $f$
DECLARE r text;
BEGIN
  EXECUTE format('SELECT count(*) || '':'' || left(md5(coalesce(string_agg(t::text, ''|'' ORDER BY rn), '''')), 8) FROM (SELECT row_number() OVER () AS rn, x.* FROM (%s) x) t', q) INTO r;
  RETURN r;
END $f$;

CREATE FUNCTION try(stmt text) RETURNS boolean LANGUAGE plpgsql AS $f$
BEGIN EXECUTE stmt; RETURN true; EXCEPTION WHEN others THEN RETURN false; END $f$;

CREATE SCHEMA IF NOT EXISTS work;
