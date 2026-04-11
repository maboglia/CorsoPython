# 📌 Dataclass in Python (`dataclasses`)

Le `dataclass` servono per creare classi “contenitore dati” in modo rapido, evitando di scrivere manualmente `__init__`, `__repr__`, `__eq__`, ecc.

```python
from dataclasses import dataclass

@dataclass
class Studente:
    nome: str
    eta: int
```

Equivale (circa) a scrivere automaticamente:

* costruttore `__init__`
* stampa `__repr__`
* confronto `__eq__`

---

# ✅ Proprietà (campi)

## 1) Campi tipizzati (obbligatori)

```python
@dataclass
class Persona:
    nome: str
    cognome: str
```

Uso:

```python
p = Persona("Mario", "Rossi")
print(p.nome)
```

---

## 2) Campi con valore di default

```python
@dataclass
class Persona:
    nome: str
    eta: int = 18
```

```python
p = Persona("Anna")
print(p.eta)  # 18
```

---

## 3) Campi non inclusi nel costruttore (`init=False`)

```python
from dataclasses import dataclass, field

@dataclass
class Persona:
    nome: str
    cognome: str
    codice: str = field(init=False)

    def __post_init__(self):
        self.codice = self.nome[0] + self.cognome[0]
```

---

## 4) Campi non stampati (`repr=False`)

```python
@dataclass
class Utente:
    username: str
    password: str = field(repr=False)
```

---

## 5) Campi non confrontati (`compare=False`)

```python
@dataclass
class Prodotto:
    nome: str
    prezzo: float
    id_interno: int = field(compare=False)
```

---

## 6) Liste e mutabili: usare `default_factory`

❌ SBAGLIATO:

```python
@dataclass
class Classe:
    studenti: list = []
```

✅ CORRETTO:

```python
@dataclass
class Classe:
    studenti: list = field(default_factory=list)
```

---

# ✅ Proprietà calcolate con `@property`

Le dataclass possono avere proprietà come qualsiasi classe.

```python
@dataclass
class Rettangolo:
    base: float
    altezza: float

    @property
    def area(self):
        return self.base * self.altezza
```

Uso:

```python
r = Rettangolo(5, 2)
print(r.area)  # 10
```

---

# ✅ Metodi in una dataclass

Una dataclass può avere tutti i metodi che vuoi.

```python
@dataclass
class Conto:
    intestatario: str
    saldo: float = 0.0

    def deposita(self, importo: float):
        self.saldo += importo

    def preleva(self, importo: float):
        if importo > self.saldo:
            raise ValueError("Saldo insufficiente")
        self.saldo -= importo
```

---

# ✅ Metodo speciale `__post_init__()`

Serve per eseguire codice dopo l’`__init__` generato automaticamente.

```python
@dataclass
class Studente:
    nome: str
    eta: int

    def __post_init__(self):
        if self.eta < 0:
            raise ValueError("Età non valida")
```

---

# ✅ Ordinamento e confronti

## 1) Confronto automatico (`eq=True` default)

```python
@dataclass
class Punto:
    x: int
    y: int
```

```python
Punto(1,2) == Punto(1,2)  # True
```

---

## 2) Ordinamento (`order=True`)

```python
@dataclass(order=True)
class Studente:
    matricola: int
    nome: str
```

Permette:

```python
Studente(2,"Luca") > Studente(1,"Anna")  # True
```

---

# ✅ Dataclass immutabile (tipo record)

## `frozen=True` (campi non modificabili)

```python
@dataclass(frozen=True)
class Coordinate:
    x: float
    y: float
```

```python
c = Coordinate(1,2)
# c.x = 5  -> ERRORE
```

---

# ✅ Classi con ereditarietà

```python
@dataclass
class Persona:
    nome: str

@dataclass
class Studente(Persona):
    matricola: int
```

---

# ✅ Dataclass e campi privati

```python
@dataclass
class Utente:
    username: str
    _token: str = field(repr=False)
```

---

# 📌 Riepilogo parametri principali `@dataclass`

```python
@dataclass(
    init=True,       # genera __init__
    repr=True,       # genera __repr__
    eq=True,         # genera __eq__
    order=False,     # genera < > <= >=
    frozen=False     # rende immutabile
)
class X:
    ...
```

---

# 📌 Riepilogo parametri principali `field()`

```python
field(
    default=...,           # valore default
    default_factory=...,   # factory per mutabili
    init=True,             # incluso in __init__
    repr=True,             # visibile in stampa
    compare=True,          # usato per confronti
    metadata={}            # info extra
)
```

---

# ⚠️ Nota importante (errore comune)

Se hai **liste, dizionari o set**, usare sempre:

```python
field(default_factory=list)
field(default_factory=dict)
field(default_factory=set)
```

Altrimenti, tutte le istanze condivideranno lo stesso oggetto mutabile!

