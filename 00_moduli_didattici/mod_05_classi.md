# Modulo 5 – Programmazione Orientata agli Oggetti (12 ore)

La **Programmazione Orientata agli Oggetti (OOP)** permette di:

* modellare il mondo reale
* organizzare il codice in modo scalabile
* lavorare in team su progetti complessi

👉 In Python l’OOP è **semplice ma potente**, ideale per la didattica.

---

## 5.1 Classi base (5 ore)

### Definizione di classi

Una **classe** è un modello (template) per creare oggetti.

```python
class Persona:
    pass
```

Un **oggetto** è un’istanza della classe:

```python
p = Persona()
```

---

### `__init__` e `self`

Il metodo `__init__` è il **costruttore**.

```python
class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
```

* `self` rappresenta **l’oggetto corrente**
* ogni attributo dell’oggetto passa da `self`

Uso:

```python
p = Persona("Mario", 30)
```

---

### Attributi e metodi

```python
class Persona:
    def __init__(self, nome):
        self.nome = nome

    def saluta(self):
        print(f"Ciao, sono {self.nome}")
```

```python
p.saluta()
```

---

### Metodi speciali: `__str__` e `__repr__`

```python
class Persona:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f"Persona: {self.nome}"

    def __repr__(self):
        return f"Persona(nome='{self.nome}')"
```

* `__str__` → output per l’utente
* `__repr__` → output tecnico / debug

---

### Properties e getter/setter

```python
class Studente:
    def __init__(self, eta):
        self._eta = eta

    @property
    def eta(self):
        return self._eta

    @eta.setter
    def eta(self, valore):
        if valore < 0:
            raise ValueError("Età non valida")
        self._eta = valore
```

Uso:

```python
s = Studente(20)
s.eta = 21
```

👉 Incapsulamento **senza cambiare la sintassi di accesso**.

---

## 5.2 OOP avanzata (7 ore)

### Ereditarietà

```python
class Persona:
    def saluta(self):
        print("Ciao")

class Studente(Persona):
    def studia(self):
        print("Sto studiando")
```

```python
s = Studente()
s.saluta()
```

---

### Polimorfismo

Stesso metodo, comportamento diverso.

```python
class Cane:
    def parla(self):
        print("Bau")

class Gatto:
    def parla(self):
        print("Miao")
```

```python
def fai_parlare(animale):
    animale.parla()
```

👉 Python usa **duck typing**.

---

### Encapsulation

In Python è **convenzionale**:

```python
self._privato
self.__molto_privato
```

```python
class Conto:
    def __init__(self, saldo):
        self._saldo = saldo
```

👉 Si protegge l’accesso, non si blocca.

---

### Classi astratte

```python
from abc import ABC, abstractmethod

class Animale(ABC):
    @abstractmethod
    def verso(self):
        pass
```

```python
class Cane(Animale):
    def verso(self):
        print("Bau")
```

👉 Impongono una struttura alle sottoclassi.

---

### Dataclasses

Riduce il boilerplate.

```python
from dataclasses import dataclass

@dataclass
class Punto:
    x: int
    y: int
```

Uso:

```python
p = Punto(3, 4)
print(p)
```

👉 Perfette per:

* DTO
* modelli dati
* configurazioni

---

### Composition vs inheritance

**Ereditarietà**:

```python
class Auto(Veicolo):
    pass
```

**Composizione**:

```python
class Motore:
    pass

class Auto:
    def __init__(self):
        self.motore = Motore()
```

👉 Regola didattica:

> *“Favorire la composizione rispetto all’ereditarietà”*

---

## Riepilogo didattico

Questo modulo permette di:

* progettare software
* lavorare su progetti complessi
* preparare l’accesso a framework e architetture

È la base per:

* MVC
* REST
* applicazioni reali

