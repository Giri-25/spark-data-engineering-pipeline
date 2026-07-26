from pyspark.sql.functions import col
from src.utils.logger import logger


def validate_data(df):

    logger.info("Starting data quality validation...")

    total_rows = df.count()

    duplicate_rows = total_rows - df.dropDuplicates().count()

    invalid_mpg = df.filter(col("Miles_per_Gallon") < 0).count()

    invalid_hp = df.filter(col("Horsepower") < 0).count()

    empty_names = df.filter(
        col("Name").isNull() | (col("Name") == "")
    ).count()

    logger.info(f"Total Rows          : {total_rows}")
    logger.info(f"Duplicate Rows      : {duplicate_rows}")
    logger.info(f"Invalid MPG Rows    : {invalid_mpg}")
    logger.info(f"Invalid HP Rows     : {invalid_hp}")
    logger.info(f"Empty Car Names     : {empty_names}")

    if duplicate_rows > 0:
        logger.warning("Duplicate records found.")

    if invalid_mpg > 0:
        logger.warning("Negative MPG values found.")

    if invalid_hp > 0:
        logger.warning("Negative Horsepower values found.")

    if empty_names > 0:
        logger.warning("Empty car names found.")

    logger.info("Data quality validation completed.")

    return df