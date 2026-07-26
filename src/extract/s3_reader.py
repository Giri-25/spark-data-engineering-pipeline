from configs.config import RAW_DATA_PATH
from src.utils.logger import logger


def read_json_from_s3(spark):

    logger.info("Reading JSON from S3")

    df = (
        spark.read
        .option("multiline", "true")
        .json(RAW_DATA_PATH)
    )

    logger.info(f"Records loaded: {df.count()}")

    return df