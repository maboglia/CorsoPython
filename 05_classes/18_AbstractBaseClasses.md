## 18) Abstract Base Classes (Classi Astratte)

### 📌 Cos’è una Abstract Base Class (ABC)

Una **Abstract Base Class** è una classe che:

* **non deve essere istanziata direttamente**
* serve come *modello* per le classi figlie
* definisce metodi che le sottoclassi **devono implementare**

In pratica impone un “contratto”.

---

## 🔹 Perché servono

Servono per:

* garantire che tutte le sottoclassi abbiano certi metodi
* progettare gerarchie pulite
* evitare classi incomplete usate per errore

---

## 🔹 ABC in Python (`abc`)

Python usa il modulo `abc`:

* `ABC` → classe base astratta
* `@abstractmethod` → metodo obbligatorio

---

## ✅ Esempio classico

```python
from abc import ABC, abstractmethod

class Animale(ABC):

    @abstractmethod
    def verso(self):
        pass
```

Qui `Animale` è astratta: definisce che ogni animale deve avere un metodo `verso()`.

---

## 🔹 Implementazione concreta

```python
class Cane(Animale):
    def verso(self):
        return "Bau!"

class Gatto(Animale):
    def verso(self):
        return "Miao!"
```

Uso:

```python
c = Cane()
g = Gatto()

print(c.verso())  # Bau!
print(g.verso())  # Miao!
```

---

## ❌ Errore se provi a istanziare la classe astratta

```python
a = Animale()
```

Output:

```
TypeError: Can't instantiate abstract class Animale...
```

➡️ perché `verso()` non è implementato.

---

## 🔹 Classe figlia incompleta → errore

```python
class Pesce(Animale):
    pass

p = Pesce()
```

➡️ errore, perché non ha implementato `verso()`.

---

## 🔹 ABC con metodi concreti + astratti

Una ABC può contenere anche metodi normali:

```python
from abc import ABC, abstractmethod

class Figura(ABC):

    @abstractmethod
    def area(self):
        pass

    def descrizione(self):
        return "Sono una figura geometrica"
```

Le sottoclassi devono implementare `area()`, ma ereditano `descrizione()`.

---

### 📌 Concetti chiave

* una ABC definisce una struttura obbligatoria per le sottoclassi
* non può essere istanziata se contiene metodi astratti
* garantisce coerenza nelle gerarchie OOP
* utile per progettazione e polimorfismo robusto
