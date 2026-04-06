# ORM

Flask (in realtà `json.dumps`) non sa come convertire automaticamente un tuo oggetto Python (es. `Studente`) in JSON.

Devi trasformarlo in **dict** prima di restituirlo.

---

## Soluzione consigliata: `dataclass` + `asdict()`

```python
from dataclasses import dataclass, asdict
from flask import jsonify

@dataclass
class Studente:
    id: int
    nome: str
    email: str
```

Poi nel controller Flask:

```python
@app.get("/studenti")
def get_studenti():
    cursor.execute("SELECT id, nome, email FROM studenti")
    rows = cursor.fetchall()

    studenti = [Studente(*row) for row in rows]

    return jsonify([asdict(s) for s in studenti])
```

---

## Se hai usato cursore `dictionary=True`

Allora è ancora più semplice, perché hai già dizionari:

```python
cursor = conn.cursor(dictionary=True)

@app.get("/studenti")
def get_studenti():
    cursor.execute("SELECT id, nome, email FROM studenti")
    rows = cursor.fetchall()  # lista di dict

    return jsonify(rows)
```

---

## Se NON usi dataclass: metodo `to_dict()`

```python
class Studente:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email
        }
```

Controller:

```python
return jsonify([s.to_dict() for s in studenti])
```

---

## Trucco veloce (ma meno pulito)

```python
return jsonify([s.__dict__ for s in studenti])
```

Funziona se l’oggetto contiene solo attributi semplici.

---

### Nota importante

Se dentro hai tipi non serializzabili (es. `datetime`, `Decimal`) devi convertirli (stringa o float), altrimenti Flask darà lo stesso errore.

---

## dataclass

Le **dataclass** (modulo `dataclasses`, Python 3.7+) servono per creare classi “porta-dati” (DTO / Model semplici) senza scrivere tutto il codice ripetitivo.

In pratica ti evitano di scrivere manualmente:

* `__init__`
* `__repr__`
* `__eq__`
* metodi di confronto
* gestione default dei campi

---

## 1) Esempio base

Senza dataclass:

```python
class Studente:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email
```

Con dataclass:

```python
from dataclasses import dataclass

@dataclass
class Studente:
    id: int
    nome: str
    email: str
```

Python genera automaticamente il costruttore:

```python
s = Studente(1, "Mario", "mario@gmail.com")
print(s)
```

Output:

```
Studente(id=1, nome='Mario', email='mario@gmail.com')
```

---

## 2) Tipi e vantaggi

Le annotazioni (`id: int`, `nome: str`) non obbligano Python a controllare i tipi runtime, però:

* rendono il codice più leggibile
* aiutano gli IDE (PyCharm, VSCode)
* permettono strumenti di validazione / type checking (mypy)

---

## 3) Default values

```python
from dataclasses import dataclass

@dataclass
class Studente:
    id: int
    nome: str
    email: str = ""
```

Ora puoi creare:

```python
s = Studente(1, "Mario")
```

---

## 4) Campi opzionali (`None`)

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class Studente:
    id: int
    nome: str
    email: Optional[str] = None
```

---

## 5) Conversione in JSON (fondamentale con Flask)

Un oggetto dataclass non è JSON serializzabile direttamente, ma puoi convertirlo in dizionario con `asdict()`:

```python
from dataclasses import asdict

s = Studente(1, "Mario", "mario@gmail.com")

d = asdict(s)
print(d)
```

Output:

```python
{'id': 1, 'nome': 'Mario', 'email': 'mario@gmail.com'}
```

Poi con Flask:

```python
from flask import jsonify

return jsonify(asdict(s))
```

Oppure lista:

```python
return jsonify([asdict(x) for x in studenti])
```

---

## 6) `field()` per liste e default mutabili

⚠️ Errore tipico: mai mettere liste vuote come default diretto.

Sbagliato:

```python
@dataclass
class Classe:
    studenti: list = []   # NO
```

Giusto:

```python
from dataclasses import dataclass, field

@dataclass
class Classe:
    studenti: list = field(default_factory=list)
```

Perché ogni oggetto deve avere la sua lista separata.

---

## 7) Rendere l’oggetto immutabile (`frozen=True`)

Se vuoi un DTO che non possa essere modificato:

```python
@dataclass(frozen=True)
class Studente:
    id: int
    nome: str
    email: str
```

Ora questo dà errore:

```python
s.nome = "Luigi"
```

Utile se vuoi oggetti “read-only” (molto usato nei DTO).

---

## 8) Personalizzare campi esclusi da init o repr

Esempio: un campo calcolato o tecnico.

```python
from dataclasses import dataclass, field

@dataclass
class Studente:
    id: int
    nome: str
    email: str
    password_hash: str = field(repr=False)  # non appare nel print
```

---

## 9) `__post_init__` (validazioni dopo init)

Se vuoi controllare dati appena creato l’oggetto:

```python
from dataclasses import dataclass

@dataclass
class Studente:
    id: int
    nome: str
    email: str

    def __post_init__(self):
        if self.id <= 0:
            raise ValueError("ID non valido")
```

---

# Collegamento diretto con MySQL fetchall()

Esempio pratico:

```python
cursor.execute("SELECT id, nome, email FROM studenti")
rows = cursor.fetchall()

studenti = [Studente(*row) for row in rows]
```

Poi per Flask JSON:

```python
return jsonify([asdict(s) for s in studenti])
```

---

## In sintesi

Le dataclass sono perfette quando vuoi creare oggetti tipo **DTO / Entity leggere**, soprattutto quando lavori con database e API REST.
