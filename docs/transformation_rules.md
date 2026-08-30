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

## Silver Layer

### Customers
- Removed duplicate customer IDs
- Trimmed customer identifiers
- Standardised customer names
- Standardised city/state values

### Products
- Removed duplicate product IDs
- Standardised product names
- Standardised categories
- Cast price to numeric datatype

### Stores
- Removed duplicate store IDs
- Standardised store names
- Standardised geographical attributes

### Sales
- Removed duplicate sales IDs
- Converted order_date to Date
- Converted quantity to Integer
- Converted prices to numeric values
- Removed invalid/null business keys
- Removed non-positive quantities
- Calculated/validated gross sales
