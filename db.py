import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password='password', database="transaction_manager")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100)
)
""")