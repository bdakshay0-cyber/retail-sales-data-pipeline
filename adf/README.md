# Azure Data Factory

ADF is responsible for orchestration and source ingestion.

## Main Pipelines

### PL_Generic_Load

Loads:

- customers.csv
- products.csv
- stores.csv
- sales.csv

from ADLS Gen2 into the target processing layer.

Reusable parameterised pipeline.

Parameters:

- p_SourceFile
- p_DestinationTable

Purpose:

Allows multiple retail datasets to use the same ingestion pattern.

## Audit and Error Handling

Pipeline execution details are written to the PipelineAudit table.

Captured fields include:

- pipeline name
- pipeline run ID
- status
- rows processed
- start time
- end time
- error message

Success and failure paths invoke InsertPipelineAudit.
