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


1. Pipeline Overview

File: 01_pipeline_overview.PNG

Shows the complete PL_Generic_Load Azure Data Factory pipeline, including:

Pipeline start-time initialization
Copy activity
Success dependency
Failure dependency
Audit logging activities
2. Generic Pipeline

File: 02_generic_pipeline.PNG

Shows the reusable generic ingestion pipeline used to load retail datasets.

The pipeline is designed to use parameters rather than creating separate ingestion logic for every source file.

3. Pipeline Parameters

File: 03_pipeline_parameters.PNG

Shows the parameters used by PL_Generic_Load:

p_SourceFile
p_DestinationTable

These parameters allow the same pipeline to load different source files into their corresponding Azure SQL tables.

4. Audit Success Path

File: 04_audit_success_path.PNG

Shows the success dependency from Copy_Retail_Data to Audit_Success.

After a successful copy operation, the pipeline calls the InsertPipelineAudit stored procedure to record information such as:

Pipeline name
Pipeline run ID
Start time
End time
Status
Rows processed
Error message
5. Audit Failure Path

File: 05_audit_failure_path.PNG

Shows the failure dependency from Copy_Retail_Data to Audit_Failure.

If the copy activity fails, the pipeline executes the failure audit activity so pipeline failures can be recorded and investigated.

6. Successful Pipeline Run

File: 06_successful_pipeline_run.PNG

Shows a successfully completed execution of PL_Generic_Load.

The monitored run confirms successful execution of:

Set_Start_Time
Copy_Retail_Data
Audit_Success

This demonstrates successful end-to-end ingestion and audit logging.

Technologies Demonstrated
Azure Data Factory
Azure Data Lake Storage Gen2
Azure SQL Database
Parameterized ADF pipelines
ADF Copy Activity
Stored Procedure Activity
Pipeline variables
Dynamic content and expressions
Success and failure dependencies
Pipeline monitoring
Audit logging
