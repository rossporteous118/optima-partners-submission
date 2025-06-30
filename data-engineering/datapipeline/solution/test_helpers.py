import pytest
import os 
import pandas as pd
from helpers import read_csv_into_dataframe, validate_dataframe_columns

class TestReadCsvIntoDataFrame:
    def test_read_csv_into_dataframe_file_not_found(self):
        """
        'read_csv_into_dataframe' should raise a FileNotFoundError if the file does not exist.
        """
        fake_file = "fake_file.csv"
        
        with pytest.raises(FileNotFoundError):
            read_csv_into_dataframe(fake_file)


class TestValidateDataFrameColumns:
    def test_validate_dataframe_columns_all_present(self):
        """
        'validate_dataframe_columns' should not raise an exception if all required columns are present.
        """
        df = pd.DataFrame(columns=["raceId", "year", "round", "name", "date", "time"])
        required_cols = {"raceId", "year", "round", "name", "date", "time"}

        validate_dataframe_columns(df, required_cols)


    def test_validate_dataframe_columns_missing_columns(self):
        """
        'validate_dataframe_columns' should raise a runtime error if required columns are missing.
        """
        df = pd.DataFrame(columns=["raceId", "year", "round"])
        required_cols = {"raceId", "year", "round", "name", "date", "time"}

        with pytest.raises(RuntimeError) as exc_info:
            validate_dataframe_columns(df, required_cols)
        
        missing = {"name", "date", "time"}
        expected_message = f"CSV file is missing required columns: {missing}"
        assert str(exc_info.value) == expected_message
