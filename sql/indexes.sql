/*
========================================================
Retail Sales Data Pipeline
Database: RetailSalesDB

Purpose:
Create indexes to improve query performance.
========================================================
*/

-- =====================================================
-- Sales order date
-- Useful for date-based reporting and filtering
-- =====================================================

CREATE INDEX IX_Sales_OrderDate
ON Sales(order_date);


-- =====================================================
-- Sales customer
-- Useful for customer-level analysis
-- =====================================================

CREATE INDEX IX_Sales_Customer
ON Sales(customer_id);


-- =====================================================
-- Sales product
-- Useful for product-level analysis
-- =====================================================

CREATE INDEX IX_Sales_Product
ON Sales(product_id);


-- =====================================================
-- Sales store
-- Useful for store-level analysis
-- =====================================================

CREATE INDEX IX_Sales_Store
ON Sales(store_id);
