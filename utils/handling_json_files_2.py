from .db import *
import json

time_slots = ["09:05", "10:00", "10:55", "11:50", "12:40", "01:25", "02:20", "03:15", "04:10"]
working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def is_slot_occupied(eid, day, time_slot_index):

    result = False
    
    with(open(f"data/{show_teacher_with_eid(eid)[3]}") as f):
        data = json.load(f)["Occupied"]
        
    for occupied_time in data[day]:
        if time_slot_index == occupied_time["time_slot_index"]:
            result = True
        
    for occupied_time in data[day]:
        if time_slot_index-1 == occupied_time["time_slot_index"]:
            if occupied_time["duration"] == 2:
                result = True
            
    return result

def occupy_slot(eid, day, time_slot_index, rid):
    
    with(open(f"data/{show_teacher_with_eid(eid)[3]}") as f):
        data = json.load(f)
    
    if not is_slot_occupied(eid, day, time_slot_index):
        
        if not is_course_lab(rid):
            
            occ_dict = { "time_slot_index" : time_slot_index, "course_id": rid, "duration" : 1}
            
            data["Occupied"][day].append(occ_dict)
            
        else:
            
            occ_dict = { "time_slot_index" : time_slot_index, "course_id": rid, "duration" : 2}
            
            data["Occupied"][day].append(occ_dict)
            
        with(open(f"data/{show_teacher_with_eid(eid)[3]}", "w") as f):
            json.dump(data, f)
            
def is_c_slot_occupied(dep, sem, day, time_slot_index, group=None):
    
    result = False
    
    with(open(f"data/{show_class_with_department_sem(dep, sem)[3]}") as f):
        data = json.load(f)["Occupied"]
        
    if group == None:
        
        for g in data:
            for occupied_time in data[g][day]:
                if time_slot_index == occupied_time["time_slot_index"]:
                    result = True
                    
            for occupied_time in data[g][day]:
                if time_slot_index-1 == occupied_time["time_slot_index"]:
                    if occupied_time["duration"] == 2:
                        result = True
                        
    else:
        
        for occupied_time in data[group][day]:
            if time_slot_index == occupied_time["time_slot_index"]:
                result = True
                
        for occupied_time in data[group][day]:
                if time_slot_index-1 == occupied_time["time_slot_index"]:
                    if occupied_time["duration"] == 2:
                        result = True
                        
    return result

def occupy_c_slot(dep, sem, day, time_slot_index, rid, group=None):
    
    with(open(f"data/{show_class_with_department_sem(dep, sem)[3]}") as f):
        data = json.load(f)
        
    if not is_c_slot_occupied(dep, sem, day, time_slot_index, group):
    
        if group == None:
               
            if not is_course_lab(rid):
                
                occ_dict = { "time_slot_index" : time_slot_index, "course_id": rid, "duration" : 1}
                for g in data["Occupied"]:
                    data["Occupied"][g][day].append(occ_dict) 
                    
            else:
                
                occ_dict = { "time_slot_index" : time_slot_index, "course_id": rid, "duration" : 2}
                for g in data["Occupied"]:
                    data["Occupied"][g][day].append(occ_dict) 
                    
        else:
            
            if not is_course_lab(rid):
                
                occ_dict = { "time_slot_index" : time_slot_index, "course_id": rid, "duration" : 1}
            
                data["Occupied"][group][day].append(occ_dict) 
                    
            else:
                
                occ_dict = { "time_slot_index" : time_slot_index, "course_id": rid, "duration" : 2}
                
                data["Occupied"][group][day].append(occ_dict) 
                
    with(open(f"data/{show_class_with_department_sem(dep, sem)[3]}", "w") as f):
        json.dump(data, f)