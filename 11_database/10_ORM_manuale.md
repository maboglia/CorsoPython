# Mappare tuple in oggetti: soluzioni manuali

In Python (con `mysql-connector`, `pymysql` o simili) `fetchall()` ti restituisce spesso una `list[tuple]` perché il cursore “normale” lavora in modalità posizionale.


---

## 1) Soluzione migliore: usare `dataclass` + mapping manuale

Esempio:

```python
from dataclasses import dataclass

@dataclass
class Studente:
    id: int
    nome: str
    email: str
```

Query:

```python
cursor.execute("SELECT id, nome, email FROM studenti")
rows = cursor.fetchall()

studenti = [Studente(*row) for row in rows]

print(studenti)
```

Funziona perché `Studente(*row)` prende la tupla e la “spacchetta” nei campi.

⚠️ Attenzione: l’ordine delle colonne deve corrispondere all’ordine dei campi.

---

## 2) Soluzione robusta: trasformare tuple in dict usando `cursor.description`

Così non dipendi dall’ordine:

```python
from dataclasses import dataclass

@dataclass
class Studente:
    id: int
    nome: str
    email: str

cursor.execute("SELECT id, nome, email FROM studenti")
rows = cursor.fetchall()

colonne = [col[0] for col in cursor.description]

studenti = [Studente(**dict(zip(colonne, row))) for row in rows]
```

Qui fai:

* recupero nomi colonne
* zip(nome_colonna, valore)
* creo un dict
* uso `Studente(**dict)` (keyword args)

---

## 3) Soluzione più semplice: usare cursore "dictionary"

Dipende dalla libreria.

### Con `mysql-connector-python`

```python
cursor = conn.cursor(dictionary=True)
cursor.execute("SELECT id, nome, email FROM studenti")
rows = cursor.fetchall()

studenti = [Studente(**row) for row in rows]
```

### Con `pymysql`

```python
cursor = conn.cursor(pymysql.cursors.DictCursor)
```

---

## 4) Soluzione OOP classica (senza dataclass)

```python
class Studente:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

cursor.execute("SELECT id, nome, email FROM studenti")
rows = cursor.fetchall()

studenti = [Studente(*row) for row in rows]
```

---

### Consiglio pratico

Per codice moderno e pulito:
✅ `dataclass` + cursor `dictionary=True` è la combinazione migliore.

