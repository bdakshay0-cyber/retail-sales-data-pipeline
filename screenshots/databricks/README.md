# Databricks Implementation Screenshots

This folder contains screenshots demonstrating the Databricks implementation of the Retail Sales Data Engineering project.

The Databricks notebooks implement a Medallion Architecture consisting of Bronze, Silver, and Gold layers. Raw retail data is ingested from Azure Data Lake Storage Gen2, transformed and validated using PySpark, stored as Delta tables, and prepared for analytics and Power BI reporting.

---

## 1. Bronze Layer Ingestion

**File:** ``01_bronze_ingestion.png``

This screenshot demonstrates the Bronze-layer ingestion process.

The notebook:

- Reads raw retail data from Azure Data Lake Storage Gen2.
- Uses PySpark DataFrames for ingestion.
- Stores the ingested data using Delta format.
- Creates Bronze-layer tables in the ``retail_sales.bronze`` schema.
- Validates the resulting Bronze data.

Example Bronze table:

``retail_sales.bronze.customers``

The Bronze layer preserves source-level data before business transformations are applied.

---

## 2. Silver Layer Transformation

**File:** ``02_silver_transformation.png``

This screenshot demonstrates the Silver-layer processing and validation.

Silver-layer transformations include:

- Removing duplicate records.
- Filtering invalid or missing identifiers.
- Trimming and standardizing values.
- Standardizing customer and business attributes.
- Applying data-quality transformations.
- Preparing clean transactional data for downstream analytics.
- Writing transformed data as Delta tables.

Example Silver table:

``retail_sales.silver.sales``

The screenshot also demonstrates validation of the resulting Silver sales records.

---

## 3. Gold Layer Aggregation

**File:** ``03_gold_aggregation.png``

This screenshot demonstrates the creation of business-level Gold aggregations using PySpark.

The ``SalesSummary`` aggregation groups sales information by:

- Year
- Month
- Store
- Product

The aggregation calculates business metrics including:

- Total transactions
- Total quantity sold
- Gross sales
- Discount amount
- Net sales

This produces an analytics-ready dataset suitable for reporting and dashboard development.

---

## 4. Gold Layer Tables

**File:** ``04_gold_tables.png``

This screenshot validates the Gold-layer dimensional model.

The Gold layer contains:

- ``DimCustomer``
- ``DimProduct``
- ``DimStore``
- ``FactSales``
- ``SalesSummary``

Validated record counts shown in the implementation:

| Gold Table | Record Count |
|---|---:|
| DimCustomer | 10 |
| DimProduct | 15 |
| DimStore | 8 |
| FactSales | 50,000 |
| SalesSummary | 720 |

These tables form the analytics-ready Gold layer of the Retail Sales Data Engineering project.

---

## 5. Sales Summary Output

**File:** ``05_sales_summary.png``

This screenshot demonstrates the final ``SalesSummary`` Delta table.

The table contains aggregated retail sales metrics including:

- Year
- Month
- Store ID
- Product ID
- Total transactions
- Total quantity
- Gross sales
- Discount amount
- Net sales

The ``SalesSummary`` table provides a reporting-ready dataset for downstream business intelligence and Power BI dashboards.

---

## 6. Successful Notebook Execution

**File:** ``06_notebook_success.png``

This screenshot demonstrates successful execution of the final Gold-layer notebook.

The final notebook includes validation checks covering:

- Gold table availability
- Sales and aggregation validation
- Data-quality checks
- Customer relationship validation
- Product relationship validation
- Store relationship validation
- Fact-to-dimension integrity checks

The successful execution of the final cells provides evidence that the Gold-layer processing and validation workflow completed successfully.

---

## Databricks Architecture

The Databricks implementation follows the Medallion Architecture:

Azure Data Lake Storage Gen2
|
v
Bronze Layer
Raw Delta Tables
|
v
Silver Layer
Cleaned and Standardized
Delta Tables
|
v
Gold Layer
Dimensional Data Model
|
+--> DimCustomer
+--> DimProduct
+--> DimStore
+--> FactSales
+--> SalesSummary
|
v
Power BI

## Technologies Demonstrated

- Azure Databricks
- Apache Spark
- PySpark
- Spark SQL
- Delta Lake
- Azure Data Lake Storage Gen2
- Medallion Architecture
- Bronze / Silver / Gold data layers
- Dimensional modelling
- Data cleansing and transformation
- Data-quality validation
- Business aggregation
- Power BI-ready data preparation

---

## Screenshot Summary

| Screenshot | Description |
|---|---|
| ``01_bronze_ingestion.png`` | Bronze-layer ingestion and Delta-table validation |
| ``02_silver_transformation.png`` | Silver-layer transformation and validation |
| ``03_gold_aggregation.png`` | Gold business aggregation logic and results |
| ``04_gold_tables.png`` | Gold dimensional tables and record counts |
| ``05_sales_summary.png`` | Final analytics-ready SalesSummary output |
| ``06_notebook_success.png`` | Successful final notebook execution and validation |

---

## Purpose

These screenshots provide implementation evidence for the Databricks component of the Retail Sales Data Engineering project. They demonstrate the progression of retail data from raw ingestion through cleansing and transformation to an analytics-ready dimensional model and aggregated reporting layer.
