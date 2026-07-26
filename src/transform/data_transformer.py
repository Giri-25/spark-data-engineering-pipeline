from pyspark.sql.functions import col, year, to_date
from src.utils.logger import logger


def transform_data(df):

    logger.info("Starting data transformation")

    df = (
        df
        .withColumnRenamed("Miles_per_Gallon", "mpg")
        .withColumnRenamed("Horsepower", "horsepower")
        .withColumnRenamed("Weight_in_lbs", "weight")
        .withColumnRenamed("Acceleration", "acceleration")
        .withColumnRenamed("Displacement", "displacement")
        .withColumnRenamed("Cylinders", "cylinders")
        .withColumnRenamed("Origin", "origin")
        .withColumnRenamed("Name", "car_name")
    )

    df = df.withColumn("Year", to_date(col("Year")))

    df = df.withColumn("manufacture_year", year(col("Year")))

    logger.info("Data transformation completed")

    return df