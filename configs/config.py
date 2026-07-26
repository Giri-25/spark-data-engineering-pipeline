import os
from dotenv import load_dotenv

load_dotenv()

# =========================
# AWS CONFIG
# =========================

AWS_REGION = os.getenv("AWS_REGION")

S3_BUCKET = os.getenv("S3_BUCKET")

RAW_DATA_PATH = f"s3a://{S3_BUCKET}/raw/cars.json"

PROCESSED_DATA_PATH = f"s3a://{S3_BUCKET}/processed/cars_parquet"

# =========================
# POSTGRES CONFIG
# =========================

POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_TABLE = os.getenv("POSTGRES_TABLE")

# =========================
# JDBC DRIVER
# =========================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

JDBC_DRIVER = os.path.join(
    BASE_DIR,
    "drivers",
    "postgresql-42.7.7.jar"
)