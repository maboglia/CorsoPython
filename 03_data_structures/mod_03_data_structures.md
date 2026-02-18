# Modulo 3 – Strutture Dati (12 ore)

Le **strutture dati** permettono di:

* organizzare informazioni
* gestire insiemi di valori
* modellare dati reali

👉 In Python sono **native**, potenti e molto leggibili.

---

## 3.1 Liste (4 ore)

Le **liste** sono:

* ordinate
* modificabili (mutabili)
* possono contenere tipi diversi

### Creazione e accesso

```python
numeri = [1, 2, 3, 4]
nomi = ["Anna", "Luca", "Marco"]
mista = [1, "ciao", True]
```

Accesso:

```python
print(numeri[0])
print(numeri[-1])
```

---

### Manipolazione delle liste

```python
numeri.append(5)
numeri.insert(0, 0)
numeri.remove(3)
ultimo = numeri.pop()
```

Modifica:

```python
numeri[1] = 10
```

---

### Metodi principali delle liste

```python
numeri.sort()
numeri.reverse()
numeri.count(10)
numeri.index(10)
```

⚠️ `sort()` modifica la lista, `sorted()` ne crea una nuova.

---

### Slicing avanzato

```python
numeri = [0, 1, 2, 3, 4, 5]

numeri[1:4]     # [1, 2, 3]
numeri[::2]     # [0, 2, 4]
numeri[::-1]    # lista invertita
```

Assegnazione con slicing:

```python
numeri[1:3] = [20, 30]
```

---

### List comprehension avanzate

```python
quadrati = [x**2 for x in range(10)]
```

Con condizione:

```python
pari = [x for x in range(20) if x % 2 == 0]
```

Con if–else:

```python
etichette = ["pari" if x % 2 == 0 else "dispari" for x in range(10)]
```

⚠️ Da usare con moderazione per mantenere leggibilità.

---

### Liste annidate

```python
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Accesso:

```python
print(matrice[1][2])  # 6
```

Iterazione:

```python
for riga in matrice:
    for valore in riga:
        print(valore)
```

---

## 3.2 Tuple e Set (3 ore)

### Tuple

Le **tuple** sono:

* ordinate
* **immutabili**
* spesso usate per dati fissi

```python
coordinate = (10, 20)
```

Accesso:

```python
print(coordinate[0])
```

---

### Unpacking

```python
x, y = coordinate
print(x, y)
```

Molto usato in:

```python
for indice, valore in enumerate(lista):
    ...
```

---

### Set

I **set** sono:

* non ordinati
* senza duplicati
* molto veloci nei controlli

```python
numeri = {1, 2, 3, 3, 4}
print(numeri)  # duplicati rimossi
```

---

### Operazioni insiemistiche

```python
a = {1, 2, 3}
b = {3, 4, 5}

a | b   # unione
a & b   # intersezione
a - b   # differenza
```

---

### Frozenset

Versione **immutabile** del set.

```python
f = frozenset([1, 2, 3])
```

Usata quando:

* serve un set come chiave
* i dati non devono cambiare

---

### Quando usare cosa

| Struttura | Quando usarla                         |
| --------- | ------------------------------------- |
| Lista     | dati ordinati e modificabili          |
| Tupla     | dati fissi                            |
| Set       | eliminare duplicati, controlli rapidi |

---

## 3.3 Dizionari (5 ore)

I **dizionari** rappresentano:

* coppie chiave → valore
* strutture tipo JSON
* record e oggetti

---

### Creazione e accesso

```python
studente = {
    "nome": "Mario",
    "eta": 20,
    "corso": "Python"
}
```

Accesso:

```python
print(studente["nome"])
```

Metodo sicuro:

```python
print(studente.get("email", "non presente"))
```

---

### Modifica e aggiunta

```python
studente["eta"] = 21
studente["email"] = "mario@mail.it"
```

---

### Metodi principali

```python
studente.keys()
studente.values()
studente.items()
studente.pop("email")
```

---

### Iterazione sui dizionari

```python
for chiave in studente:
    print(chiave, studente[chiave])
```

Forma consigliata:

```python
for chiave, valore in studente.items():
    print(chiave, valore)
```

---

### Dictionary comprehension

```python
quadrati = {x: x**2 for x in range(5)}
```

Con condizione:

```python
pari = {x: x for x in range(10) if x % 2 == 0}
```

---

### `defaultdict` e `Counter`

```python
from collections import defaultdict, Counter
```

**defaultdict**

```python
voti = defaultdict(int)
voti["matematica"] += 1
```

**Counter**

```python
testo = "python"
conteggio = Counter(testo)
print(conteggio)
```

---

## Riepilogo didattico

Questo modulo permette di:

* modellare dati reali
* leggere JSON e CSV (moduli successivi)
* scrivere programmi più strutturati

È il ponte verso:

* funzioni
* file
* OOP
* basi dati

---

