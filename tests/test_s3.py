from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("TestS3")
    .config(
        "spark.jars.packages",
        "org.apache.hadoop:hadoop-aws:3.5.0"
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
        "s3.ap-south-1.amazonaws.com"
    )
    .getOrCreate()
)

# Reduce Spark logs
spark.sparkContext.setLogLevel("ERROR")

try:
    print("Reading JSON from S3...\n")

    df = (
        spark.read
        .option("multiline", "true")
        .json("s3a://girija-citi-data-pipeline-950119649378/raw/cars.json")
    )

    print("✅ Successfully connected to S3!\n")
    print(f"Total Records: {df.count()}\n")

    print("Schema:")
    df.printSchema()

    print("\nSample Data:")
    df.show(5, truncate=False)

except Exception as e:
    print("\n❌ Error:")
    print(e)

finally:
    spark.stop()