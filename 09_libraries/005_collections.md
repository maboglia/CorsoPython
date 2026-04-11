# 5. Modulo `collections`: Strutture dati "Speciali"

Questo è un modulo per un livello intermedio, ottimo per mostrare come scrivere codice più pulito.

* **`Counter`**: Perfetto per esercizi di analisi del testo (es. "conta quante volte appare ogni parola").
* **`defaultdict`**: Risolve il fastidioso errore `KeyError`. Se cerchi una chiave che non esiste, la crea lui con un valore di default (es. 0 o una lista vuota).
* **`namedtuple`**: Per creare oggetti leggeri senza dover scrivere una classe intera.

---

```python
from collections import Counter, defaultdict, namedtuple

# Counter - conteggio elementi
parole = ["mela", "banana", "mela", "arancia", "banana", "mela"]
conteggio = Counter(parole)
print(conteggio)  # Counter({'mela': 3, 'banana': 2, 'arancia': 1})
print(conteggio.most_common(2))  # I 2 elementi più comuni

# defaultdict - dizionario con valore predefinito
gruppi = defaultdict(list)
studenti = [("Mario", "A"), ("Lucia", "B"), ("Paolo", "A"), ("Anna", "B")]

for nome, classe in studenti:
    gruppi[classe].append(nome)

# namedtuple - tupla con nomi
Punto = namedtuple("Punto", ["x", "y"])
p1 = Punto(3, 4)
print(f"Coordinate: x={p1.x}, y={p1.y}")
```

---

# 📌 Libreria `collections` – Scheda Completa

`collections` contiene strutture dati avanzate (oltre a list/dict).

```python
import collections
```

Oppure import mirati:

```python
from collections import Counter, defaultdict, deque, namedtuple
```

---

## 1) `Counter` (conteggio frequenze)

Serve per contare elementi in una lista/stringa.

```python
from collections import Counter

lettere = Counter("banana")
print(lettere)
```

Output:

```python
Counter({'a': 3, 'n': 2, 'b': 1})
```

Accesso:

```python
print(lettere["a"])   # 3
```

Elementi più comuni:

```python
print(lettere.most_common(2))
```

Output:

```python
[('a', 3), ('n', 2)]
```

Somma e sottrazione Counter:

```python
c1 = Counter("banana")
c2 = Counter("ananas")

print(c1 + c2)
print(c1 - c2)
```

---

## 2) `defaultdict` (dizionario con valore default)

Evita `KeyError` e semplifica codice.

```python
from collections import defaultdict

d = defaultdict(int)

d["a"] += 1
d["b"] += 5

print(d)
```

📌 `int` produce valore default `0`.

Esempio lista come default:

```python
d = defaultdict(list)

d["classeA"].append("Mario")
d["classeA"].append("Anna")

print(d)
```

---

## 3) `deque` (coda efficiente)

Più efficiente di list per inserimenti in testa/coda.

```python
from collections import deque

coda = deque([1, 2, 3])
coda.append(4)        # aggiunge in coda
coda.appendleft(0)    # aggiunge in testa

print(coda)
```

Rimozione:

```python
coda.pop()        # rimuove ultimo
coda.popleft()    # rimuove primo
```

Rotazione:

```python
coda.rotate(1)    # ruota a destra
coda.rotate(-1)   # ruota a sinistra
```

---

## 4) `namedtuple` (record immutabili)

Simile a una classe semplice.

```python
from collections import namedtuple

Studente = namedtuple("Studente", ["nome", "eta"])

s = Studente("Mario", 20)

print(s.nome)
print(s.eta)
```

📌 è immutabile (non modificabile).

---

## 5) `OrderedDict` (ordine garantito)

Oggi (Python 3.7+) anche i dict normali mantengono ordine, quindi è meno usato.

```python
from collections import OrderedDict
```

---

## 6) `ChainMap` (unire dizionari senza copiarli)

```python
from collections import ChainMap

d1 = {"a": 1, "b": 2}
d2 = {"b": 20, "c": 30}

cm = ChainMap(d1, d2)
print(cm["b"])  # prende da d1 (prima mappa)
```

---

## 7) `UserDict`, `UserList`, `UserString`

Classi base per creare strutture personalizzate.

---

## Best practice collections

✅ `Counter` per frequenze
✅ `defaultdict` per raggruppamenti
✅ `deque` per code FIFO/LIFO
✅ `namedtuple` per record leggeri

