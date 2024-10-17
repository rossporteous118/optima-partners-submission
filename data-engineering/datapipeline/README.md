# Data Pipeline Assignment

## Background
Optima has been hired by a motorsport analytics Youtube channel who are looking to do rapid analysis of Formula 1 for their viewers. The company wants to have some automated data pipelines in place to perform automated transformation of incoming datasets immediately following races.

## Objective
- Develop a data pipeline that produces a JSON that has the same structure as below.
- Each element in the list should be for one race from the `races.csv` file.
- You should produce one file per year available in the source data.
- Your JSONs should be called `stats_{year}.json` for each year and be placed in the `results` folder. 
  - For example for 2024, the file should be called `stats_2024.json`.

```
  [
	  {
		  "Race Name": "Race Name here",
		  "Race Round": Race Number here,
		  "Race Datetime": "Race Datetime here in ISO8601 format",
		  "Race Winning driverId": "Race Datetime here in RFC3339 format",
		  "Race Fastest Lap": "Fastest Lap TIme here in ISO8601 format"
	  },
	  ...
  ]
```

- In `races.csv`, the `date` and `time` column are the date and time of the race.
- In `races.csv`, all dates and times are in UTC
- If the time is not available in `races.csv`, use `00:00:00`
- In `results.csv` the winning driver is determined as the one who finished in position 1 for that race
- If the JSON value for a key is always a number, represent it as such rather than a string

## Stretch goals
- Include unit tests for all functions
- While this assignmment does not require you to deploy to a cloud provider, the solution would eventually require this. Add some notes to your documentation about the tools you might use to deploy this pipeline to a cloud provider of your choice and what kind of considerations you'd need to make in doing so.


# Assignment notes
- This is a fictional assignment and has no bearing on any future or previous work related to Optima
- You may choose to use any packages or tools you wish to complete the assignment, but the solution must be built using Python
- Your solution should be built inside the `solution` folder
- Your solution should contain a `main.py` python file that allows the reviewer to run the code
- Include clear documentation for how to run the pipeline from a python terminal in a `README.md` file
- You should not use any extra source data apart from that inside the `source-data` folder
- Your code should adhere to Python best practices and should be clear for a reviewer to read
- Clearly indicate if any stretch requirements have been undertaken
- All output files should be placed in the `results` folder in your branch when merging, the folder structure is up to you

# Evaluation Criteria
Code Quality: Organisation, readability, and adherence to best practices.  
Functionality: Correctness and completeness of the core requirements.  
Scalability & Performance: Ability to handle larger data volumes or more complex operations.  
Bonus Features: Successful implementation of the stretch requirements.  
Testing: Coverage and effectiveness of test cases.  
Documentation: Clarity and usefulness of the API documentation and README file.  
