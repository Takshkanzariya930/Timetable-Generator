from db import *
import json

all_courses_of_department = show_courses_department_wise("CE")

time_slots = ["09:05", "10:00", "10:55", "11:50", "12:40", "01:25", "02:20", "03:15", "04:10"]
working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

rids = [i[0] for i in all_courses_of_department]
eids = [i[4] for i in all_courses_of_department]

my_dict = []
time_table = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
        
for eid in eids:
    
    with(open(f"data/{show_teacher_with_eid(eid)[3]}") as f):
        my_dict = json.load(f)["Occupied"]
    
    for day in working_days:
        
        instants = []
        
        for _ in my_dict[day]:
            
            print(day)
            print(_)
            
        break
        
    break