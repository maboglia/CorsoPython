## 14) Method Overriding (Sovrascrittura di Metodi)

### 📌 Cos’è il Method Overriding

Il **method overriding** avviene quando una **sottoclasse** ridefinisce un metodo già presente nella **superclasse**.

➡️ In questo modo, l’oggetto della sottoclasse userà la versione del metodo definita nella sottoclasse.

---

## 🔹 Esempio base

```python
class Persona:
    def saluta(self):
        print("Ciao, sono una persona")

class Studente(Persona):
    def saluta(self):   # override
        print("Ciao, sono uno studente")
```

Uso:

```python
p = Persona()
s = Studente()

p.saluta()   # Ciao, sono una persona
s.saluta()   # Ciao, sono uno studente
```

➡️ `Studente.saluta()` ha sovrascritto `Persona.saluta()`.

---

## 🔹 Perché è utile

Serve per:

* specializzare un comportamento ereditato
* adattare una classe derivata a un contesto diverso
* implementare polimorfismo

---

## 🔹 Usare `super()` per richiamare il metodo originale

A volte vuoi estendere il comportamento della superclasse, non sostituirlo completamente.

```python
class Persona:
    def saluta(self):
        print("Ciao, sono una persona")

class Studente(Persona):
    def saluta(self):
        super().saluta()   # richiama versione base
        print("...e studio informatica")
```

Uso:

```python
s = Studente()
s.saluta()
```

Output:

```
Ciao, sono una persona
...e studio informatica
```

---

## 🔹 Override anche del costruttore `__init__`

Spesso si override anche il costruttore:

```python
class Persona:
    def __init__(self, nome):
        self.nome = nome

class Studente(Persona):
    def __init__(self, nome, classe):
        super().__init__(nome)
        self.classe = classe
```

---

### 📌 Concetti chiave

* overriding = ridefinire un metodo ereditato
* la versione chiamata dipende dal tipo reale dell’oggetto
* `super()` permette di riutilizzare il comportamento della superclasse
