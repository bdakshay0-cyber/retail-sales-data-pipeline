# ============================================================
# Monthly Sales
# ============================================================

monthly_sales = (
    fact_sales
    .groupBy(
        year("order_date").alias("year"),
        month("order_date").alias("month")
    )
    .agg(
        sum("gross_sales").alias("total_sales"),
        sum("quantity").alias("units_sold"),
        countDistinct("sales_id").alias("total_orders")
    )
)

# ============================================================
# Category Sales
# ============================================================

category_sales = (
    fact_sales.alias("f")
    .join(
        dim_product.alias("p"),
        col("f.product_id") == col("p.product_id")
    )
    .groupBy("p.category")
    .agg(
        sum("f.gross_sales").alias("total_sales"),
        sum("f.quantity").alias("units_sold"),
        countDistinct("f.sales_id").alias("total_orders")
    )
)

# ============================================================
# Store Sales
# ============================================================

store_sales = (
    fact_sales.alias("f")
    .join(
        dim_store.alias("s"),
        col("f.store_id") == col("s.store_id")
    )
    .groupBy(
        "s.store_id",
        "s.store_name"
    )
    .agg(
        sum("f.gross_sales").alias("total_sales"),
        sum("f.quantity").alias("units_sold"),
        countDistinct("f.sales_id").alias("total_orders")
    )
)

# ============================================================
# Customer Sales
# ============================================================

customer_sales = (
    fact_sales.alias("f")
    .join(
        dim_customer.alias("c"),
        col("f.customer_id") == col("c.customer_id")
    )
    .groupBy(
        "c.customer_id",
        "c.customer_name"
    )
    .agg(
        sum("f.gross_sales").alias("total_sales"),
        countDistinct("f.sales_id").alias("total_orders"),
        sum("f.quantity").alias("units_sold")
    )
)

