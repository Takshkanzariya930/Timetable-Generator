import os
import json
from db import *
import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password='password', database="schedgendb")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS teachers (
    eid INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100),
    file_path VARCHAR(255) AS (CONCAT(eid, '.json')) STORED,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    rid INT AUTO_INCREMENT PRIMARY KEY,
    cid INT NOT NULL,
    cname VARCHAR(255) NOT NULL,
    type VARCHAR(3) NOT NULL,
    eid INT,
    classes_per_week INT NOT NULL,
    department VARCHAR(255) NOT NULL,
    group_no VARCHAR(6),
    sem INT NOT NULL,
    class VARCHAR(5),
    classes_scheduled_per_week INT DEFAULT 0,
    FOREIGN KEY (eid) REFERENCES teachers(eid) ON UPDATE CASCADE ON DELETE SET NULL
)
""")

blueprint = {"Occupied" : { "Monday" : [],
                            "Tuesday" : [],
                            "Wednesday" : [],
                            "Thursday" : [],
                            "Friday" : [] }}


for row in show_all_teachers():  
    if not os.path.exists(f"data/{row[3]}"):
        with(open(f"data/{row[3]}", "w") as f):
            json.dump(blueprint, f)
        