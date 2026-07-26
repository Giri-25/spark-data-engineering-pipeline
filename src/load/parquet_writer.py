from configs.config import PROCESSED_DATA_PATH
from src.utils.logger import logger


def write_parquet(df):

    logger.info("Writing processed data to S3 as Parquet...")

    (
        df.write
        .mode("overwrite")
        .parquet(PROCESSED_DATA_PATH)
    )

    logger.info("Parquet files written successfully.")