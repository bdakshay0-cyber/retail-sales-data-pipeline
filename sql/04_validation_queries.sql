SELECT COUNT(*) AS customer_count
FROM Customers;

SELECT COUNT(*) AS product_count
FROM Products;

SELECT COUNT(*) AS store_count
FROM Stores;

SELECT COUNT(*) AS sales_count
FROM Sales;

SELECT
    COUNT(*) AS audit_rows
FROM PipelineAudit;

SELECT TOP 20 *
FROM PipelineAudit
ORDER BY CreatedDate DESC;
