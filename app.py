from flask import Flask, render_template, request, redirect, url_for, session, flash
from display import forms
from utils.db import *
from utils.handling_json_files import *


app = Flask(__name__,template_folder="display/templates")
app.secret_key = "my_secret_key"

@app.route('/', methods=['GET', 'POST'])
def home():

    form = forms.Selectteacher()
    
    data = read_json_file("101.json")
    
    form.teacher.choices = [(x[0],x[0]) for x in show_all_teachers()]
    
    if request.method == 'POST' and form.validate_on_submit():
        teacher_id = form.teacher.data
        data = read_json_file(show_teacher_with_eid(teacher_id)[3])        

    all_course_ids = set()
    
    for day in working_days:
        for entry in data[day]:
            all_course_ids.add(entry["course_id"])
    
    courses = {}
                
    for id in all_course_ids:
        title = show_course_with_rid(id)[2]
        department = show_course_with_rid(id)[6]
        sem = show_course_with_rid(id)[8]
        eid = show_course_with_rid(id)[4]
        
        courses[id] = {"title" : title, "department" : department, "sem" : sem, "eid" : eid}
        
    return render_template("teachers_tt.html", form=form, data=data, courses=courses, time_slots=time_slots, days=working_days)

@app.route('/classes', methods=['GET', 'POST'])
def classes():
    
    form = forms.Selectclass()
    
    data = read_json_file("CE3.json")
    
    form.department.choices = [(x[1],x[1]) for x in show_all_classes()]
    form.semester.choices = [(x[2],x[2]) for x in show_all_classes()]
    
    if request.method == 'POST' and form.validate_on_submit():
        dep = form.department.data
        sem = form.semester.data
        data = read_json_file(show_class_with_department_sem(dep, sem)[3])        

    all_course_ids = set()
    
    for day in working_days:
        for entry in data[day]:
            all_course_ids.add(entry["course_id"])
    
    courses = {}
                
    for id in all_course_ids:
        title = show_course_with_rid(id)[2]
        department = show_course_with_rid(id)[6]
        sem = show_course_with_rid(id)[8]
        eid = show_course_with_rid(id)[4]
        
        courses[id] = {"title" : title, "department" : department, "sem" : sem, "eid" : eid}
        
    return render_template("classes_tt.html", form=form, data=data, courses=courses, time_slots=time_slots, days=working_days)

if __name__ == '__main__':
     app.run(host="0.0.0.0",debug=True)