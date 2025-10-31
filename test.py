from utils.handling_json_files import *
import random

all_courses = [(x[0], x[1], x[4], x[5], x[7]) for x in show_courses_department_wise_lab("CE", 3)]

courses_id = [x[1] for x in all_courses]
courses_id = (set(courses_id))

tempa = []
for id in courses_id:
    temp = []
    for courses in all_courses:
        if courses[1] == id:
            temp.append(courses)
    tempa.append(temp)

all_courses = tempa

for _ in all_courses:
    print(_)
