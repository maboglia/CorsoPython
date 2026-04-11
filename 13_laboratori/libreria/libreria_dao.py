from libro import Libro
import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root', 
    database = 'its2026'
)

cursor = db.cursor()


cursor.execute("select * from biblioteca")

libri = cursor.fetchall()
libreria = []

for libro in libri:
    id = libro[0]
    Codice = libro[1]
    Autore = libro[2]
    Titolo = libro[3]
    Editore = libro[4]
    Classificazione = libro[5]
    
    l = Libro(id, Codice, Autore, Titolo, Editore, Classificazione)
    libreria.append(l)
    
