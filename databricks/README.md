# Databricks Transformation Layer

This folder contains the PySpark code used to implement the Retail Sales Medallion architecture.

## 01_bronze_ingestion.py

Purpose:

- Read source CSV files from the raw layer
- Preserve source data with minimal transformation
- Add ingestion metadata
- Write Bronze Delta datasets

Sources:

- customers.csv
- products.csv
- stores.csv
- sales.csv

## 02_silver_transformation.py

Purpose:

- Remove duplicate records
- Clean business keys
- Standardise text attributes
- Convert data types
- Handle invalid or missing values
- Validate transaction data
- Prepare trusted Silver datasets

## 03_gold_star_schema.py

Purpose:

Create the analytical Gold dimensional model:

- FactSales
- DimCustomer
- DimProduct
- DimStore
- DimDate

## 04_gold_aggregations.py

Purpose:

Create reusable analytical aggregations for:

- Monthly sales
- Product/category performance
- Store performance
- Customer performance

The Gold layer is consumed by Power BI.
