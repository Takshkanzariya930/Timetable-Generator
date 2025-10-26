from utils.handling_json_files import *

data = read_json_file(show_teacher_with_eid(101)[3])

# print(data)
course_ids = []

for day in working_days:
    for entry in data[day]:
        course_ids.append(entry["course_id"])

course_ids = list(set(course_ids))

courses = []
for id in course_ids:
    # print(show_course_with_rid(id))
    title = show_course_with_rid(id)[2]
    course_number = show_course_with_rid(id)[1]
    teacher_name = show_teacher_with_eid(show_course_with_rid(id)[4])[1]
    room_number = show_course_with_rid(id)[9]
    
    courses.append({id : {"title" : title, "course_number" : course_number, "teacher_name" : teacher_name, "room_number" : room_number}})
    
courses = {k : v for d in courses for k, v in d.items()}

slot_info = courses[23]
