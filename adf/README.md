Azure Data Factory – Parameterized Pipeline Design

Project overview

This Azure Data Factory implementation uses a reusable parameterized pipeline named PL_Generic_Load to load retail CSV files from Azure Data Lake Storage into Azure SQL Database.

Instead of creating separate pipelines for Customers, Products, Stores, and Sales, one generic pipeline is reused by passing different parameter values.

Pipeline

Pipeline Name: PL_Generic_Load

The pipeline performs the following workflow:

Set pipeline start time.
Copy data from Azure Data Lake Storage.
Load data into the destination Azure SQL table.
Execute audit logging on success or failure.
Pipeline parameters

Parameter

Type

Purpose

p_SourceFile

String

Name of the source CSV file

p_DestinationTable

String

Destination Azure SQL table name

Example default values used during development:

Parameter

Example

p_SourceFile

customers.csv

p_DestinationTable

Customers

Dynamic expressions

The pipeline uses parameters to dynamically identify the source file and destination table.

Source file

@pipeline().parameters.p_SourceFile

Destination table

@pipeline().parameters.p_DestinationTable

These expressions allow the same pipeline to process multiple retail datasets without hard-coded values.

Reusability

The parameterized design allows the same pipeline to load different files such as:

customers.csv → Customers
products.csv → Products
stores.csv → Stores
sales.csv → Sales
Only the parameter values change; the pipeline logic remains the same.

Benefits of this design

Reusable ETL pipeline
Reduced duplicate development
Easier maintenance
Consistent audit logging
Scalable for additional source files and tables
Related resources

Pipeline JSON: pipelines/PL_Generic_Load.json
ARM deployment templates: arm_template/
Dataset definitions: datasets/
