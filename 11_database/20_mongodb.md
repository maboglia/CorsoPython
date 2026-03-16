# Lezione: Python e MongoDB

## 1. Introduzione ai Database NoSQL

MongoDB è un database **NoSQL document-oriented**.

Differenze principali rispetto ai database relazionali:

| SQL      | MongoDB    |
| -------- | ---------- |
| Database | Database   |
| Tabella  | Collection |
| Riga     | Document   |
| Colonna  | Campo      |

Caratteristiche:

* dati in formato **JSON/BSON**
* schema **flessibile**
* scalabilità orizzontale
* molto usato in **web app, microservizi e big data**

Esempio documento MongoDB:

```json
{
  "nome": "Mario",
  "cognome": "Rossi",
  "eta": 30,
  "corsi": ["Python", "MongoDB"]
}
```

---

# 2. Installazione ambiente

### Installare MongoDB

Scaricare da:

MongoDB

oppure usare Docker.

Verifica:

```bash
mongod --version
```

Avvio server:

```bash
mongod
```

---

# 3. Installare libreria Python

Python usa la libreria ufficiale:

PyMongo

Installazione:

```bash
pip install pymongo
```

Test installazione:

```python
import pymongo
print("PyMongo installato")
```

---

# 4. Connessione a MongoDB con Python

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["scuola"]

print("Connessione OK")
```

Struttura:

```
client
 └── database
      └── collection
            └── document
```

---

# 5. Creazione Collection

MongoDB crea automaticamente la collection.

```python
studenti = db["studenti"]
```

---

# 6. Inserimento dati

### Inserire un documento

```python
studente = {
    "nome": "Luca",
    "cognome": "Bianchi",
    "eta": 22,
    "corso": "Informatica"
}

studenti.insert_one(studente)
```

---

### Inserire più documenti

```python
lista_studenti = [
    {"nome": "Anna", "eta": 21},
    {"nome": "Marco", "eta": 23},
    {"nome": "Giulia", "eta": 20}
]

studenti.insert_many(lista_studenti)
```

---

# 7. Query (lettura dati)

### Trovare tutti i documenti

```python
for s in studenti.find():
    print(s)
```

---

### Query con filtro

```python
ris = studenti.find({"nome": "Anna"})

for s in ris:
    print(s)
```

---

### Operatori

```python
studenti.find({"eta": {"$gt": 21}})
```

Operatori comuni:

| Operatore | Significato     |
| --------- | --------------- |
| $gt       | maggiore        |
| $lt       | minore          |
| $gte      | maggiore uguale |
| $lte      | minore uguale   |
| $ne       | diverso         |

---

# 8. Aggiornamento dati

### Update singolo

```python
studenti.update_one(
    {"nome": "Anna"},
    {"$set": {"eta": 22}}
)
```

---

### Update multiplo

```python
studenti.update_many(
    {"corso": "Informatica"},
    {"$set": {"anno": 1}}
)
```

---

# 9. Cancellazione

### Eliminare un documento

```python
studenti.delete_one({"nome": "Marco"})
```

---

### Eliminare più documenti

```python
studenti.delete_many({"eta": {"$lt": 21}})
```

---

# 10. Ordinamento

```python
for s in studenti.find().sort("eta", 1):
    print(s)
```

1 = crescente
-1 = decrescente

---

# 11. Proiezione (selezione campi)

```python
for s in studenti.find({}, {"nome": 1, "eta": 1, "_id": 0}):
    print(s)
```

Mostra solo:

```
nome
eta
```

---

# 12. Indici

Gli indici migliorano le prestazioni.

```python
studenti.create_index("nome")
```

---

# 13. Esempio completo

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["scuola"]
studenti = db["studenti"]

studente = {
    "nome": "Paolo",
    "eta": 24,
    "corso": "Data Science"
}

studenti.insert_one(studente)

for s in studenti.find():
    print(s)
```

---

# 14. Mini esercizio per studenti

Realizzare un programma Python che gestisca una **collection libri**.

Campi:

```
titolo
autore
anno
genere
```

Operazioni da implementare:

1. inserimento libro
2. visualizzazione libri
3. ricerca per autore
4. aggiornamento anno
5. cancellazione libro

---

# 15. Estensione avanzata

Argomenti successivi:

* aggregazioni MongoDB
* pipeline
* MongoDB Atlas (cloud)
* integrazione con API REST
* MongoDB + Flask / FastAPI

---

# 16. Esercizio avanzato

Creare un **gestionale studenti MongoDB con Python**:

Funzioni:

```
1 aggiungi studente
2 mostra studenti
3 cerca studente
4 modifica studente
5 elimina studente
```

