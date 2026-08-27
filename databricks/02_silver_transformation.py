# ============================================================
# Example imports
# ============================================================


from pyspark.sql.functions import (
    col,
    trim,
    upper,
    lower,
    initcap,
    to_date,
    round,
    when
)

# ============================================================
# Load Bronze
# ============================================================

customers_df = spark.read.format("delta").load(
    f"{BRONZE_BASE_PATH}/customers"
)

products_df = spark.read.format("delta").load(
    f"{BRONZE_BASE_PATH}/products"
)

stores_df = spark.read.format("delta").load(
    f"{BRONZE_BASE_PATH}/stores"
)

sales_df = spark.read.format("delta").load(
    f"{BRONZE_BASE_PATH}/sales"
)

# ============================================================
# Customers transformations
# ============================================================

customers_silver = (
    customers_df
    .dropDuplicates(["customer_id"])
    .withColumn("customer_id", trim(col("customer_id")))
    .withColumn("customer_name", initcap(trim(col("customer_name"))))
)

# ============================================================
# If city exists
# ============================================================

customers_silver = customers_silver.withColumn(
    "city",
    initcap(trim(col("city")))
)

# ============================================================
# If state exists
# ============================================================

customers_silver = customers_silver.withColumn(
    "state",
    upper(trim(col("state")))
)





# ============================================================
# Product cleansing
# ============================================================

products_silver = (
    products_df
    .dropDuplicates(["product_id"])
    .withColumn("product_id", trim(col("product_id")))
    .withColumn("product_name", initcap(trim(col("product_name"))))
    .withColumn("category", initcap(trim(col("category"))))
)


# ============================================================
# If price exists
# ============================================================

products_silver = products_silver.withColumn(
    "unit_price",
    round(col("unit_price").cast("double"), 2)
)



# ============================================================
# Store cleansing
# ============================================================

stores_silver = (
    stores_df
    .dropDuplicates(["store_id"])
    .withColumn("store_id", trim(col("store_id")))
    .withColumn("store_name", initcap(trim(col("store_name"))))
)

# ============================================================
# If applicable
# ============================================================

stores_silver = (
    stores_silver
    .withColumn("city", initcap(trim(col("city"))))
    .withColumn("state", upper(trim(col("state"))))
)



# ============================================================
# Sales cleansing
# ============================================================

sales_silver = (
    sales_df
    .dropDuplicates(["sales_id"])
    .withColumn("sales_id", trim(col("sales_id")))
    .withColumn("customer_id", trim(col("customer_id")))
    .withColumn("product_id", trim(col("product_id")))
    .withColumn("store_id", trim(col("store_id")))
    .withColumn("order_date", to_date(col("order_date")))
    .withColumn("quantity", col("quantity").cast("integer"))
    .withColumn("unit_price", col("unit_price").cast("double"))
)

# ============================================================
# Remove invalid quantities
# ============================================================

sales_silver = sales_silver.filter(
    col("quantity") > 0
)

# ============================================================
# Remove missing keys
# ============================================================

sales_silver = sales_silver.filter(
    col("sales_id").isNotNull() &
    col("customer_id").isNotNull() &
    col("product_id").isNotNull() &
    col("store_id").isNotNull()
)

# ============================================================
# Calculate sales amount
# ============================================================

sales_silver = sales_silver.withColumn(
    "gross_sales",
    round(
        col("quantity") * col("unit_price"),
        2
    )
)

# ============================================================
# Calculate discount
# ============================================================

sales_silver = sales_silver.withColumn(
    "net_sales",
    round(
        col("gross_sales") - col("discount"),
        2
    )
)



# ============================================================
# Write Silver Delta tables
# ============================================================

(
    customers_silver.write
    .format("delta")
    .mode("overwrite")
    .save(f"{SILVER_BASE_PATH}/customers")
)

(
    products_silver.write
    .format("delta")
    .mode("overwrite")
    .save(f"{SILVER_BASE_PATH}/products")
)

(
    stores_silver.write
    .format("delta")
    .mode("overwrite")
    .save(f"{SILVER_BASE_PATH}/stores")
)

(
    sales_silver.write
    .format("delta")
    .mode("overwrite")
    .save(f"{SILVER_BASE_PATH}/sales")
)


