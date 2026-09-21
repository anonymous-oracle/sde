\set sku 1
BEGIN;
WITH d AS (UPDATE tx.inv SET on_hand = on_hand - 1 WHERE sku = :sku AND on_hand > 0 RETURNING sku)
INSERT INTO tx.sale (sku) SELECT sku FROM d;
COMMIT;
