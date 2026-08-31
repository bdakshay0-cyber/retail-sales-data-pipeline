# Azure Data Factory Screenshots

This folder contains screenshots demonstrating the Azure Data Factory implementation used in the Retail Sales Data Engineering project.

The ADF solution provides parameterized ingestion of retail data from Azure Data Lake Storage Gen2 into Azure SQL Database, together with pipeline monitoring, audit logging, and success/failure handling.

## Pipeline Flow

The generic ingestion pipeline follows the following process:

```text
Set_Start_Time
      |
      v
Copy_Retail_Data
     / \
Success Failure
   /       \
  v         v
Audit_Success   Audit_Failure