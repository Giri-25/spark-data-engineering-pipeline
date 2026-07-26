from src.utils.spark_session import create_spark_session
from src.extract.s3_reader import read_json_from_s3
from src.validation.schema_validator import validate_schema
from src.validation.data_validator import validate_data
from src.transform.clean_data import clean_data
from src.transform.data_transformer import transform_data
from src.load.parquet_writer import write_parquet
from src.load.postgres_loader import load_to_postgres
from src.utils.logger import logger


def main():

    logger.info("=" * 60)
    logger.info("CITI DATA ENGINEERING PIPELINE STARTED")
    logger.info("=" * 60)

    spark = create_spark_session()

    try:

        df = read_json_from_s3(spark)

        validate_schema(df)

        validate_data(df)

        df = clean_data(df)

        df = transform_data(df)

        # Save cleaned data to S3 as Parquet
        write_parquet(df)

        # Load to PostgreSQL
        load_to_postgres(df)

        logger.info("Pipeline completed successfully.")

    except Exception:

        logger.exception("Pipeline failed.")
        raise

    finally:

        spark.stop()

        logger.info("Spark Session Closed")


if __name__ == "__main__":
    main()