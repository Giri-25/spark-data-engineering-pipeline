from pyspark.sql import SparkSession

from configs.config import AWS_REGION, JDBC_DRIVER


def create_spark_session():

    spark = (
        SparkSession.builder
        .appName("Citi Data Engineering Pipeline")

        .config(
            "spark.jars.packages",
            "org.apache.hadoop:hadoop-aws:3.5.0"
        )

        .config(
            "spark.jars",
            JDBC_DRIVER
        )

        .config(
            "spark.hadoop.fs.s3a.impl",
            "org.apache.hadoop.fs.s3a.S3AFileSystem"
        )

        .config(
            "spark.hadoop.fs.s3a.aws.credentials.provider",
            "software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider"
        )

        .config(
            "spark.hadoop.fs.s3a.endpoint",
            f"s3.{AWS_REGION}.amazonaws.com"
        )

        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("ERROR")

    return spark