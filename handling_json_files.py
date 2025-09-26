from db import *
import json
from datetime import datetime, timedelta

start_of_day = datetime.strptime("09:00","%H:%M")
end_of_day = datetime.strptime("17:00","%H:%M")

time_slots = [[]]

def is_occupied(eid, day, time):
    
    file = show_teacher_with_eid(eid)[3]
    time = datetime.strptime(time, "%H:%M")
    
    with(open(f"data/{file}") as f):
        data = json.load(f)["Occupied"]
    
    for occupied_time in data[day]:
        
        start = datetime.strptime(occupied_time["start"], "%H:%M")
        end = datetime.strptime(occupied_time["end"], "%H:%M")
        
        if time >= start and time < end:
            return True
    
    return False

def occupy_slot(eid, day, time, rid):
    
    file = show_teacher_with_eid(eid)[3]
    
    start = datetime.strptime(time, "%H:%M")

    if is_it_lec_or_lab(rid) == "lec":
        end = start + timedelta(hours=1)
    else :
        end = start + timedelta(hours=2)
    
    occ_dict = { "start": start , "end": end, "course_id": rid }
    
    if not is_occupied(eid, day, time):
        
        with(open(f"data/{file}") as f):
            data = json.load(f)
            
        data["Occupied"][day].append(occ_dict)
        
        with(open(f"data/{file}", "w") as f):
            json.dump(data, f)
            
# print(is_occupied(101, "Monday", "10:30"))