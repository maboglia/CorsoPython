# Modulo 9 – Librerie Standard Essenziali (6 ore)

La **standard library** di Python è uno dei suoi punti di forza:

* ricca
* coerente
* pronta all’uso

👉 Spesso **non serve installare nulla** per fare cose molto potenti.

---

## `datetime` – Gestione di date e orari

Serve per:

* date
* orari
* differenze temporali

```python
from datetime import date, datetime
```

Data corrente:

```python
oggi = date.today()
print(oggi)
```

Data e ora:

```python
adesso = datetime.now()
print(adesso)
```

---

### Formattazione

```python
print(adesso.strftime("%d/%m/%Y %H:%M"))
```

Parsing:

```python
data = datetime.strptime("10-02-2026", "%d-%m-%Y")
```

---

### Differenze temporali

```python
from datetime import timedelta

scadenza = oggi + timedelta(days=7)
```

---

## `os` e `sys` – Interazione con il sistema

### `os`

```python
import os

print(os.getcwd())
os.mkdir("nuova_cartella")
```

Verifica file:

```python
os.path.exists("file.txt")
```

---

### `sys`

Argomenti da linea di comando:

```python
import sys

print(sys.argv)
```

Uscita dal programma:

```python
sys.exit()
```

👉 Fondamentale per script e CLI.

---

## `collections` – Strutture dati avanzate

### `defaultdict`

```python
from collections import defaultdict

contatori = defaultdict(int)
contatori["a"] += 1
```

---

### `Counter`

```python
from collections import Counter

testo = "python"
print(Counter(testo))
```

---

### `namedtuple`

```python
from collections import namedtuple

Punto = namedtuple("Punto", ["x", "y"])
p = Punto(3, 4)
```

---

## `itertools` – Iterazione efficiente

```python
import itertools
```

Esempi comuni:

```python
itertools.count(1)
itertools.cycle([1, 2, 3])
```

Combinazioni:

```python
list(itertools.combinations([1, 2, 3], 2))
```

👉 Ottimo per:

* combinatoria
* simulazioni
* grandi sequenze

---

## `re` – Espressioni regolari (base)

```python
import re
```

Verifica:

```python
email = "test@mail.com"
if re.match(r".+@.+\..+", email):
    print("Email valida")
```

Ricerca:

```python
re.findall(r"\d+", "abc123xyz")
```

Sostituzione:

```python
re.sub(r"\s+", "_", "ciao mondo python")
```

👉 Introdurre come **strumento**, non come teoria pura.

---

## `random` – Numeri casuali

```python
import random
```

Numero casuale:

```python
random.randint(1, 10)
```

Scelta casuale:

```python
random.choice(["rosso", "verde", "blu"])
```

Mescolare:

```python
random.shuffle(lista)
```

---

## Riepilogo didattico

Questo modulo permette di:

* scrivere script completi
* interagire col sistema
* usare strutture avanzate
* lavorare con date, testo e dati

È il **kit di sopravvivenza Python**.

