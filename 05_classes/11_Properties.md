## 11) Properties (Proprietà)

### 📌 Problema che risolvono

In OOP spesso vuoi:

* accedere a un attributo come se fosse pubblico (`obj.nome`)
* ma **controllare** lettura/scrittura (validazione, calcoli, log)

In Python le **properties** permettono di farlo senza cambiare la sintassi.

---

## 🔹 Caso classico: attributo con validazione

Esempio: età non può essere negativa.

```python
class Studente:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta   # passa dalla property

    @property
    def eta(self):
        return self._eta

    @eta.setter
    def eta(self, valore):
        if valore < 0:
            raise ValueError("L'età non può essere negativa")
        self._eta = valore
```

Uso:

```python
s = Studente("Marco", 18)
print(s.eta)      # 18

s.eta = 20
print(s.eta)      # 20

s.eta = -5        # ValueError
```

---

## 🔹 Come funziona

* `@property` trasforma un metodo in **attributo leggibile**
* `@nome.setter` definisce cosa succede quando assegni un valore

Quindi:

```python
s.eta = 20
```

non scrive direttamente una variabile, ma chiama il metodo setter.

---

## 🔹 Perché usare `_eta` invece di `eta`

Per evitare ricorsione infinita.

Se nello setter scrivessi:

```python
self.eta = valore
```

richiameresti lo stesso setter all’infinito.

Quindi si usa un attributo interno come `_eta`.

---

## 🔹 Property in sola lettura

Se definisci solo `@property` e non il setter:

```python
class Studente:
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome
```

Ora `nome` è **read-only**:

```python
s = Studente("Anna")
print(s.nome)   # ok
s.nome = "Luca" # errore: AttributeError
```

---

## 🔹 Property calcolata (computed property)

Una property può anche calcolare valori:

```python
class Rettangolo:
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    @property
    def area(self):
        return self.base * self.altezza
```

Uso:

```python
r = Rettangolo(10, 5)
print(r.area)   # 50
```

➡️ `area` sembra un attributo ma è un metodo calcolato.

---

### 📌 Concetti chiave

* una property permette accesso tipo attributo ma con logica interna
* utile per validazioni, attributi read-only, calcoli dinamici
* migliora l’incapsulamento senza complicare l’uso della classe
