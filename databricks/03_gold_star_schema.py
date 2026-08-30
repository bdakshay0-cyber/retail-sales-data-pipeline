# ============================================================
# Gold model contains
# FactSales
# DimCustomer
# DimProduct
# DimStore
# DimDate
# ============================================================



# ============================================================
# DimCustomer
# ============================================================

dim_customer = (
    customers_silver
    .select(
        "customer_id",
        "customer_name",
        "city",
        "state"
    )
    .dropDuplicates(["customer_id"])
)

# ============================================================
# DimProduct
# ============================================================

dim_product = (
    products_silver
    .select(
        "product_id",
        "product_name",
        "category",
        "unit_price"
    )
    .dropDuplicates(["product_id"])
)

# ============================================================
# DimStore
# ============================================================

dim_store = (
    stores_silver
    .select(
        "store_id",
        "store_name",
        "city",
        "state"
    )
    .dropDuplicates(["store_id"])
)

# ============================================================
# FactSales
# ============================================================

fact_sales = (
    sales_silver
    .select(
        "sales_id",
        "customer_id",
        "product_id",
        "store_id",
        "order_date",
        "quantity",
        "unit_price",
        "gross_sales"
    )
)

# ============================================================
# DimDate
# ============================================================

from pyspark.sql.functions import (
    explode,
    sequence,
    to_date,
    year,
    month,
    dayofmonth,
    date_format,
    quarter,
    weekofyear,
    lit
)

dim_date = (
    spark.sql("""
        SELECT explode(
            sequence(
                to_date('2026-01-01'),
                to_date('2026-12-31'),
                interval 1 day
            )
        ) AS date
    """)
    .withColumn("year", year(col("date")))
    .withColumn("month", month(col("date")))
    .withColumn("month_name", date_format(col("date"), "MMMM"))
    .withColumn("day", dayofmonth(col("date")))
    .withColumn("day_name", date_format(col("date"), "EEEE"))
    .withColumn("quarter", quarter(col("date")))
    .withColumn(
        "quarter_name",
        concat(lit("Q"), quarter(col("date")))
    )
    .withColumn("week_of_year", weekofyear(col("date")))
)

# ============================================================
# Write Gold tables
# ============================================================

(
    fact_sales.write
    .format("delta")
    .mode("overwrite")
    .saveAsTable("gold.factsales")
)

(
    dim_customer.write
    .format("delta")
    .mode("overwrite")
    .saveAsTable("gold.dimcustomer")
)

(
    dim_product.write
    .format("delta")
    .mode("overwrite")
    .saveAsTable("gold.dimproduct")
)

(
    dim_store.write
    .format("delta")
    .mode("overwrite")
    .saveAsTable("gold.dimstore")
)

(
    dim_date.write
    .format("delta")
    .mode("overwrite")
    .saveAsTable("gold.dimdate")
)
