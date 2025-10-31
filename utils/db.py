import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password='password', database="schedgendb")

cursor = conn.cursor()

def show_all_teachers():
    cursor.execute("SELECT * FROM teachers")
    return cursor.fetchall()

def show_all_courses():
    cursor.execute("SELECT * FROM courses")
    return cursor.fetchall()

def show_all_classes():
    cursor.execute("SELECT * FROM classes")
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

def show_courses_department_wise_lec(department, sem):
    cursor.execute("SELECT * FROM courses WHERE department = %s AND sem = %s AND type = 'lec'", (department, sem, ))
    return cursor.fetchall()

def show_courses_department_wise_lab(department, sem):
    cursor.execute("SELECT * FROM courses WHERE department = %s AND sem = %s AND type = 'lab'", (department, sem, ))
    return cursor.fetchall()

def show_class_with_department_sem(department, sem):
    cursor.execute("SELECT * FROM classes WHERE department = %s AND sem = %s", (department, sem, ))
    return cursor.fetchone()