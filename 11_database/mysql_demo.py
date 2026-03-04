import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="fondamenti"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM studenti")

for row in cursor:
    print(row)

cursor.close()
conn.close()