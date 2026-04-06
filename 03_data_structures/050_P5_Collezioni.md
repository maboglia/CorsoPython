# 📘 Corso Python – Modulo 5

## Collezioni: liste, tuple, set e dizionari

---

### 1. Liste (`list`)

* Sequenza ordinata e modificabile di elementi.
* Definita con `[]`.

```python
frutta = ["mela", "banana", "pera"]
print(frutta[0])   # mela
print(frutta[-1])  # pera
```

#### Operazioni principali

```python
frutta.append("arancia")   # aggiunge
frutta.remove("banana")    # rimuove
print(len(frutta))         # lunghezza
print(frutta[1:3])         # slicing
frutta.sort()              # ordina
```

---

### 2. Tuple (`tuple`)

* Sequenza ordinata **immutabile**.
* Definita con `()`.

```python
coordinate = (10, 20)
print(coordinate[0])  # 10
```

⚠️ Non si possono modificare gli elementi.

---

### 3. Set (`set`)

* Collezione **non ordinata**, senza duplicati.
* Definita con `{}`.

```python
numeri = {1, 2, 3, 3, 4}
print(numeri)  # {1, 2, 3, 4}
```

#### Operazioni insiemistiche

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # unione {1, 2, 3, 4, 5}
print(a & b)  # intersezione {3}
print(a - b)  # differenza {1, 2}
```

---

### 4. Dizionari (`dict`)

* Collezione di coppie **chiave → valore**.
* Definito con `{}`.

```python
studente = {"nome": "Anna", "età": 21}
print(studente["nome"])   # Anna
```

#### Metodi principali

```python
studente["corso"] = "Informatica"  # aggiunta
print(studente.keys())    # tutte le chiavi
print(studente.values())  # tutti i valori
print(studente.items())   # coppie chiave-valore
```

---

### 5. Iterazione sulle collezioni

```python
lista = [1, 2, 3]
for x in lista:
    print(x)
```

```python
for chiave, valore in studente.items():
    print(chiave, ":", valore)
```

---

### 6. Differenze principali

| Tipo      | Ordinato | Modificabile | Duplicati     | Accesso |
| --------- | -------- | ------------ | ------------- | ------- |
| **list**  | ✅        | ✅            | ✅             | Indice  |
| **tuple** | ✅        | ❌            | ✅             | Indice  |
| **set**   | ❌        | ✅            | ❌             | No      |
| **dict**  | ✅        | ✅            | Chiavi uniche | Chiave  |


