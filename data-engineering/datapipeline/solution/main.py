import os
import logging
import pandas as pd
from helpers import read_csv_into_dataframe, validate_dataframe_columns

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Define pipeline constants
SOURCE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'source-data'))
RESULTS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'results'))
RACES_FILENAME = "races.csv"
RESULTS_FILENAME = "results.csv"


def run_pipeline():
    # Read source CSV files into a Pandas DataFrame
    races_path = os.path.join(SOURCE_DIR, RACES_FILENAME)
    races_df = read_csv_into_dataframe(races_path)

    results_path = os.path.join(SOURCE_DIR, RESULTS_FILENAME)
    results_df = read_csv_into_dataframe(results_path)

    logger.info(f"Loaded {len(races_df)} races and {len(results_df)} results")

    # Validate the DataFrame to ensure that all required columns are present
    validate_dataframe_columns(races_df, {"raceId", "year", "round", "name", "date", "time"}, RACES_FILENAME)
    validate_dataframe_columns(results_df, {"resultId", "raceId", "driverId", "position", "fastestLapTime"}, RESULTS_FILENAME)

    # Format races data
    races_df["time"] = races_df["time"].fillna("00:00:00")
    races_df['Race Datetime'] = pd.to_datetime(races_df['date'] + ' ' + races_df['time'])
    races_df['Race Datetime'] = races_df['Race Datetime'].dt.strftime('%Y-%m-%dT%H:%M:%S.000')
    
    logger.info(f"Processed races data")

    # Filter results DataFrame for race winners
    results_df = results_df[results_df["position"] == 1]

    logger.info(f"Processed results data")

    # Combine DataFrames
    merged_df = races_df.merge(results_df[["raceId", "driverId", "fastestLapTime"]], how="left", on="raceId")
   
    logger.info(f"Merged races and results DataFrames")

    # Rename the key columns
    merged_df = merged_df.rename(columns={
        "name": "Race Name",
        "round": "Race Round",
        "driverId": "Race Winning driverId",
        "fastestLapTime": "Race Fastest Lap"
    })

    # Convert numerical columns to the correct data type
    merged_df["Race Round"] = merged_df["Race Round"].astype(int)
    merged_df["Race Winning driverId"] = merged_df["Race Winning driverId"].astype('Int64') 

    # Save data in JSON format with a separate file for each year
    for year, group_df in merged_df.groupby("year"):
        group_df = group_df[["Race Name", "Race Round", "Race Datetime", "Race Winning driverId", "Race Fastest Lap"]]
        filepath = os.path.join(RESULTS_DIR, f"stats_{year}.json")
        group_df.to_json(filepath, orient="records")

        logger.info(f"Saved {len(group_df)} records for {year}")


if __name__ == "__main__":
    try:
        run_pipeline()
        logger.info("Pipeline ran successfully")
    except Exception as e:
        logger.exception(f"Pipeline failed with exception:")
