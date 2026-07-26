from src.utils.spark_session import create_spark_session
from src.extract.s3_reader import read_json_from_s3
from src.validation.schema_validator import validate_schema
from src.validation.data_validator import validate_data
from src.transform.clean_data import clean_data
from src.transform.data_transformer import transform_data
from src.load.parquet_writer import write_parquet
from src.load.postgres_loader import load_to_postgres
from src.utils.logger import logger
import time


def main():

    start_time = time.time()

    print("\n🚀 Starting Citi Data Engineering Pipeline...\n")

    logger.info("=" * 60)
    logger.info("CITI DATA ENGINEERING PIPELINE STARTED")
    logger.info("=" * 60)

    spark = create_spark_session()

    try:

        df = read_json_from_s3(spark)

        validate_schema(df)

        validate_data(df)

        df = clean_data(df)

        record_count = df.count()

        df = transform_data(df)

        write_parquet(df)

        load_to_postgres(df)

        execution_time = round(time.time() - start_time, 2)

        logger.info("Pipeline completed successfully.")

        print("\n" + "=" * 60)
        print("🎉 PIPELINE EXECUTED SUCCESSFULLY")
        print("=" * 60)
        print(f"Records Processed : {record_count}")
        print("Schema Validation : PASSED")
        print("Data Quality      : PASSED")
        print("Output            : S3 (Parquet)")
        print("Database          : PostgreSQL")
        print(f"Execution Time    : {execution_time} seconds")
        print("=" * 60)

    except Exception as e:

        logger.exception("Pipeline failed.")

        print("\n" + "=" * 60)
        print("❌ PIPELINE EXECUTION FAILED")
        print("=" * 60)
        print(f"Reason : {e}")
        print("Check logs/pipeline.log for details.")
        print("=" * 60)

        raise

    finally:

        spark.stop()

        logger.info("Spark Session Closed")


if __name__ == "__main__":
    main()