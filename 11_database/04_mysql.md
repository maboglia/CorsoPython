# 🐍 Python + 🐬 MySQL

## 1️⃣ Driver principali per Python

Per collegare Python a MySQL servono librerie (driver):

### 🔹 `mysql-connector-python`

* Driver ufficiale Oracle
* Puro Python
* Facile da usare

Installazione:

```bash
pip install mysql-connector-python
```

### 🔹 `PyMySQL`

* Puro Python
* Molto usato in ambiente web

```bash
pip install pymysql
```

### 🔹 `mysqlclient`

* Wrapper C (più veloce)
* Usato spesso con Django

```bash
pip install mysqlclient
```

---

# 2️⃣ Connessione base con mysql-connector

```python
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="testdb"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM studenti")

for row in cursor:
    print(row)

cursor.close()
conn.close()
```

---

# 3️⃣ Esempio CRUD completo

## 🔹 INSERT

```python
sql = "INSERT INTO studenti (nome, eta) VALUES (%s, %s)"
val = ("Mario", 22)

cursor.execute(sql, val)
conn.commit()
```

⚠ Importante: sempre `commit()` per salvare.

---

## 🔹 SELECT con fetch

```python
cursor.execute("SELECT * FROM studenti")

rows = cursor.fetchall()

for r in rows:
    print(r[0], r[1])
```

---

## 🔹 UPDATE

```python
sql = "UPDATE studenti SET eta=%s WHERE nome=%s"
cursor.execute(sql, (23, "Mario"))
conn.commit()
```

---

## 🔹 DELETE

```python
sql = "DELETE FROM studenti WHERE nome=%s"
cursor.execute(sql, ("Mario",))
conn.commit()
```

---

# 4️⃣ Gestione sicura (SQL Injection)

Usare sempre i placeholder `%s`:

```python
cursor.execute("SELECT * FROM utenti WHERE email=%s", (email_input,))
```

❌ MAI:

```python
cursor.execute("SELECT * FROM utenti WHERE email='" + email_input + "'")
```

---

# 5️⃣ Transazioni

```python
try:
    conn.start_transaction()

    cursor.execute("INSERT ...")
    cursor.execute("UPDATE ...")

    conn.commit()

except:
    conn.rollback()
```

---

# 6️⃣ Uso con ORM (livello avanzato)

Se vuoi qualcosa di più strutturato:

### 🔹 SQLAlchemy

* ORM professionale
* Simile a JPA/Hibernate
* Supporta MySQL, SQLite, PostgreSQL

Installazione:

```bash
pip install sqlalchemy pymysql
```

Esempio base:

```python
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:password@localhost/testdb")

with engine.connect() as conn:
    result = conn.execute("SELECT * FROM studenti")
    for row in result:
        print(row)
```

---

# 7️⃣ Quando usare MySQL con Python?

✅ Applicazioni web (Flask, Django)
✅ Backend REST API
✅ Applicazioni enterprise
✅ Sistemi multiutente

---

# 8️⃣ Confronto rapido: Python + MySQL vs SQLite

|                | MySQL      | SQLite   |
| -------------- | ---------- | -------- |
| Server         | Necessario | No       |
| Multiutente    | Ottimo     | Limitato |
| Produzione web | ✔          | ❌        |
| Setup          | Medio      | Zero     |

