#Import the library needed to analyze the hospital data.
import pandas as pd
#Load the hospital CSV files into Pandas DataFrames.
def load_data():
     patients = pd.read_csv("data/patients.csv") 
     visits = pd.read_csv("data/visits.csv") 
     departments = pd.read_csv("data/departments.csv")


     return patients, visits, departments
#Calculate the total number of visits.
def total_visits(visits):
     return len(visits)
def average_waiting_time(visits):
     return visits["Waiting_Time_Minutes"].mean()
def busiest_department(visits):
     return visits["Department"].value_counts().idxmax()
#Define the main function and start the program.
def main():
     patients, visits, departments = load_data()

#Python
     print("Patients:", len(patients))
     print("Visits:", len(visits))

# Calculate and display the total number of visits.
     total = total_visits(visits)
     print("Total visits:", total)

# Count the number of visits in each department.
     department_visits = visits["Department"].value_counts()
     print(department_visits)

# Calculate the average waiting time.
     average_wait = visits["Waiting_Time_Minutes"].mean()
     print("Average waiting time:", round(average_wait, 2), "minutes")
     max_wait = visits["Waiting_Time_Minutes"].max()
     print("Maximum waiting time:", max_wait, "minutes")
     median_wait = visits["Waiting_Time_Minutes"].median()
     print("Median waiting time:", median_wait, "minutes")

# Calculate the average waiting time for each department.
     department_wait = visits.groupby("Department")["Waiting_Time_Minutes"].mean()
     print(department_wait.round(2))
     department_max_wait = visits.groupby("Department")["Waiting_Time_Minutes"].max()
     print("Maximum waiting time by department:")
     print(department_max_wait)
     department_median_wait = visits.groupby("Department")["Waiting_Time_Minutes"].median()
     print("Median waiting time by department:")
     print(department_median_wait)
     # Calculate total staff count.
     total_staff = departments["Staff_Count"].sum()
     print("Total staff:", total_staff)
     visits_per_staff = len(visits) / total_staff
     print("Visits per staff member:", round(visits_per_staff, 2))
     longest_wait_department = department_wait.idxmax()
     print("Department with longest average wait:", longest_wait_department)
     shortest_wait_department = department_wait.idxmin()
     print("Department with shortest average wait:", shortest_wait_department)
     wait_difference = department_wait.max() - department_wait.min()
     print("Waiting time difference:", round(wait_difference, 2), "minutes")


# Find the busiest department.
     busiest_department = department_visits.idxmax()
     print("Busiest department:", busiest_department)

# Find the busiest arrival hour.
     visits["Arrival_Hour"] = pd.to_datetime(visits["Arrival_Time"]).dt.hour
     hourly_visits = visits["Arrival_Hour"].value_counts().sort_index()
     print("Visits by hour:")
     print(hourly_visits)

# Find the busiest arrival hour.
     busiest_hour = hourly_visits.idxmax()
     print("Busiest hour:", busiest_hour)


# Check for missing values in the hospital data.print("Missing values:")
     print("Missing values:")
     print(patients.isnull().sum())
     print(visits.isnull().sum())
     print(departments.isnull().sum())
if __name__ == "__main__":
     main()
