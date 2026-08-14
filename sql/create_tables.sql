/*
========================================================
Retail Sales Data Pipeline
Database: RetailSalesDB

Purpose:
Create source/transaction tables for the retail
sales analytics project.
========================================================
*/

-- =====================================================
-- 1. Customers
-- =====================================================

CREATE TABLE Customers
(
    customer_id VARCHAR(20) NOT NULL,
    customer_name VARCHAR(100) NOT NULL,
    gender VARCHAR(10),
    age INT,
    city VARCHAR(100),
    state VARCHAR(50),

    CONSTRAINT PK_Customers
        PRIMARY KEY (customer_id)
);


-- =====================================================
-- 2. Products
-- =====================================================

CREATE TABLE Products
(
    product_id VARCHAR(20) NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(100),
    subcategory VARCHAR(100),
    unit_price DECIMAL(18,2) NOT NULL,

    CONSTRAINT PK_Products
        PRIMARY KEY (product_id)
);


-- =====================================================
-- 3. Stores
-- =====================================================

CREATE TABLE Stores
(
    store_id VARCHAR(20) NOT NULL,
    store_name VARCHAR(100) NOT NULL,
    city VARCHAR(100),
    state VARCHAR(50),
    region VARCHAR(50),

    CONSTRAINT PK_Stores
        PRIMARY KEY (store_id)
);


-- =====================================================
-- 4. Sales
-- =====================================================

CREATE TABLE Sales
(
    sales_id BIGINT NOT NULL,
    order_date DATE NOT NULL,
    customer_id VARCHAR(20) NOT NULL,
    product_id VARCHAR(20) NOT NULL,
    store_id VARCHAR(20) NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(18,2) NOT NULL,
    discount DECIMAL(5,2) NOT NULL,

    CONSTRAINT PK_Sales
        PRIMARY KEY (sales_id),

    CONSTRAINT FK_Sales_Customers
        FOREIGN KEY (customer_id)
        REFERENCES Customers(customer_id),

    CONSTRAINT FK_Sales_Products
        FOREIGN KEY (product_id)
        REFERENCES Products(product_id),

    CONSTRAINT FK_Sales_Stores
        FOREIGN KEY (store_id)
        REFERENCES Stores(store_id)
);
