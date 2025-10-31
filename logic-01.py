from utils.db import * 
from utils.handling_json_files import *
import random

all_classes = [(x[1], x[2]) for x in show_all_classes()]

for dep, sem in all_classes:
    
    all_courses = [(x[0], x[4], x[5], x[10]) for x in show_courses_department_wise_lec(dep, sem)]
    working_days_local = working_days.copy()
    time_slots_local = time_slots.copy()

    for course in all_courses:
        
        while course[2] != show_course_with_rid(course[0])[-1]:
        
            time_slot = random.randrange(0, len(time_slots_local))
            day = working_days_local[random.randrange(0, len(working_days_local))]
    
            if  (not is_occupied(course[1], day, time_slot)) and (not is_class_occupied(dep, sem, day, time_slot)):
                occupy_slot(course[1], day, time_slot, course[0])
                occupy_class_slot(dep, sem, day, time_slot, course[0])
                add_class_to_classes_scheduled_per_week(course[0])