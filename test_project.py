from project import total_visits, average_waiting_time, busiest_department

def test_total_visits():
     visits = [1, 2, 3, 4, 5]
     assert total_visits(visits) == 5
def test_average_waiting_time():
     import pandas as pd
     visits = pd.DataFrame({"Waiting_Time_Minutes": [10, 20, 30]})
     assert average_waiting_time(visits) == 20
def test_busiest_department():
     import pandas as pd
     visits = pd.DataFrame({
     "Department": ["Emergency", "Cardiology", "Emergency"]
     })
     assert busiest_department(visits) == "Emergency"