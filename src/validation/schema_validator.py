from src.validation.schema import EXPECTED_COLUMNS
from src.utils.logger import logger


def validate_schema(df):
    logger.info("Validating input schema...")

    actual_columns = df.columns

    missing_columns = [
        column for column in EXPECTED_COLUMNS
        if column not in actual_columns
    ]

    extra_columns = [
        column for column in actual_columns
        if column not in EXPECTED_COLUMNS
    ]

    if missing_columns:
        logger.error(f"Missing columns: {missing_columns}")
        raise ValueError(
            f"Schema validation failed. Missing columns: {missing_columns}"
        )

    if extra_columns:
        logger.warning(f"Extra columns found: {extra_columns}")

    logger.info("Schema validation passed.")

    return True