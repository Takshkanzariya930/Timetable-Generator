from utils.handling_json_files import *
import random

data = read_json_file(show_class_with_department_sem("CE", 3)[3])

all_course_ids = set()

for day in working_days:
        for entry in data[day]:
            all_course_ids.add(entry["course_id"])
            
print(all_course_ids)