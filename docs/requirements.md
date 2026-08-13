# Retail Sales Data Pipeline

## 1. Business Problem

A retail company receives sales data from multiple sources in CSV format.

The company currently has difficulty obtaining a centralized and reliable view of its sales performance.

Business users need to understand:

- Total sales revenue
- Number of orders
- Product performance
- Store performance
- Customer purchasing behaviour
- Regional sales performance
- Monthly sales trends

The objective is to build an automated data pipeline that collects, cleans, transforms and prepares retail sales data for business reporting.

---

## 2. Project Objective

Build an end-to-end retail sales data engineering solution using Microsoft Azure.

The solution will use:

- Azure Data Factory for data ingestion and orchestration
- Azure SQL Database for structured data storage
- Azure Databricks for data transformation and processing
- Power BI for business reporting and visualization

The final solution will provide a reliable analytical dataset that can be consumed by business users through Power BI dashboards.

---

## 3. Data Sources

The initial project will use CSV files representing retail business data.

The source datasets will include:

### Customers

Customer information including:

- Customer ID
- Customer Name
- Gender
- Age
- City
- State

### Products

Product information including:

- Product ID
- Product Name
- Category
- Subcategory
- Unit Price

### Stores

Store information including:

- Store ID
- Store Name
- City
- State
- Region

### Sales

Transaction-level sales information including:

- Sales ID
- Order Date
- Customer ID
- Product ID
- Store ID
- Quantity
- Unit Price
- Discount

---

## 4. Proposed Data Architecture

The solution will follow this architecture:

Source CSV Files
        |
        v
Azure Data Factory
        |
        v
Azure SQL Database
        |
        v
Azure Databricks
        |
        v
Bronze Layer
        |
        v
Silver Layer
        |
        v
Gold Layer
        |
        v
Power BI
        |
        v
Business Dashboard

---

## 5. Data Engineering Requirements

The pipeline should:

1. Ingest source files into the data platform.
2. Validate incoming data.
3. Store source data without losing the original information.
4. Remove duplicate records.
5. Handle missing or invalid values.
6. Validate customer, product and store relationships.
7. Calculate sales metrics.
8. Create analytical datasets.
9. Maintain pipeline execution information.
10. Provide data quality checks.

---

## 6. Azure Data Factory Requirements

Azure Data Factory will be responsible for:

- Connecting to source data
- Extracting source files
- Loading data into Azure SQL
- Orchestrating data movement
- Parameterizing pipelines
- Monitoring pipeline executions
- Handling pipeline failures
- Maintaining pipeline audit information

The pipeline should be designed to support reusable and parameterized ingestion.

---

## 7. Azure SQL Requirements

Azure SQL Database will be used for structured storage.

The database should contain tables for:

- Customers
- Products
- Stores
- Sales
- Pipeline Audit

Appropriate primary keys and indexes should be implemented.

---

## 8. Databricks Requirements

Azure Databricks will be used for data transformation and analytical processing.

The solution will implement a Medallion Architecture:

### Bronze

Raw data with minimal transformation.

### Silver

Cleaned and validated data.

Transformations will include:

- Duplicate removal
- Data type standardization
- Null handling
- Data validation
- Business rule validation
- Sales calculations

### Gold

Business-ready analytical datasets.

The Gold layer will contain:

- Fact Sales
- Customer Dimension
- Product Dimension
- Store Dimension
- Sales Summary

---

## 9. Data Quality Requirements

The pipeline should identify:

- Duplicate sales records
- Missing customer IDs
- Missing product IDs
- Missing store IDs
- Invalid quantities
- Invalid prices
- Invalid dates
- Referential integrity issues

Data quality results should be documented.

---

## 10. Data Model

The final analytical model will follow a star schema.

Fact table:

- FactSales

Dimension tables:

- DimCustomer
- DimProduct
- DimStore
- DimDate

The FactSales table will contain transactional sales information.

Dimension tables will provide descriptive information used for analysis.

---

## 11. Power BI Requirements

Power BI will provide business users with interactive dashboards.

The dashboard should provide:

### Executive Overview

- Total Revenue
- Total Orders
- Total Quantity Sold
- Average Order Value

### Product Analysis

- Revenue by Product
- Revenue by Category
- Top 10 Products
- Quantity Sold

### Store Analysis

- Revenue by Store
- Revenue by Region
- Orders by Store
- Monthly Store Performance

Users should be able to filter the dashboard by:

- Date
- Product
- Category
- Store
- Region
- Customer

---

## 12. Performance Requirements

The solution should be designed to process increasing volumes of sales data.

The project will measure:

- Number of records processed
- Pipeline execution time
- Databricks transformation time
- Data quality issues
- Processing performance

Performance results will be documented after implementation.

---

## 13. Security Requirements

The project should follow secure data engineering practices.

Credentials and secrets must not be stored in GitHub.

The solution should consider:

- Azure Key Vault
- Managed identities
- Role-based access control
- Secure database connectivity
- Environment-specific configuration

No passwords, access keys, connection strings or API keys will be committed to the repository.

---

## 14. Monitoring and Error Handling

The solution should provide visibility into pipeline execution.

The following information should be captured where practical:

- Pipeline name
- Pipeline run ID
- Start time
- End time
- Status
- Records processed
- Error message

Failed pipeline executions should be identifiable and investigated.

---

## 15. Expected Business Outcome

The completed solution should provide a centralized and reliable retail sales analytics platform.

Business users should be able to use Power BI to answer questions such as:

- How much revenue did we generate?
- Which products generate the most revenue?
- Which stores perform best?
- Which regions are growing?
- What are our monthly sales trends?
- Which products have the highest sales volume?
- How many orders do we receive?
- What is our average order value?

---

## 16. Future Enhancements

Future versions of the project may include:

- Incremental data loading
- Azure Data Lake Storage Gen2
- Microsoft Fabric
- Real-time data ingestion
- CI/CD using Azure DevOps
- Automated data quality testing
- Azure Key Vault integration
- Data lineage
- Machine learning for sales forecasting
- Customer segmentation
- AI-powered sales insights
- 
