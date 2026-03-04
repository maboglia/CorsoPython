import sqlite3
import json

# definisci connessione
connection = sqlite3.connect('capitali.db')

# ottieni cursorer
cursor = connection.cursor()

# crea tabella
cmd1 = """
CREATE TABLE IF NOT EXISTS 
capitali(country_id INTEGER PRIMARY KEY AUTOINCREMENT, country TEXT, capital TEXT)
"""

# esegui query
cursor.execute(cmd1)

with open("capitali.json", 'r', encoding='utf-8') as f:
    countries = json.load(f)


print(countries)
for i, country in enumerate(countries, start=1):
    # add records
    query = f"INSERT INTO capitali VALUES (null,?,?)"
    print(query)
    cursor.execute(query,(country['country'], country['capital']))

cursor.execute("SELECT * FROM capitali")
# get results
capitali = cursor.fetchall()

for capitale in capitali:
    print(capitale)


connection.commit()

connection.close()
