# I moduli dipendenti

**in Python quando importi un modulo vengono eseguiti anche gli `import` presenti al suo interno**. Questo significa che **i moduli che quel modulo importa vengono caricati in memoria**, ma **non vengono automaticamente importati nel tuo namespace**.

Vediamo bene le due conseguenze.

---

## 1️⃣ I moduli dipendenti vengono caricati

Se hai questa struttura:

**modulo_b.py**

```python
import math

def radice(x):
    return math.sqrt(x)
```

**main.py**

```python
import modulo_b

print(modulo_b.radice(9))
```

Quando esegui `main.py`:

1. Python importa `modulo_b`
2. Durante l'import di `modulo_b`, viene eseguito anche `import math`
3. Quindi **math viene caricato**

---

## 2️⃣ Ma non è disponibile direttamente nel tuo file

Nel file `main.py` **math non è visibile direttamente**.

Questo NON funziona:

```python
import modulo_b

print(math.sqrt(9))   # ERRORE
```

Errore:

```
NameError: name 'math' is not defined
```

Per usarlo devi importarlo anche tu:

```python
import math
import modulo_b
```

---

## 3️⃣ Però è accessibile tramite il modulo

Se il modulo lo espone, puoi accedervi così:

```python
import modulo_b

print(modulo_b.math.sqrt(9))
```

Perché `math` è una variabile globale dentro `modulo_b`.

---

## 4️⃣ Riassunto

Quando fai:

```python
import modulo_a
```

succede che:

| Cosa succede                                    | Risultato |
| ----------------------------------------------- | --------- |
| Gli `import` dentro `modulo_a` vengono eseguiti | ✅ sì      |
| I moduli importati vengono caricati             | ✅ sì      |
| Diventano visibili nel tuo file                 | ❌ no      |
| Sono accessibili tramite `modulo_a.nome`        | ✅ sì      |

---

## 5️⃣ Nota importante: caching

Python **non ricarica lo stesso modulo due volte**.

Se:

```python
import modulo_a
import modulo_b
```

e **entrambi importano `math`**, Python lo carica **una sola volta** (grazie a `sys.modules`).

---

## Casi particolari

Ci sono **alcuni casi particolari negli `import` di Python** che spesso creano confusione anche a programmatori esperti. I tre più importanti riguardano:

1. `from modulo import *`
2. **import circolari**
3. differenza tra `import modulo` e `from modulo import funzione`

---

# 1️⃣ `from modulo import *`

Questo import **porta tutti i nomi pubblici del modulo direttamente nel namespace corrente**.

### Esempio

**modulo.py**

```python
x = 10

def saluta():
    print("ciao")
```

**main.py**

```python
from modulo import *

print(x)
saluta()
```

Funziona perché **tutti i simboli vengono importati nel file corrente**.

---

### Problema principale: collisioni

Se due moduli hanno lo stesso nome di funzione:

```python
from modulo1 import *
from modulo2 import *
```

se entrambi hanno:

```python
def calcola():
```

la seconda **sovrascrive la prima**.

Questo rende il codice:

* difficile da leggere
* difficile da debuggare

Per questo motivo **PEP8 sconsiglia fortemente `import *`**.

Uso consigliato:

```python
import modulo
modulo.saluta()
```

oppure:

```python
from modulo import saluta
```

---

# 2️⃣ Import circolari

Succede quando **due moduli si importano a vicenda**.

### Esempio

**a.py**

```python
import b

def funzione_a():
    print("A")
```

**b.py**

```python
import a

def funzione_b():
    print("B")
```

Quando Python esegue:

```
import a
```

succede:

1. Python carica `a`
2. `a` importa `b`
3. `b` prova a importare `a`
4. ma `a` **non è ancora completamente inizializzato**

Questo può produrre errori come:

```
ImportError: cannot import name ...
```

---

### Soluzioni comuni

**1️⃣ Spostare l'import dentro la funzione**

```python
def funzione():
    import b
```

**2️⃣ Creare un terzo modulo comune**

```
a.py
b.py
common.py
```

---

# 3️⃣ Differenza tra `import modulo` e `from modulo import funzione`

Questa differenza è **fondamentale per capire i namespace**.

---

## Caso 1

```python
import math

math.sqrt(9)
```

Il modulo rimane **incapsulato nel suo namespace**.

---

## Caso 2

```python
from math import sqrt

sqrt(9)
```

Qui **la funzione viene copiata nel namespace corrente**.

---

## Effetto importante con le modifiche

Supponiamo:

**modulo.py**

```python
valore = 10
```

---

### Caso A

```python
import modulo

print(modulo.valore)
```

Se `modulo.valore` cambia, tu lo vedi.

---

### Caso B

```python
from modulo import valore
```

Qui `valore` è **una copia del riferimento al momento dell'import**.

Se nel modulo succede:

```python
valore = 20
```

il tuo `valore` **non cambia automaticamente**.

---

# 📌 Riassunto

| Tipo import            | Effetto                                |
| ---------------------- | -------------------------------------- |
| `import modulo`        | importa il modulo intero               |
| `from modulo import x` | importa solo `x`                       |
| `from modulo import *` | importa tutto nel namespace            |
| import circolare       | può causare errori di inizializzazione |

---

💡 **Regola pratica usata nei progetti grandi**

Quasi sempre si preferisce:

```python
import modulo
```

perché:

* evita collisioni
* rende il codice più leggibile
* rende chiara l'origine delle funzioni.
