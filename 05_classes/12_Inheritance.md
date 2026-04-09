## 12) Inheritance (Ereditarietà)

### 📌 Cos’è l’ereditarietà

L’**inheritance** (ereditarietà) è un meccanismo OOP che permette di creare una nuova classe (**sottoclasse / derived class**) a partire da una classe esistente (**superclasse / base class**).

La sottoclasse:

* eredita attributi e metodi della superclasse
* può aggiungere nuove funzionalità
* può modificare (override) metodi esistenti

---

## 🔹 Esempio base

```python
class Persona:
    def __init__(self, nome):
        self.nome = nome

    def saluta(self):
        print("Ciao, sono", self.nome)


class Studente(Persona):
    pass
```

Uso:

```python
s = Studente("Marco")
s.saluta()
```

Output:

```
Ciao, sono Marco
```

➡️ `Studente` eredita automaticamente `__init__` e `saluta()` da `Persona`.

---

## 🔹 Aggiungere metodi nella sottoclasse

```python
class Studente(Persona):
    def studia(self):
        print(self.nome, "sta studiando")
```

Uso:

```python
s = Studente("Anna")
s.saluta()
s.studia()
```

---

## 🔹 Ridefinire il costruttore (con `super()`)

Se la sottoclasse ha attributi aggiuntivi:

```python
class Studente(Persona):
    def __init__(self, nome, classe):
        super().__init__(nome)   # richiama il costruttore della superclasse
        self.classe = classe
```

Uso:

```python
s = Studente("Marco", "5A")
print(s.nome, s.classe)
```

---

## 🔹 Perché usare `super()`

`super()` serve per:

* riusare il codice della classe base
* evitare duplicazione
* mantenere la logica comune centralizzata

---

## 🔹 Relazione "IS-A"

L’ereditarietà rappresenta una relazione del tipo:

✅ **Studente IS-A Persona**
❌ **Persona IS-A Studente** (non vero)

Quindi va usata solo quando la relazione è coerente.

---

### 📌 Concetti chiave

* una sottoclasse eredita metodi/attributi dalla superclasse
* `super()` richiama metodi della classe padre
* utile per riuso del codice e specializzazione

