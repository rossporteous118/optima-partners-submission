# Data Pipeline Assignment

## Background
Optima has been hired by a motorsport analytics Youtube channel who are looking to do rapid analysis of Formula 1 for their viewers. The company wants to have some automated data pipelines in place to perform automated transformation of incoming datasets immediately following races.

## Objective
Develop a data pipeline (or several) using Python that will perform the following tasks:
- For all races and sprint races, the following data is required. Unless otherwise stated, the client is expecting one set of files per race rather than one large file with all data included:
  - Results of the race as a CSV file, including the following columns:
    - Race Name, Race Year, Driver name, Constructor name, Car number, Number of points awarded, Starting position, Finishing position, Total laps driven in the race, Drivers fastest lap
  - Race lap status as a JSON file, structured like so: 
  ```
    {
        "Race Name": "Race Name here",
        "Race Year": "Race Year here",
        "Fastest Lap": {
            "Driver Name": "Driver Name Here",
            "Car Number": "Car Number here",
            "Constructor Name": "Constructor Name Here",
            "Lap Time": "Lap Time Here"
        },
        "Slowest Lap": {
            "Driver Name": "Driver Name Here",
            "Car Number": "Car Number here",
            "Constructor Name": "Constructor Name Here",
            "Lap Time": "Lap Time Here"
        },
        "Average Lap Time In ms": 1234556
    }
  ```
  - Highlight any statuses are that not `Finished` for the race and sprint races as a JSON which includes the following keys:
    - Race Name, Race Year, Driver Name, Car Number, Constructor Name, Status
- For any future races that have not happened yet, data should not be processed
- All output data should be arranged in an appropriately named folder structure
- Any NULL values or values indicating it is a NULL value should be replaced with blank values
- It is expected this pipeline will be run multiple times when no new data is available, your pipeline should account for this and not waste resources




## Stretch goals;
- Include unit tests for all functions
- While this assignmment does not require you to deploy to a cloud provider, the solution would eventually require this. Add some notes to your documentation about the tools you might use to deploy this pipeline to a cloud provider of your choice and what kind of considerations you'd need to make in doing so.
- For all races and sprint races, add the following data:
  - Constructor standings as a CSV file, ordered by their points descending, including the following columns:
    - Race Name, Race Year, Constructor name, Constructor points, Constructor ranking, Number of wins
  - Qualifying results as a CSV file, including the following columns:
    - Race Name, Race Year, Driver Name, Car Number, Constructor Name, Qualified position, Qualifying 1 time, Qualifying 2 time, Qualifying 3 time
  - Pit stop summary of the race as a CSV file, including the following columns:
    - Race Name, Race Year, Driver Name, Constructor name, Car Number, Stop Number, Lap Number, Time in Pits in seconds




# Assignment notes
- This is a fictional assignment and has no bearing on any future or previous work related to Optima
- You may choose to use any packages or tools you wish to complete the assignment, but the solution must be built using Python
- Your solution should be built inside the `solution` folder
- Your solution should contain a `main.py` python file that allows the reviewer to run the code
- Include clear documentation for how to run the pipeline using a python terminal
- You should not use any extra source data apart from that inside the `source-data` folder
- Your code should adhere to Python best practices and should be clear for a reviewer to read
- Clearly indicate if any stretch requirements have been undertaken
- All output files should be placed in the `results` folder in your branch when merging, the folder structure is up to you



## Note on Source Data for this assignment
For more information on column types and documentation around the datasets, please refer to the dataset in [Kaggle](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020) .

# Evaluation Criteria
Code Quality: Organisation, readability, and adherence to best practices.  
Functionality: Correctness and completeness of the core requirements.  
Scalability & Performance: Ability to handle larger data volumes or more complex operations.  
Bonus Features: Successful implementation of the stretch requirements.  
Testing: Coverage and effectiveness of test cases.  
Documentation: Clarity and usefulness of the API documentation and README file.  

# Questions
Please reach out if you have questions or anything is unclear