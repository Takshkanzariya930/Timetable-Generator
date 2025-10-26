import json
from utils.db import *
import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password='password', database="schedgendb")

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS courses")
cursor.execute("DROP TABLE IF EXISTS teachers")

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

cursor.execute("""
INSERT INTO teachers(eid,name) VALUES
(101, "SNG"),
(102, "NBD"),
(103, "CB"),
(104, "DG"),
(105, "HNP"),
(106, "VVN"),
(107, "JMK"),
(108, "SJ"),
(109, "PDP"),
(110, "PKT"),
(111, "PSB"),
(112, "XI"),
(113, "SRP"),
(114, "MDP");
""")

cursor.execute("""
INSERT INTO courses(cid, cname, type, eid, classes_per_week, department, group_no, sem, class) VALUES
(202040301, "DS", "lec", 108, 4, "CE", NULL, 3, "311"),
(202040301, "DS", "lab", 101, 1, "CE", "A4", 3, "232"),
(202040301, "DS", "lab", 109, 1, "CE", "B4", 3, "232"),
(202040301, "DS", "lab", 108, 1, "CE", "C4", 3, "232"),
(202040301, "DS", "lab", 101, 1, "CE", "D4", 3, "232"),
(202040301, "DBMS", "lec", 106, 4, "CE", NULL, 3, "311"),
(202040301, "DBMS", "lab", 110, 1, "CE", "A4", 3, "CE5"),
(202040301, "DBMS", "lab", 106, 1, "CE", "B4", 3, "CE5"),
(202040301, "DBMS", "lab", 110, 1, "CE", "C4", 3, "CE5"),
(202040301, "DBMS", "lab", 111, 1, "CE", "D4", 3, "CE5"),
(202003402, "FEBM", "lec", 107, 3, "CE", NULL, 3, "311"),
(202000303, "PSNM", "lec", 102, 3, "CE", NULL, 3, "311"),
(202000303, "PSNM", "lab", 102, 1, "CE", "A4", 3, "211"),
(202000303, "PSNM", "lab", 113, 1, "CE", "B4-C4", 3, "211"),
(202000303, "PSNM", "lab", 114, 1, "CE", "D4", 3, "211"),
(202040303, "DF", "lec", 105, 3, "CE", NULL, 3, "311"),
(202040303, "DF", "lab", 112, 1, "CE", "A4", 3, "329A"),
(202040303, "DF", "lab", 105, 1, "CE", "B4", 3, "330A"),
(202040303, "DF", "lab", 104, 1, "CE", "C4", 3, "329A"),
(202040303, "DF", "lab", 105, 1, "CE", "D4", 3, "330A"),
(900009901, "CPI", "lab", 103, 1, "CE", "A4-B4", 3, "311"),
(900009901, "CPI", "lab", 103, 1, "CE", "C4-D4", 3, "311"),
(202003403, "Ethos", "lec", 101, 2, "CE", NULL, 3, "311"),
(202040301, "DS2", "lec", 101, 4, "CE", NULL, 3, "311");
""")

cursor.execute("DELETE FROM `schedgendb`.`courses` WHERE (`rid` = '2')")
cursor.execute("DELETE FROM `schedgendb`.`courses` WHERE (`rid` = '3')")
cursor.execute("DELETE FROM `schedgendb`.`courses` WHERE (`rid` = '4')")
cursor.execute("DELETE FROM `schedgendb`.`courses` WHERE (`rid` = '5')")
cursor.execute("DELETE FROM `schedgendb`.`courses` WHERE (`rid` = '7')")
cursor.execute("DELETE FROM `schedgendb`.`courses` WHERE (`rid` = '8')")
cursor.execute("DELETE FROM `schedgendb`.`courses` WHERE (`rid` = '9')")
cursor.execute("DELETE FROM `schedgendb`.`courses` WHERE (`rid` = '10')")
cursor.execute("DELETE FROM `schedgendb`.`courses` WHERE (`rid` = '13')")
cursor.execute("DELETE FROM `schedgendb`.`courses` WHERE (`rid` = '14')")
cursor.execute("DELETE FROM `schedgendb`.`courses` WHERE (`rid` = '15')")
cursor.execute("DELETE FROM `schedgendb`.`courses` WHERE (`rid` = '17')")
cursor.execute("DELETE FROM `schedgendb`.`courses` WHERE (`rid` = '18')")
cursor.execute("DELETE FROM `schedgendb`.`courses` WHERE (`rid` = '19')")
cursor.execute("DELETE FROM `schedgendb`.`courses` WHERE (`rid` = '20')")
cursor.execute("DELETE FROM `schedgendb`.`courses` WHERE (`rid` = '21')")
cursor.execute("DELETE FROM `schedgendb`.`courses` WHERE (`rid` = '22')")


blueprint = {"Occupied" : { "Monday" : [],
                            "Tuesday" : [],
                            "Wednesday" : [],
                            "Thursday" : [],
                            "Friday" : [] }}

conn.commit()

for row in show_all_teachers():  
    with(open(f"data/{row[3]}", "w") as f):
        json.dump(blueprint, f)
