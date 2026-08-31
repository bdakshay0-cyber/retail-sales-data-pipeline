# Data Dictionary

## FactSales

| Column | Description |
|---|---|
| sales_id | Unique transaction identifier |
| customer_id | Customer dimension key |
| product_id | Product dimension key |
| store_id | Store dimension key |
| order_date | Transaction date |
| quantity | Quantity sold |
| unit_price | Product selling price |
| gross_sales | Transaction sales value |

## DimProduct

| Column | Description |
|---|---|
| product_id | Unique product identifier |
| product_name | Product name |
| category | Product category |
| unit_price | Standard unit price |

## DimCustomer

| Column | Description |
|---|---|
| customer_id | Unique customer identifier |
| customer_name | Customer name |

## DimStore

| Column | Description |
|---|---|
| store_id | Unique store identifier |
| store_name | Store name |

## DimDate

| Column | Description |
|---|---|
| date | Calendar date |
| day | Day of month |
| day_name | Name of day |
| day_type | Weekday/weekend classification |
| month | Numeric month |
| month_name | Month name |
| quarter | Quarter number |
| quarter_name | Quarter label |
| week_of_year | ISO/calendar week number |
| year | Calendar year |
