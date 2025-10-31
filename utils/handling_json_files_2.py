from .db import *
import json

time_slots = ["09:05", "10:00", "10:55", "11:50", "12:40", "01:25", "02:20", "03:15", "04:10"]
working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def is_occupied(eid, day, time_slot_index):
    
    file = show_teacher_with_eid(eid)[3]
    
    with(open(f"data/{file}") as f):
        data = json.load(f)["Occupied"]
        
    for occupied_time in data[day]:
        
        if occupied_time["time_slot_index"] == time_slot_index:
            
            for occupied_time_slot in data[day]:
                if occupied_time_slot["time_slot_index"] == time_slot_index-1:
                    
                    if occupied_time_slot["duration"] == 2:
                        return True
                    
                    
             
    
    return False