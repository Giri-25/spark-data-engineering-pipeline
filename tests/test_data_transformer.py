import pytest
from pyspark.sql import SparkSession

from src.transform.data_transformer import transform_data


@pytest.fixture(scope="session")
def spark():
    spark = (
        SparkSession.builder
        .master("local[*]")
        .appName("PySparkTransformTests")
        .getOrCreate()
    )

    yield spark

    spark.stop()


def test_transform_data(spark):

    data = [
        (
            18.0,
            8,
            307.0,
            130.0,
            12.0,
            "chevrolet chevelle malibu",
            "USA",
            3504,
            "1970-01-01",
        )
    ]

    columns = [
        "Miles_per_Gallon",
        "Cylinders",
        "Displacement",
        "Horsepower",
        "Acceleration",
        "Name",
        "Origin",
        "Weight_in_lbs",
        "Year",
    ]

    df = spark.createDataFrame(data, columns)

    transformed_df = transform_data(df)

    expected_columns = [
        "mpg",
        "cylinders",
        "displacement",
        "horsepower",
        "acceleration",
        "car_name",
        "origin",
        "weight",
        "Year",
        "manufacture_year",
    ]

    assert transformed_df.columns == expected_columns

    row = transformed_df.first()

    assert row.mpg == 18.0
    assert row.cylinders == 8
    assert row.displacement == 307.0
    assert row.horsepower == 130.0
    assert row.acceleration == 12.0
    assert row.car_name == "chevrolet chevelle malibu"
    assert row.origin == "USA"
    assert row.weight == 3504
    assert row.manufacture_year == 1970