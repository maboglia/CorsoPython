import mysql.connector
import json


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="countries"

)

cursor = conn.cursor()
cursor.execute("SELECT * FROM countries")

# for row in cursor:
#     for i, col in enumerate(row):
#         print(f"{i}: {col}")

capitali = [{"country": row[13],"capital": row[6]} for row in cursor]

with open("capitali.json", "w") as f:
    json.dump(capitali, f, indent=4)

# print(json.dumps(capitali, indent=4))

cursor.close()
conn.close()