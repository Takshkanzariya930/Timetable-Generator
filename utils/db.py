import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password='password', database="schedgendb")

cursor = conn.cursor()

def show_all_teachers():
    cursor.execute("SELECT * FROM teachers")
    return cursor.fetchall()

def show_all_courses():
    cursor.execute("SELECT * FROM courses")
    return cursor.fetchall()

def show_teacher_with_eid(eid):
    cursor.execute("SELECT * FROM teachers WHERE eid = %s", (eid, ))
    return cursor.fetchone()

def show_course_with_rid(rid):
    cursor.execute("SELECT * FROM courses WHERE rid = %s", (rid, ))
    return cursor.fetchone()

def add_class_to_classes_scheduled_per_week(rid):
    cursor.execute("UPDATE courses SET classes_scheduled_per_week = classes_scheduled_per_week + 1 WHERE rid = %s", (rid, ))
    conn.commit()

def is_it_lec_or_lab(rid):
    cursor.execute("SELECT type FROM courses WHERE rid = %s", (rid, ))
    return cursor.fetchone()[0]

def show_courses_department_wise(department):
    cursor.execute("Select * FROM courses WHERE department = %s", (department, ))
    return cursor.fetchall()