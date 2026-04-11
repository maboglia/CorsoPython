from tinydb import TinyDB

db = TinyDB("magazzino.json")

# db.insert({"nome_prodotto": "PC", "prezzo":1200})

# for p in db.all():
#     print(p['nome_prodotto'])
    
    
# # Inserire più record
# db.insert_multiple([
#     {"nome": "Mario", "eta": 35},
#     {"nome": "Maria", "eta": 45}
# ])

# Tutti i record
# for user in db.all():
#     print(user, user['nome'], user['eta'] )

# # TinyDB usa l’oggetto Query.

from tinydb import Query

Persona = Query()

# # # Cercare record con condizione
ris = db.search(Persona.eta > 25)
print(ris)

# # Condizione numerica
# ris = db.search(Persona.eta > 30)
# # Condizione multipla (AND)
# ris = db.search((Persona.eta > 20) & (Persona.nome == "Anna"))
# # Condizione OR
# ris = db.search((Persona.nome == "Anna") | (Persona.nome == "Luca"))

# # 5) Primo record trovato
ris = db.get(Persona.nome == "Mario")
print(ris)

# # 6) Aggiornamento record
# # Update con condizione
# db.update({"nome": "Mario"}, Persona.nome == "Luca")
# # Aggiornamento usando funzione
# db.update(lambda x: {"eta": x["eta"] + 1}, Persona.nome == "Anna")

# 7) Eliminazione record
# Remove con condizione
db.remove(Persona.nome == "Maria")

# # Cancellare tutto
# db.truncate()

# # 8) Uso di tabelle (collections)
# # TinyDB può gestire più tabelle.

utenti = db.table("utenti")
prodotti = db.table("prodotti")

utenti.insert({"username": "pippo", "ruolo": "editor"})
prodotti.insert({"nome": "Laptop", "prezzo": 1500})

# Leggere da tabella:

print(utenti.all())
print(prodotti.all())

# 9) ID automatico (doc_id)
# Ogni record ha un ID.

doc_id = db.insert({"nome": "Sara", "eta": 20})
print(doc_id)

# # Leggere per ID:

record = db.get(doc_id=doc_id)
print(record)

# # Aggiornare per ID:

# db.update({"eta": 21}, doc_ids=[doc_id])
# # Eliminare per ID:

# db.remove(doc_ids=[doc_id])

# # 10) Operazioni avanzate con tinydb.operations
# from tinydb.operations import increment, add

# db.update(increment("eta"), Persona.nome == "Mario")
# # Aggiungere valori a una lista:

# db.update(add("hobby", ["calcio"]), Persona.nome == "Mario")

# # 11) Query su campi nested (dizionari interni)
# db.insert({"nome": "Paolo", "indirizzo": {"citta": "Roma"}})
# # Query nested:

# ris = db.search(Persona.indirizzo.citta == "Roma")
# print(ris)

# ------------------------------------------------------------
print('-' * 40)
# Tutti i record
for user in db.all():
    print(user, user['nome'], user['eta'] )
# ------------------------------------------------------------
print('-' * 40)


# # 12) Chiusura DB
# db.close()