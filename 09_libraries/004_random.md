# 📌 Libreria `random` in Python – Scheda Completa

La libreria standard **`random`** serve per generare numeri casuali e fare operazioni random su liste, stringhe, estrazioni, shuffle, simulazioni.

📌 Modulo incluso in Python → non serve installare nulla.

```python
import random
```

⚠️ Attenzione: `random` NON è adatto per sicurezza (password, crittografia).
Per quello usare `secrets`.

---

# 1) Generare numeri casuali float

### Numero casuale tra 0 e 1

```python
random.random()
```

Esempio:

```python
x = random.random()
print(x)   # es: 0.73456
```

---

# 2) Numeri casuali interi (`randint`)

### Intero tra a e b (inclusi)

```python
random.randint(1, 10)
```

📌 Include sia 1 che 10.

---

# 3) Intero casuale con step (`randrange`)

```python
random.randrange(start, stop, step)
```

Esempi:

```python
random.randrange(1, 10)      # 1..9
random.randrange(0, 100, 5)  # multipli di 5 tra 0 e 95
```

📌 stop NON incluso.

---

# 4) Float casuale in un intervallo (`uniform`)

```python
random.uniform(1.5, 5.5)
```

📌 Restituisce float tra 1.5 e 5.5 (estremi inclusi in modo teorico).

---

# 5) Scelta casuale da una lista (`choice`)

```python
nomi = ["Mario", "Anna", "Luca", "Sara"]
print(random.choice(nomi))
```

📌 Estrae un solo elemento.

---

# 6) Estrazione casuale di più elementi (`sample`)

```python
nomi = ["Mario", "Anna", "Luca", "Sara"]

estratti = random.sample(nomi, 2)
print(estratti)
```

📌 Restituisce una lista di elementi distinti (senza ripetizione).

---

# 7) Estrazione casuale con ripetizione (`choices`)

```python
nomi = ["Mario", "Anna", "Luca"]

estratti = random.choices(nomi, k=5)
print(estratti)
```

📌 Può ripetere elementi.

---

# 8) Estrazione con pesi (`weights`)

```python
nomi = ["Mario", "Anna", "Luca"]

estratti = random.choices(nomi, weights=[0.1, 0.7, 0.2], k=10)
print(estratti)
```

📌 Anna ha probabilità più alta.

---

# 9) Mischiare una lista (`shuffle`)

```python
numeri = [1, 2, 3, 4, 5]
random.shuffle(numeri)

print(numeri)
```

📌 modifica la lista originale (in-place).

---

# 10) Generare un boolean casuale

```python
random.choice([True, False])
```

Oppure:

```python
random.random() < 0.5
```

---

# 11) Lanciare una moneta (testa/croce)

```python
random.choice(["Testa", "Croce"])
```

---

# 12) Simulare un dado

```python
dado = random.randint(1, 6)
print(dado)
```

---

# 13) Seed (ripetibilità esperimenti)

### Impostare seed

```python
random.seed(10)
print(random.randint(1, 100))
```

📌 Con lo stesso seed, la sequenza sarà sempre uguale.

Utile per test e debug.

---

# 14) Funzioni principali della libreria

| Funzione           | Descrizione                  |
| ------------------ | ---------------------------- |
| `random()`         | float tra 0 e 1              |
| `randint(a,b)`     | intero tra a e b (inclusi)   |
| `randrange(a,b,s)` | intero con step              |
| `uniform(a,b)`     | float tra a e b              |
| `choice(seq)`      | 1 elemento casuale           |
| `choices(seq,k=n)` | n elementi con ripetizione   |
| `sample(seq,k=n)`  | n elementi senza ripetizione |
| `shuffle(seq)`     | mescola lista                |
| `seed(x)`          | imposta seme casuale         |

---

# 15) Distribuzioni statistiche (avanzato)

### Distribuzione normale (Gauss)

```python
random.gauss(mu=0, sigma=1)
```

Esempio:

```python
x = random.gauss(10, 2)  # media 10, deviazione 2
print(x)
```

---

### Distribuzione normale alternativa

```python
random.normalvariate(mu, sigma)
```

---

### Distribuzione esponenziale

```python
random.expovariate(lambd)
```

Esempio:

```python
random.expovariate(1/10)  # media 10
```

---

### Distribuzione uniforme discreta

```python
random.triangular(low, high, mode)
```

Esempio:

```python
random.triangular(0, 10, 3)
```

---

# 16) Numeri casuali in una lista (esempio pratico)

```python
import random

numeri = [random.randint(1, 100) for _ in range(10)]
print(numeri)
```

---

# 17) Generare password semplice (NON sicura)

```python
import random
import string

caratteri = string.ascii_letters + string.digits
pwd = "".join(random.choice(caratteri) for _ in range(8))

print(pwd)
```

⚠️ NON adatto per sicurezza reale.

Per password vere usare `secrets`.

---

# 18) Libreria `secrets` (per sicurezza)

Esempio corretto:

```python
import secrets
import string

caratteri = string.ascii_letters + string.digits
pwd = "".join(secrets.choice(caratteri) for _ in range(12))
print(pwd)
```

---

# 19) Esempio completo: estrazione Lotto (5 numeri su 90)

```python
import random

estrazione = random.sample(range(1, 91), 5)
estrazione.sort()

print("Estrazione:", estrazione)
```

---

# 20) Esempio: generare numeri senza duplicati

```python
import random

numeri = random.sample(range(1, 11), 10)
print(numeri)
```

📌 genera una permutazione di 1..10.

---

# 21) Esempio: gioco "Indovina il numero"

```python
import random

numero = random.randint(1, 100)

while True:
    tentativo = int(input("Indovina (1-100): "))

    if tentativo < numero:
        print("Troppo piccolo!")
    elif tentativo > numero:
        print("Troppo grande!")
    else:
        print("Bravo! Hai indovinato!")
        break
```

---

# 22) Errori tipici

### ❌ `randrange(1,10)` produce 10?

No, produce 1..9.

### ❌ `shuffle()` restituisce lista?

No, modifica la lista e restituisce `None`.

```python
lista = [1,2,3]
print(random.shuffle(lista))  # None
```

---

# 23) Best practice

✅ usare `sample()` se non vuoi ripetizioni
✅ usare `choices()` se vuoi ripetizioni
✅ usare `seed()` per debug e test
✅ usare `secrets` per password e token
✅ `shuffle()` solo su liste mutabili

---

# 24) Mini riepilogo rapido

📌 Estrarre un elemento:

```python
random.choice(lista)
```

📌 Estrarre N distinti:

```python
random.sample(lista, k=N)
```

📌 Estrarre N con ripetizione:

```python
random.choices(lista, k=N)
```

📌 Numero casuale intero:

```python
random.randint(a, b)
```

📌 Mescolare lista:

```python
random.shuffle(lista)
```
