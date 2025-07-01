# Solution README

## Project Setup

1. Clone the repository

```bash
git clone https://github.com/rossporteous118/optima-partners-submission.git
```

2. Create and activate a virtual environment to isolate dependencies (optional)

```bash
python3 -m venv venv

source venv/bin/activate    # MacOS / Linux

venv\Scripts\activate       # Windows
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run main.py from the project's root directory

```bash
python3 data-engineering/datapipeline/solution/main.py
```

5. Run the project tests from the project's root directory

```bash
pytest data-engineering/datapipeline/solution/test_helpers.py
```

## Stretch Goals

### Unit tests

I have created two custom auxiliary functions for use in my Python pipeline that have been placed in the 'helpers.py' file within the solution folder. I have also created some basic tests to ensure that these functions perform as expected. The tests for these functions can be found within the 'test_helpers.py' file.

### Cloud deployment

When deploying this pipeline to a cloud environment there are several important considerations that would need to be made.

One consideration would be around the volume of data we expect to be processed within this pipeline. In this case, the volume of data is relatively small. Due to this, we could use a serverless compute cloud service such as AWS Lambda to execute our Python scripts and process our data. This approach would remain extremely cheap and would be able to comfortably handle the relatively small amount of data being processed. However, if we expected the volume of data to increase significantly then a distributed computing framework may need to be employed to handle the increased data volume. In this case, the Python pipeline may need to be modified to use PySpark instead of Pandas as PySpark is designed to efficiently process large datasets across distributed machines. This approach would also incur greater costs as more compute resources would be required and additonal tools such as AWS Glue may be needed to manage the more complex compute infrastructure.

Another consideration is how we intend to store our data. At the moment, our pipeline simply saves JSON files to a local folder which would not be suitable for a production environment. One good option here would be to utilise an object store such as AWS S3 to store our output JSON files. A cloud object store would be a good option here as they have very high scalability and low costs without enforcing a strict schema. These features lend themselves well to the semi-structured JSON files we are working with as we can save large quantities of data without worrying about conforming to a rigid schema.

Finally, we should also consider how we will monitor the status of our pipeline. The pipeline script I have created includes a basic logging system which will log key events throughout the pipeline to the console by default. If we deploy this pipeline on a cloud environment, it would be good to integrate these logs with a more complete monitoring tool such as Amazon CloudWatch which would allow us to continue to observe the status logs from our pipeline when it is in production. In addition to this, we may want to set up a notification system to alert us of any issues in the event our pipeline encounters a problem. These notifications could be triggered within the try / except block of the Python pipeline.
