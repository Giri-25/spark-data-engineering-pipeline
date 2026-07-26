import pytest
from pyspark.sql import SparkSession

from src.validation.schema_validator import validate_schema


@pytest.fixture(scope="session")
def spark():
    spark = (
        SparkSession.builder
        .master("local[*]")
        .appName("PySparkUnitTests")
        .getOrCreate()
    )

    yield spark

    spark.stop()


def test_valid_schema(spark):
    data = [
        (
            12.0,
            8,
            307.0,
            130.0,
            18.0,
            "chevrolet chevelle malibu",
            "USA",
            3504,
            "1970-01-01",
        )
    ]

    columns = [
        "Acceleration",
        "Cylinders",
        "Displacement",
        "Horsepower",
        "Miles_per_Gallon",
        "Name",
        "Origin",
        "Weight_in_lbs",
        "Year",
    ]

    df = spark.createDataFrame(data, columns)

    assert validate_schema(df) is True


def test_invalid_schema(spark):
    data = [
        (
            18.0,
            "chevrolet chevelle malibu",
        )
    ]

    columns = [
        "Miles_per_Gallon",
        "Name",
    ]

    df = spark.createDataFrame(data, columns)

    with pytest.raises(ValueError):
        validate_schema(df)