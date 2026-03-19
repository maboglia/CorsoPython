# 🐍 Python + 🐬 PyMySQL

## ✅ 1️⃣ Installazione

```bash
pip install pymysql
```

Oppure (consigliato):

```bash
python -m pip install pymysql
```

---

# ✅ 2️⃣ Connessione base

```python
import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    database="testdb",
    cursorclass=pymysql.cursors.DictCursor  # risultati come dict
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM studenti")

for row in cursor:
    print(row)
    
conn.close()
```

---

# ✅ 3️⃣ CRUD completo

## 🔹 INSERT

```python
sql = "INSERT INTO studenti (nome, eta) VALUES (%s, %s)"

cursor.execute(sql, ("Mario", 22))
conn.commit()
```

---

## 🔹 SELECT

```python
cursor.execute("SELECT * FROM studenti")

rows = cursor.fetchall()

for r in rows:
    print(r["nome"], r["eta"])
```

---

## 🔹 UPDATE

```python
cursor.execute(
    "UPDATE studenti SET eta=%s WHERE nome=%s",
    (23, "Mario")
)
conn.commit()
```

---

## 🔹 DELETE

```python
cursor.execute(
    "DELETE FROM studenti WHERE nome=%s",
    ("Mario",)
)
conn.commit()
```

---

# 🔐 4️⃣ Sicurezza (IMPORTANTISSIMO)

Sempre usare placeholder `%s`:

```python
cursor.execute("SELECT * FROM utenti WHERE email=%s", (email,))
```

❌ MAI concatenare stringhe → SQL Injection

---

# ✅ 5️⃣ Versione più pulita con context manager

```python
import pymysql

with pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    database="testdb"
) as conn:
    
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM studenti")
        print(cursor.fetchall())
```

---

# 🧠 6️⃣ Differenze rispetto a SQLite

|                 | PyMySQL + MySQL | SQLite |
| --------------- | --------------- | ------ |
| Server          | ✔               | ❌      |
| Multiutente     | ✔✔✔             | ⚠      |
| Setup           | Medio           | Zero   |
| Performance web | Alta            | Bassa  |

---

# 🚀 7️⃣ Struttura del progetto

Puoi organizzare così:

```
progetto/
│
├── db.py
├── studenti_dao.py
├── main.py
```

### db.py

```python
import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="testdb",
        cursorclass=pymysql.cursors.DictCursor
    )
```

---

### studenti_dao.py

```python
from db import get_connection

def find_all():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM studenti")
            return cursor.fetchall()
```

---

### main.py

```python
from studenti_dao import find_all

for s in find_all():
    print(s)
```

---

# ⭐ Vantaggi di PyMySQL

✔ Nessuna compilazione
✔ Funziona ovunque (anche WSL)
✔ API simile a MySQL classico
✔ Perfetto per esercitazioni

---

# ⚠ Quando NON usarlo

* sistemi ad alte prestazioni
* Django in produzione (meglio mysqlclient)

