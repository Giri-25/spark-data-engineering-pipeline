from configs.config import (
    POSTGRES_HOST,
    POSTGRES_PORT,
    POSTGRES_DB,
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    POSTGRES_TABLE,
)

from src.utils.logger import logger


def load_to_postgres(df):

    logger.info("Loading data into PostgreSQL")

    jdbc_url = (
        f"jdbc:postgresql://{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )

    (
        df.write
        .format("jdbc")
        .option("url", jdbc_url)
        .option("dbtable", POSTGRES_TABLE)
        .option("user", POSTGRES_USER)
        .option("password", POSTGRES_PASSWORD)
        .option("driver", "org.postgresql.Driver")
        .mode("overwrite")
        .save()
    )

    logger.info("Data loaded successfully into PostgreSQL")