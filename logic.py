from db import * 
from handling_json_files import *
import random

all_courses = []

for course in show_all_courses():
    course = [course[i] for i in [0,3,4,5,10]]
    all_courses.append(course)

