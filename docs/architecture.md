# Solution Architecture

Source CSV Files
        |
        v
Azure Data Lake Storage Gen2
        |
        v
Azure Data Factory
        |
        v
Bronze Delta Layer
        |
        v
Databricks Silver Transformations
        |
        v
Gold Dimensional Model
        |
        +---- FactSales
        +---- DimCustomer
        +---- DimProduct
        +---- DimStore
        +---- DimDate
        |
        v
Power BI Semantic Model
        |
        v
Retail Sales Dashboard
