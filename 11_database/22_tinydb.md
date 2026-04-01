# 📌 TinyDB (Python) – Scheda Rapida

## ✅ Installazione

```bash
pip install tinydb
```

---

# 1) Creazione / Apertura Database

TinyDB salva i dati in un file JSON.

```python
from tinydb import TinyDB

db = TinyDB("db.json")
```

---

# 2) Inserimento dati

## Inserire un singolo record

```python
db.insert({"nome": "Mario", "eta": 30})
```

## Inserire più record

```python
db.insert_multiple([
    {"nome": "Anna", "eta": 25},
    {"nome": "Luca", "eta": 40}
])
```

---

# 3) Lettura dati

## Tutti i record

```python
print(db.all())
```

---

# 4) Query (ricerche)

TinyDB usa l’oggetto `Query`.

```python
from tinydb import Query

Persona = Query()
```

## Cercare record con condizione

```python
ris = db.search(Persona.nome == "Mario")
print(ris)
```

## Condizione numerica

```python
ris = db.search(Persona.eta > 30)
```

## Condizione multipla (AND)

```python
ris = db.search((Persona.eta > 20) & (Persona.nome == "Anna"))
```

## Condizione OR

```python
ris = db.search((Persona.nome == "Anna") | (Persona.nome == "Luca"))
```

---

# 5) Primo record trovato

```python
ris = db.get(Persona.nome == "Mario")
print(ris)
```

---

# 6) Aggiornamento record

## Update con condizione

```python
db.update({"eta": 31}, Persona.nome == "Mario")
```

## Aggiornamento usando funzione

```python
db.update(lambda x: {"eta": x["eta"] + 1}, Persona.nome == "Anna")
```

---

# 7) Eliminazione record

## Remove con condizione

```python
db.remove(Persona.nome == "Luca")
```

## Cancellare tutto

```python
db.truncate()
```

---

# 8) Uso di tabelle (collections)

TinyDB può gestire più tabelle.

```python
utenti = db.table("utenti")
prodotti = db.table("prodotti")

utenti.insert({"username": "admin", "ruolo": "root"})
prodotti.insert({"nome": "PC", "prezzo": 1200})
```

Leggere da tabella:

```python
print(utenti.all())
```

---

# 9) ID automatico (doc_id)

Ogni record ha un ID.

```python
doc_id = db.insert({"nome": "Sara", "eta": 20})
print(doc_id)
```

Leggere per ID:

```python
record = db.get(doc_id=doc_id)
print(record)
```

Aggiornare per ID:

```python
db.update({"eta": 21}, doc_ids=[doc_id])
```

Eliminare per ID:

```python
db.remove(doc_ids=[doc_id])
```

---

# 10) Operazioni avanzate con `tinydb.operations`

```python
from tinydb.operations import increment, add

db.update(increment("eta"), Persona.nome == "Mario")
```

Aggiungere valori a una lista:

```python
db.update(add("hobby", ["calcio"]), Persona.nome == "Mario")
```

---

# 11) Query su campi nested (dizionari interni)

```python
db.insert({"nome": "Paolo", "indirizzo": {"citta": "Roma"}})
```

Query nested:

```python
ris = db.search(Persona.indirizzo.citta == "Roma")
print(ris)
```

---

# 12) Chiusura DB

```python
db.close()
```

---

# 13) Esempio completo CRUD

```python
from tinydb import TinyDB, Query

db = TinyDB("db.json")
Persona = Query()

# CREATE
db.insert({"nome": "Mario", "eta": 30})

# READ
print(db.search(Persona.eta >= 30))

# UPDATE
db.update({"eta": 31}, Persona.nome == "Mario")

# DELETE
db.remove(Persona.nome == "Mario")

db.close()
```

---

# 📌 Quando usare TinyDB?

✅ progetti piccoli
✅ dati locali su file JSON
✅ configurazioni / app CLI / prototipi
❌ non adatto a grandi sistemi multiutente (meglio SQLite/PostgreSQL)

