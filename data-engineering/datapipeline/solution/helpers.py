import os
import pandas as pd


def read_csv_into_dataframe(filepath: str) -> pd.DataFrame:
    """
    Reads a CSV file from the given filepath into a Pandas DataFrame.

    :param filepath: The path to the CSV file.
    :return: A Pandas DataFrame containing the data from the CSV file.
    :raises RuntimeError: If the file does not exist or cannot be read.
    """
    if not os.path.isfile(filepath):
        raise RuntimeError(f"File does not exist: {filepath}")

    try:
        return pd.read_csv(filepath)
    except Exception as e:
        raise RuntimeError(f"Failed to read file: {e}")


def validate_dataframe_columns(df: pd.DataFrame, required_cols: set, filename: str = "CSV file") -> None:
    """
    Validates that all required columns are present in the DataFrame.
    
    :param df: The DataFrame to validate.
    :param required_cols: The set of required columns.
    :param filename (optional): The name of the source file (used in error messages).
    :raises RuntimeError: If required columns are missing
    """
    missing = required_cols - set(df.columns)
    if missing:
        raise RuntimeError(f"{filename} is missing required columns: {missing}")