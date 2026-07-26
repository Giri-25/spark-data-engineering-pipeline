from src.utils.logger import logger


def clean_data(df):

    logger.info("Cleaning data")

    before = df.count()

    df = df.dropDuplicates()

    df = df.dropna(subset=["Name"])

    df = df.fillna({"Miles_per_Gallon": 0})

    df = df.fillna({"Horsepower": 0})

    after = df.count()

    logger.info(f"Rows before cleaning: {before}")
    logger.info(f"Rows after cleaning: {after}")

    return df