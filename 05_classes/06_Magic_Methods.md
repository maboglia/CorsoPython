## 6) Magic Methods (Metodi Magici)

### 📌 Cosa sono

I **magic methods** (o *dunder methods*, perché hanno `__nome__`) sono metodi speciali che Python chiama automaticamente in certe situazioni.

Esempio:

* `__init__` → quando crei un oggetto
* `__str__` → quando fai `print(obj)`
* `__len__` → quando fai `len(obj)`

---

### 📌 Perché sono importanti

Permettono di rendere le classi **integrate nel linguaggio**, cioè usabili come i tipi built-in (`list`, `str`, ecc.).

---

### 📌 Esempio: `__str__` (stampa leggibile)

```python
class Studente:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f"Studente: {self.nome}"


s1 = Studente("Marco")
print(s1)
```

Output:

```
Studente: Marco
```

Senza `__str__`, Python stamperebbe qualcosa tipo:
`<__main__.Studente object at 0x...>`

---

### 📌 Esempio: `__repr__` (rappresentazione tecnica)

```python
class Studente:
    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return f"Studente('{self.nome}')"
```

`__repr__` è utile per debug e log.

---

### 📌 Esempio: `__len__`

```python
class Classe:
    def __init__(self, studenti):
        self.studenti = studenti

    def __len__(self):
        return len(self.studenti)


c = Classe(["Marco", "Anna", "Luca"])
print(len(c))
```

Output:

```
3
```

---

### 📌 Alcuni magic methods comuni

* `__init__()` → costruttore
* `__str__()` → stampa utente
* `__repr__()` → stampa tecnica/debug
* `__len__()` → supporto `len()`
* `__eq__()` → confronto con `==`
* `__lt__()` → confronto con `<`
* `__add__()` → supporto `+`
* `__getitem__()` → supporto `obj[i]`

---

### 📌 Concetto chiave

I magic methods permettono di definire **come un oggetto si comporta** con operatori e funzioni standard di Python.

