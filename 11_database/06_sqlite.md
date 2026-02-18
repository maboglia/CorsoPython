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

---

## **tipi di dato in SQLite**.

In **SQLite** i tipi di dato funzionano in modo diverso rispetto a MySQL o PostgreSQL.

---

# 🔎 1️⃣ Caratteristica fondamentale: Tipizzazione dinamica

SQLite usa un sistema chiamato:

> **Type Affinity (affinità di tipo)**

👉 Non esistono tipi rigidi come negli altri DBMS.
👉 Il tipo è associato **alla colonna**, ma il valore può avere tipo diverso.

Esempio:

```sql
CREATE TABLE esempio (
    numero INTEGER
);
```

Puoi comunque inserire:

```sql
INSERT INTO esempio VALUES ('ciao');
```

SQLite lo permette (anche se non è consigliato).

---

# 2️⃣ I 5 tipi di storage reali

Internamente SQLite usa solo **5 tipi di dato effettivi**:

| Tipo        | Descrizione           |
| ----------- | --------------------- |
| **NULL**    | Valore nullo          |
| **INTEGER** | Intero (1–8 byte)     |
| **REAL**    | Numero floating point |
| **TEXT**    | Stringa UTF-8/UTF-16  |
| **BLOB**    | Dati binari           |

⚠ Questi sono i veri tipi memorizzati su disco.

---

# 3️⃣ Type Affinity (come interpreta i tipi dichiarati)

Quando dichiari una colonna:

```sql
CREATE TABLE studenti (
    id INT,
    nome VARCHAR(100),
    voto DECIMAL(5,2),
    attivo BOOLEAN,
    dati BLOB
);
```

SQLite converte tutto in una delle 5 affinità:

| Tipo dichiarato     | Affinità |
| ------------------- | -------- |
| INT, INTEGER        | INTEGER  |
| VARCHAR, TEXT, CHAR | TEXT     |
| DECIMAL, NUMERIC    | NUMERIC  |
| REAL, FLOAT, DOUBLE | REAL     |
| BLOB                | BLOB     |

---

# 4️⃣ Tipo NUMERIC (particolarità)

NUMERIC è speciale:

Se inserisci:

* `"123"` → diventa INTEGER
* `"123.45"` → diventa REAL
* `"abc"` → resta TEXT

---

# 5️⃣ Booleani in SQLite

SQLite **non ha un vero BOOLEAN**.

```sql
BOOLEAN
```

è solo un alias di NUMERIC.

Convenzione:

```sql
0 = false
1 = true
```

---

# 6️⃣ Date e Orari

SQLite **non ha un tipo DATE nativo**.

Le date possono essere salvate come:

| Formato            | Tipo    |
| ------------------ | ------- |
| "2025-02-17"       | TEXT    |
| timestamp Unix     | INTEGER |
| 2450000.5 (Julian) | REAL    |

Esempio:

```sql
CREATE TABLE eventi (
    data TEXT
);
```

Funzioni disponibili:

* `date()`
* `datetime()`
* `strftime()`

---

# 7️⃣ Differenza rispetto a MySQL

In MySQL:

* Tipizzazione **rigida**
* VARCHAR(100) è realmente limitato
* BOOLEAN è reale (alias TINYINT)
* DATE è tipo nativo

In SQLite:

* VARCHAR(100) non impone limite reale
* Tipi molto flessibili
* Meno controllo, più libertà

---

# 8️⃣ STRICT mode (novità moderna)

Dalla versione 3.37 esiste:

```sql
CREATE TABLE studenti (
    id INTEGER,
    nome TEXT
) STRICT;
```

👉 Impone controllo più rigido sui tipi
👉 Si comporta più come MySQL/PostgreSQL

Molto utile in ambito didattico.

---

# 9️⃣ Riassunto sintetico

SQLite usa solo 5 tipi reali:

```
NULL
INTEGER
REAL
TEXT
BLOB
```

Tutto il resto è interpretazione tramite **type affinity**.
