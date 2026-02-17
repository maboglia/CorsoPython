# 🐍 Python + 🗄️ SQLite

## 1️⃣ Vantaggio principale

SQLite è **già incluso nella libreria standard di Python** tramite il modulo:

```python
import sqlite3
```

👉 Non serve installare nulla.

---

# 2️⃣ Creare (o aprire) un database

```python
import sqlite3

conn = sqlite3.connect("scuola.db")  # crea il file se non esiste
cursor = conn.cursor()
```

📁 `scuola.db` è un semplice file.

---

# 3️⃣ Creare una tabella

```python
cursor.execute("""
CREATE TABLE IF NOT EXISTS studenti (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    eta INTEGER
)
""")

conn.commit()
```

---

# 4️⃣ CRUD completo

## 🔹 INSERT

```python
cursor.execute(
    "INSERT INTO studenti (nome, eta) VALUES (?, ?)",
    ("Mario", 22)
)
conn.commit()
```

⚠ In SQLite si usa `?` come placeholder (non `%s`).

---

## 🔹 SELECT

```python
cursor.execute("SELECT * FROM studenti")
rows = cursor.fetchall()

for row in rows:
    print(row)
```

---

## 🔹 UPDATE

```python
cursor.execute(
    "UPDATE studenti SET eta=? WHERE nome=?",
    (23, "Mario")
)
conn.commit()
```

---

## 🔹 DELETE

```python
cursor.execute(
    "DELETE FROM studenti WHERE nome=?",
    ("Mario",)
)
conn.commit()
```

---

# 5️⃣ Accesso per nome colonna (Row Factory)

Molto utile didatticamente:

```python
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute("SELECT * FROM studenti")
rows = cursor.fetchall()

for row in rows:
    print(row["nome"], row["eta"])
```

---

# 6️⃣ Gestione transazioni

```python
try:
    conn.execute("BEGIN")

    cursor.execute("INSERT INTO studenti (nome, eta) VALUES (?, ?)", ("Luca", 20))
    cursor.execute("UPDATE studenti SET eta=? WHERE nome=?", (21, "Luca"))

    conn.commit()

except:
    conn.rollback()
```

---

# 7️⃣ Uso con context manager (più pulito)

```python
import sqlite3

with sqlite3.connect("scuola.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM studenti")
    print(cursor.fetchall())
```

La connessione viene chiusa automaticamente.

---

# 8️⃣ Quando usare SQLite con Python?

✅ Script CLI
✅ Applicazioni desktop
✅ Prototipi
✅ Test automatici
✅ Progetti didattici
✅ Piccoli gestionali locali

❌ Non ideale per:

* Sistemi web con molti utenti contemporanei
* Carichi di scrittura elevati

---

# 9️⃣ Esempio mini-progetto CLI didattico

Struttura tipica del progetto:

```
progetto/
│
├── main.py
├── database.py
└── scuola.db
```

**database.py**

```python
import sqlite3

def get_connection():
    return sqlite3.connect("scuola.db")
```

**main.py**

```python
from database import get_connection

def inserisci(nome, eta):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO studenti (nome, eta) VALUES (?, ?)",
            (nome, eta)
        )

inserisci("Anna", 19)
```

---

# 🔎 Confronto rapido: Python + SQLite vs MySQL

|                 | SQLite        | MySQL             |
| --------------- | ------------- | ----------------- |
| Installazione   | Nessuna       | Server necessario |
| File            | Singolo `.db` | Server + storage  |
| Multiutente     | Limitato      | Ottimo            |
| Velocità locale | Molto alta    | Buona             |
| Ideale per      | CLI / Desktop | Web / Enterprise  |

