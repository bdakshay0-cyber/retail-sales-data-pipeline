# ADF Pipelines

## PL_Generic_Load

Reusable parameterised ingestion pipeline.

Typical parameters:

- p_SourceFile
- p_DestinationTable

Purpose:

- Reuse one ingestion design for multiple retail datasets
- Reduce duplicated ADF logic
- Support scalable source-to-target loading
