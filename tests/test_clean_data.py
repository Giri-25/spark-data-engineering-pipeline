import pytest
from pyspark.sql import SparkSession

from src.transform.clean_data import clean_data


@pytest.fixture(scope="session")
def spark():
    spark = (
        SparkSession.builder
        .master("local[*]")
        .appName("PySparkCleanDataTests")
        .getOrCreate()
    )

    yield spark

    spark.stop()


def test_clean_data(spark):

    data = [
        (18.0, 130.0, "chevrolet"),
        (18.0, 130.0, "chevrolet"),   # Duplicate
        (None, 150.0, "ford"),        # MPG is null
        (20.0, None, "toyota"),       # Horsepower is null
        (22.0, 120.0, None),          # Name is null
    ]

    columns = [
        "Miles_per_Gallon",
        "Horsepower",
        "Name",
    ]

    df = spark.createDataFrame(data, columns)

    cleaned_df = clean_data(df)

    # Duplicate removed + null Name removed
    assert cleaned_df.count() == 3

    rows = cleaned_df.collect()

    mpg_values = [row["Miles_per_Gallon"] for row in rows]
    hp_values = [row["Horsepower"] for row in rows]
    names = [row["Name"] for row in rows]

    # Null values replaced with 0
    assert 0 in mpg_values
    assert 0 in hp_values

    # No null names remain
    assert None not in names