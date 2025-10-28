from .db import *
import json

time_slots = ["09:05", "10:00", "10:55", "11:50", "12:40", "01:25", "02:20", "03:15", "04:10"]
working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

break_slot = 4

valid_indices = [i for i in range(len(time_slots)) if i != break_slot]

def is_occupied(eid, day, time_slot_indices):
    
    file = show_teacher_with_eid(eid)[3]
    
    with(open(f"data/{file}") as f):
        data = json.load(f)["Occupied"]
    
    for occupied_time in data[day]:
        # print(occupied_time)
        if time_slot_indices in [occupied_time["time_slot_indices"]]:
            return True
    
    return False

def occupy_slot(eid, day, time_slot_indices, rid):
    
    file = show_teacher_with_eid(eid)[3]

    occ_dict = { "time_slot_indices" : time_slot_indices, "course_id": rid }

    if not is_occupied(eid, day, time_slot_indices):

        with(open(f"data/{file}") as f):
            data = json.load(f)
            
        data["Occupied"][day].append(occ_dict)

        with(open(f"data/{file}", "w") as f):
            json.dump(data, f)

def read_json_file(file):
    
    with(open(f"data/{file}") as f):
        data = json.load(f)['Occupied']
    
    return data

def is_class_occupied(department, sem, day, time_slot_indices):
    
    file = show_class_with_department_sem(department, sem)[3]
    
    with(open(f"data/{file}") as f):
        data = json.load(f)["Occupied"]
    
    for occupied_time in data[day]:
        # print(occupied_time)
        if time_slot_indices in [occupied_time["time_slot_indices"]]:
            return True
    
    return False

def occupy_class_slot(department, sem, day, time_slot_indices, rid):
    
    file = show_class_with_department_sem(department, sem)[3]

    occ_dict = { "time_slot_indices" : time_slot_indices, "course_id": rid }

    if not is_class_occupied(department, sem, day, time_slot_indices):

        with(open(f"data/{file}") as f):
            data = json.load(f)
            
        data["Occupied"][day].append(occ_dict)

        with(open(f"data/{file}", "w") as f):
            json.dump(data, f)
