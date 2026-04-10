# Esempi progressivi NumPy (da livello base → avanzato)

NumPy è la libreria fondamentale per:

* calcolo numerico veloce
* vettori e matrici (array n-dimensionali)
* algebra lineare, statistica, simulazioni

Installazione:

```bash
pip install numpy
```

Import:

```python
import numpy as np
```

---

# LIVELLO 1 — BASE (array 1D)

## 1) Creare un array

```python
import numpy as np

a = np.array([10, 20, 30, 40])
print(a)
print(type(a))
```

---

## 2) Proprietà fondamentali

```python
print(a.shape)   # dimensioni
print(a.ndim)    # numero dimensioni
print(a.dtype)   # tipo dati
print(a.size)    # numero elementi
```

---

## 3) Accesso e slicing

```python
print(a[0])      # primo elemento
print(a[-1])     # ultimo elemento
print(a[1:3])    # slicing
```

---

# LIVELLO 2 — ARRAY GENERATI AUTOMATICAMENTE

## 4) Array di zeri, uni, valori costanti

```python
z = np.zeros(5)
u = np.ones(5)
c = np.full(5, 7)

print(z)
print(u)
print(c)
```

---

## 5) Sequenze numeriche (arange, linspace)

```python
x = np.arange(0, 10, 2)       # 0,2,4,6,8
y = np.linspace(0, 1, 5)      # 5 valori tra 0 e 1

print(x)
print(y)
```

---

# LIVELLO 3 — ARRAY 2D (matrici)

## 6) Matrice 2D

```python
m = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(m)
print(m.shape)
```

---

## 7) Accesso a righe e colonne

```python
print(m[0, 0])    # elemento (riga0,col0)
print(m[1, 2])    # elemento (riga1,col2)

print(m[0])       # prima riga
print(m[:, 1])    # seconda colonna
```

---

# LIVELLO 4 — OPERAZIONI VETTORIALI

## 8) Operazioni elemento per elemento

```python
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print(a + b)
print(a * b)
print(a - b)
```

---

## 9) Operazioni con scalare

```python
print(a * 2)
print(a + 5)
```

📌 NumPy è veloce perché evita i cicli `for` (calcolo vettoriale).

---

# LIVELLO 5 — FUNZIONI MATEMATICHE E STATISTICHE

## 10) Funzioni matematiche

```python
a = np.array([1, 4, 9, 16])

print(np.sqrt(a))
print(np.log(a))
print(np.sin(a))
```

---

## 11) Statistiche base

```python
a = np.array([10, 20, 30, 40])

print(np.mean(a))
print(np.sum(a))
print(np.min(a))
print(np.max(a))
print(np.std(a))
```

---

# LIVELLO 6 — BOOLEAN MASK (filtri)

## 12) Filtrare con condizioni

```python
a = np.array([10, 5, 30, 2, 50])

mask = a > 10
print(mask)

print(a[mask])
```

Forma compatta:

```python
print(a[a > 10])
```

---

# LIVELLO 7 — BROADCASTING (concetto fondamentale)

## 13) Sommare vettore a matrice

```python
m = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

v = np.array([10, 20, 30])

print(m + v)
```

📌 Broadcasting = NumPy “adatta” le dimensioni automaticamente.

---

# LIVELLO 8 — RESHAPE E FLATTEN

## 14) Cambiare forma a un array

```python
a = np.arange(12)
m = a.reshape(3, 4)

print(a)
print(m)
```

---

## 15) Flatten (matrice → vettore)

```python
v = m.flatten()
print(v)
```

---

# LIVELLO 9 — CONCATENAZIONE E SPLIT

## 16) Concatenare array

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = np.concatenate([a, b])
print(c)
```

---

## 17) Concatenare matrici per righe o colonne

```python
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])

print(np.concatenate([m1, m2], axis=0))  # righe
print(np.concatenate([m1, m2], axis=1))  # colonne
```

---

# LIVELLO 10 — INDICIZZAZIONE AVANZATA

## 18) Fancy indexing

```python
a = np.array([10, 20, 30, 40, 50])

print(a[[0, 2, 4]])   # prende elementi in posizioni 0,2,4
```

---

## 19) Selezione multipla su matrice

```python
m = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(m[[0, 2], [1, 2]])  # (0,1) e (2,2)
```

---

# LIVELLO 11 — ALGEBRA LINEARE

## 20) Prodotto scalare (dot product)

```python
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print(np.dot(a, b))
```

Oppure:

```python
print(a @ b)
```

---

## 21) Prodotto tra matrici

```python
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[10, 20],
              [30, 40]])

print(A @ B)
```

---

## 22) Determinante e inversa

```python
A = np.array([[1, 2],
              [3, 4]])

det = np.linalg.det(A)
inv = np.linalg.inv(A)

print(det)
print(inv)
```

---

# LIVELLO 12 — SISTEMI LINEARI

## 23) Risolvere Ax = b

```python
A = np.array([[2, 1],
              [5, 3]])

b = np.array([8, 18])

x = np.linalg.solve(A, b)

print(x)
```

📌 Utile in economia, fisica, modelli di regressione.

---

# LIVELLO 13 — GENERAZIONE NUMERI CASUALI (simulazioni)

## 24) Random base

```python
np.random.seed(0)

a = np.random.randint(1, 11, size=10)
print(a)
```

---

## 25) Distribuzione normale

```python
x = np.random.normal(loc=0, scale=1, size=1000)
print(x.mean(), x.std())
```

---

# LIVELLO 14 — STATISTICA SU ASSI (axis)

## 26) Somme e medie su righe/colonne

```python
m = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(np.sum(m))         # somma totale
print(np.sum(m, axis=0)) # somma colonne
print(np.sum(m, axis=1)) # somma righe

print(np.mean(m, axis=0))
print(np.mean(m, axis=1))
```

---

# LIVELLO 15 — FUNZIONI UTILI (sort, unique, where)

## 27) Ordinamento

```python
a = np.array([30, 10, 20])
print(np.sort(a))
```

---

## 28) Valori unici

```python
a = np.array([1, 2, 2, 3, 3, 3])
print(np.unique(a))
```

---

## 29) where (if vettoriale)

```python
a = np.array([5, 8, 3, 10])

b = np.where(a >= 6, "OK", "KO")
print(b)
```

---

# LIVELLO 16 — PERFORMANCE (vettorializzazione vs ciclo)

## 30) Caso tipico

```python
a = np.arange(1_000_000)

b = a * 2 + 5   # vettoriale, molto veloce
print(b[:5])
```

📌 NumPy è progettato per calcoli su milioni di dati.

---

# LIVELLO 17 — MINI-PROGETTO (analisi dati simulati)

## 31) Simulazione voti studenti e analisi

```python
np.random.seed(1)

voti = np.random.randint(1, 11, size=(5, 4))  # 5 studenti, 4 materie
print(voti)

media_studente = np.mean(voti, axis=1)
media_materia = np.mean(voti, axis=0)

print("Media per studente:", media_studente)
print("Media per materia:", media_materia)

migliore = np.argmax(media_studente)
print("Studente migliore indice:", migliore)
```

---

# LIVELLO 18 — NUMPY + PANDAS (integrazione reale)

## 32) Da NumPy a Pandas

```python
import pandas as pd

np.random.seed(0)
voti = np.random.randint(1, 11, size=(4, 3))

df = pd.DataFrame(voti, columns=["Matematica", "Informatica", "Inglese"])
df["Media"] = df.mean(axis=1)

print(df)
```

---

# RIASSUNTO CONCETTI IMPORTANTI

### Fondamentali

* `np.array()`
* slicing `a[1:5]`
* `shape`, `ndim`, `dtype`
* operazioni vettoriali

### Intermedi

* `reshape()`
* `axis=0 / axis=1`
* maschere booleane
* broadcasting

### Avanzati

* `np.linalg` (algebra lineare)
* `solve`, `det`, `inv`
* random e simulazioni
* performance e vettorializzazione

