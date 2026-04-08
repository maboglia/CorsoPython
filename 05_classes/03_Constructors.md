## 3) Constructors (Costruttori)

### 📌 Cos’è un costruttore

Il **costruttore** è un metodo speciale che viene chiamato **automaticamente** quando crei un oggetto.

In Python il costruttore si chiama:

```python
__init__
```

---

### 📌 A cosa serve

Serve per:

* inizializzare gli attributi dell’oggetto
* impostare valori iniziali
* preparare lo stato dell’istanza

---

### 📌 Esempio base

```python
class Studente:
    
    def __init__(self, nome):
        self.nome = nome

    def saluta(self):
        print("Ciao, mi chiamo", self.nome)


s1 = Studente("Marco")
s1.saluta()
```

Output:

```
Ciao, mi chiamo Marco
```

---

### 📌 `self.nome = nome`

Questa riga significa:

* `self.nome` → attributo dell’oggetto
* `nome` → parametro ricevuto

Quindi ogni oggetto avrà un valore diverso.

---

### 📌 Costruttore con più attributi

```python
class Studente:
    
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
```

Uso:

```python
s1 = Studente("Anna", 18)
```

---

### 📌 Valori di default

Puoi assegnare valori predefiniti:

```python
class Studente:
    
    def __init__(self, nome, eta=18):
        self.nome = nome
        self.eta = eta
```

---

### 📌 Concetti chiave

* `__init__` viene chiamato automaticamente con `Studente(...)`
* inizializza gli attributi dell’istanza
* permette parametri obbligatori o opzionali

---

**Class vs Instance Attributes**
