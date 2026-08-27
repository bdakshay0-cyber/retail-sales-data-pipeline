## Bronze Layer

Purpose: Preserve source data with minimal modification.

Transformations:

- Read CSV files from ADLS Gen2 raw container
- Enabled header parsing
- Inferred source schema
- Added ingestion_timestamp
- Added source_file metadata
- Stored datasets as Delta tables
- Retained source-level records for traceability
