# Hospilyt

## Project Description

Hospilyt is a Python-based hospital data analysis project developed as a CS50P final project.

The project analyzes synthetic hospital data using Python and Pandas. It examines patient visits, waiting times, department activity, and hospital resources.

Hospilyt helps identify the busiest departments, compare waiting times, and provide insights into hospital operations.


## Project Files

- project.py: Contains the main program and hospital data analysis functions.
- test_project.py: Contains tests for the project’s functions using pytest.
- generate_data.py: Generates synthetic hospital data.
- requirements.txt: Lists the Python libraries required to run the project.
- data/: Contains CSV files for patients, visits, and departments.


## How to Run

1- Install the required libraries:
python -m pip install -r requirements.txt

2- Run the hospital data analysis:
python project.py

3- Run the tests:
python -m pytest test_project.py -v


## Analysis Results

Hospilyt analyzes synthetic hospital data and provides the following results:

- Total number of patients and visits.
- Number of visits in each department.
- Average, median, and maximum waiting times.
- Waiting time comparisons between departments.
- Busiest department and busiest arrival hour.
- Total hospital staff and visits per staff member.
- Missing values in the hospital datasets.

The analysis helps identify patterns in hospital activity and potential areas for operational improvement.

