import csv
import random
from datetime import datetime, timedelta

departments = [
    "Emergency",
    "Cardiology",
    "Pediatrics",
    "Orthopedics",
    "Internal Medicine"
]

department_info = {
    "Emergency": {"staff": 18, "resources": 10},
    "Cardiology": {"staff": 10, "resources": 6},
    "Pediatrics": {"staff": 12, "resources": 7},
    "Orthopedics": {"staff": 8, "resources": 5},
    "Internal Medicine": {"staff": 14, "resources": 8}
}

num_patients = 200

patients = []

for i in range(1, num_patients + 1):
    patient = {
        "Patient_ID": i,
        "Age": random.randint(1, 90),
        "Gender": random.choice(["Male", "Female"])
    }
    patients.append(patient)

visits = []
visit_id = 1
for patient in patients: num_visits = random.randint(1, 3)
  for _ in range(num_visits):
    department = random.choice(departments)

    visit = {
        "Visit_ID": visit_id,
        "Patient_ID": patient["Patient_ID"],
        "Department": department
    }

    visits.append(visit)
    visit_id += 1

start_date = datetime(2026, 1, 1)
for visit in visits: random_days = random.randint(0, 364) arrival_date = start_date + timedelta(days=random_days)
hour = random.randint(8, 20)
minute = random.randint(0, 59)

visit["Arrival_Date"] = arrival_date.strftime("%Y-%m-%d")
visit["Arrival_Time"] = f"{hour:02d}:{minute:02d}"
visit["Waiting_Time_Minutes"] = random.randint(5, 60)

with open("data/visits.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=visits[0].keys())
    writer.writeheader()
    writer.writerows(visits)

with open("data/patients.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=patients[0].keys())
    writer.writeheader()
    writer.writerows(patients)

with open("data/departments.csv", "w", newline="") as file: writer = csv.writer(file) writer.writerow(["Department", "Staff_Count", "Resource_Count"])
for department in departments:
    writer.writerow([
        department,
        department_info[department]["staff"],
        department_info[department]["resources"]
    ])
