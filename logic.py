from utils.db import * 
from utils.handling_json_files import *
import random

all_courses = []
time_slots_local = time_slots.copy()
working_days_local = working_days.copy()

for course in show_all_courses():
    course = [course[i] for i in [0,3,4,5,10]]
    all_courses.append(course)  

for i in range(len(all_courses)):
    time_slots_local = time_slots.copy()
    working_days_local = working_days.copy()
    ri = random.randrange(0, len(all_courses))
    course = all_courses[ri]
    
    for _ in range(course[3]):
        rt = random.randrange(0, len(time_slots_local))
        rd = random.randrange(0, len(working_days_local))
        
        occupy_slot(course[2], working_days_local[rd], [ri], course[0])
        add_class_to_classes_scheduled_per_week(course[0])
        
        time_slots_local.pop(rt)
        working_days_local.pop(rd)
        
    all_courses.pop(ri)
    
print(all_courses)