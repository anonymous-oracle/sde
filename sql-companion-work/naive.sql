\set sku 1
BEGIN;
SELECT on_hand AS oh FROM tx.inv WHERE sku = :sku \gset
\if :oh > 0
UPDATE tx.inv SET on_hand = :oh - 1 WHERE sku = :sku;
INSERT INTO tx.sale (sku) VALUES (:sku);
\endif
COMMIT;
