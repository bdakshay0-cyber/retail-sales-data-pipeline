from pyspark.sql.functions import current_timestamp, input_file_name

# ============================================================
# Retail Sales Project
# Bronze Layer Ingestion
# ============================================================

RAW_BASE_PATH = "abfss://raw@<storage-account>.dfs.core.windows.net"

BRONZE_BASE_PATH = "abfss://bronze@<storage-account>.dfs.core.windows.net"


def load_to_bronze(source_file, destination_path):
    """
    Reads CSV from ADLS raw layer,
    adds ingestion metadata,
    writes data in Delta format.
    """

    df = (
        spark.read
        .option("header", "true")
        .option("inferSchema", "true")
        .csv(source_file)
    )

    bronze_df = (
        df
        .withColumn("ingestion_timestamp", current_timestamp())
        .withColumn("source_file", input_file_name())
    )

    (
        bronze_df.write
        .format("delta")
        .mode("overwrite")
        .option("overwriteSchema", "true")
        .save(destination_path)
    )

    return bronze_df
