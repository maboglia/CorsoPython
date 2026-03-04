import sqlite3

# definisci connessione
connection = sqlite3.connect('store_transactions.db')

# ottieni cursorer
cursor = connection.cursor()

# crea tabella
cmd1 = """
CREATE TABLE IF NOT EXISTS 
libri(libro_id INTEGER PRIMARY KEY AUTOINCREMENT, titolo TEXT)
"""

# esegui query
cursor.execute(cmd1)

titoli = [
    'il nome della rosa',
    'il nome della viola',
    'il nome della margherita'
    ]
print(titoli)
for i, titolo in enumerate(titoli, start=1):
    # add records
    query = f"INSERT INTO libri VALUES (null,'{titolo}')"
    print(query)
    cursor.execute(query)

cursor.execute("SELECT * FROM libri")
# get results
libri = cursor.fetchall()

for libro in libri:
    print(libro)


connection.commit()

connection.close()
