from flask import Flask, render_template, request, redirect, url_for, session, flash
from display import forms
from utils.db import *
from utils.handling_json_files import *


app = Flask(__name__,template_folder="display/templates")
app.secret_key = "my_secret_key"

@app.route('/', methods=['GET', 'POST'])
def home():
    
    form = forms.Selectteachers()
    form.teacher.choices = [(x[0], x[0]) for x in show_all_teachers()]
    data = []
    courses = []
    data = read_json_file(show_teacher_with_eid(101)[3])
    
    if request.method == 'POST' and form.validate_on_submit():
        teacherid = form.teacher.data   
        data = read_json_file(show_teacher_with_eid(teacherid)[3])
    
        course_ids = []

        for day in working_days:
            for entry in data[day]:
                course_ids.append(entry["course_id"])

        course_ids = list(set(course_ids))

        for id in course_ids:
            print(show_course_with_rid(id))
            title = show_course_with_rid(id)[2]
            course_number = show_course_with_rid(id)[1]
            teacher_name = show_teacher_with_eid(show_course_with_rid(id)[4])[1]
            room_number = show_course_with_rid(id)[9]
            
            courses.append({id : {"title" : title, "course_number" : course_number, "teacher_name" : teacher_name, "room_number" : room_number}})

        courses = {k : v for d in courses for k, v in d.items()}
    
    return render_template("home.html", form=form, data=data, courses=courses, time_slots=time_slots, days=working_days)


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)