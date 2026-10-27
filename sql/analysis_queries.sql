-- Smart Warehouse & Inventory Optimization
-- Example SQL queries (table name: warehouse_inventory)

-- 1. Latest stock snapshot and reorder alerts
WITH latest AS (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY warehouse, product_id ORDER BY date DESC) AS rn
  FROM warehouse_inventory
)
SELECT warehouse, product_id, product_name, stock_on_hand, reorder_point,
       CASE WHEN stock_on_hand <= reorder_point THEN 'REORDER' ELSE 'HEALTHY' END AS stock_status
FROM latest
WHERE rn = 1
ORDER BY warehouse, product_name;

-- 2. Fulfilment rate by warehouse
SELECT warehouse,
       ROUND(100.0 * SUM(units_fulfilled) / NULLIF(SUM(units_ordered), 0), 2) AS fulfilment_pct
FROM warehouse_inventory
GROUP BY warehouse
ORDER BY fulfilment_pct DESC;

-- 3. Average delivery delay by warehouse
SELECT warehouse, ROUND(AVG(delivery_delay_days), 2) AS avg_delay_days
FROM warehouse_inventory
GROUP BY warehouse
ORDER BY avg_delay_days DESC;

-- 4. Inventory value by category on the latest date
WITH latest_date AS (SELECT MAX(date) AS max_date FROM warehouse_inventory)
SELECT category, SUM(stock_on_hand * unit_cost_inr) AS inventory_value_inr
FROM warehouse_inventory
WHERE date = (SELECT max_date FROM latest_date)
GROUP BY category
ORDER BY inventory_value_inr DESC;

-- 5. Demand fulfilment gap by product
SELECT product_id, product_name,
       SUM(units_ordered) AS units_ordered,
       SUM(units_fulfilled) AS units_fulfilled,
       SUM(units_ordered - units_fulfilled) AS units_unfulfilled
FROM warehouse_inventory
GROUP BY product_id, product_name
ORDER BY units_unfulfilled DESC;
