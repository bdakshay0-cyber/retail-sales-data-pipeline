CREATE TABLE Customers (
    customer_id VARCHAR(20) PRIMARY KEY,
    customer_name VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(100)
);

CREATE TABLE Products (
    product_id VARCHAR(20) PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(100),
    unit_price DECIMAL(12,2)
);

CREATE TABLE Stores (
    store_id VARCHAR(20) PRIMARY KEY,
    store_name VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(100)
);

CREATE TABLE Sales (
    sales_id VARCHAR(30) PRIMARY KEY,
    customer_id VARCHAR(20),
    product_id VARCHAR(20),
    store_id VARCHAR(20),
    order_date DATE,
    quantity INT,
    unit_price DECIMAL(12,2),
    gross_sales DECIMAL(18,2)
);
