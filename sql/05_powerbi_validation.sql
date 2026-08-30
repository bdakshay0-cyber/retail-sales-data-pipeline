SELECT
    SUM(gross_sales) AS total_sales,
    COUNT(DISTINCT sales_id) AS total_orders,
    SUM(quantity) AS units_sold,
    COUNT(DISTINCT customer_id) AS total_customers
FROM gold.FactSales;

# ============================================================
# Category
# ============================================================

SELECT
    p.category,
    SUM(f.gross_sales) AS total_sales
FROM gold.FactSales f
JOIN gold.DimProduct p
    ON f.product_id = p.product_id
GROUP BY p.category
ORDER BY total_sales DESC;

# ============================================================
# Store
# ============================================================

SELECT
    s.store_name,
    SUM(f.gross_sales) AS total_sales
FROM gold.FactSales f
JOIN gold.DimStore s
    ON f.store_id = s.store_id
GROUP BY s.store_name
ORDER BY total_sales DESC;

# ============================================================
# Customer
# ============================================================

SELECT
    customer_id,
    SUM(gross_sales) AS total_sales
FROM gold.FactSales
GROUP BY customer_id
ORDER BY total_sales DESC;

