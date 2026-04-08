## 9) Making Custom Containers (Creare Contenitori Personalizzati)

### 📌 Cos’è un container

Un **container** è un oggetto che contiene altri oggetti, come:

* `list`
* `tuple`
* `dict`
* `set`

In Python puoi creare una tua classe che si comporta come un container implementando alcuni **magic methods**.

---

### 📌 Metodi fondamentali di un container

* `__len__()` → permette `len(obj)`
* `__getitem__(index)` → permette `obj[index]`
* `__setitem__(index, value)` → permette `obj[index] = value`
* `__iter__()` → permette `for x in obj`
* `__contains__(item)` → permette `item in obj`

---

### 📌 Esempio: container semplice (lista di studenti)

```python id="c56rjl"
class Classe:
    def __init__(self):
        self.studenti = []

    def add(self, studente):
        self.studenti.append(studente)

    def __len__(self):
        return len(self.studenti)

    def __getitem__(self, index):
        return self.studenti[index]
```

Uso:

```python id="lm3e7h"
c = Classe()
c.add("Marco")
c.add("Anna")

print(len(c))      # 2
print(c[0])        # Marco
print(c[1])        # Anna
```

---

### 📌 Rendere l’oggetto iterabile (`__iter__`)

Così puoi fare `for`:

```python id="k7lh77"
class Classe:
    def __init__(self):
        self.studenti = []

    def add(self, studente):
        self.studenti.append(studente)

    def __iter__(self):
        return iter(self.studenti)
```

Uso:

```python id="iwdt72"
c = Classe()
c.add("Marco")
c.add("Anna")

for s in c:
    print(s)
```

---

### 📌 Supportare `in` (`__contains__`)

```python id="txr2u8"
def __contains__(self, item):
    return item in self.studenti
```

Uso:

```python id="s1cyn0"
print("Marco" in c)  # True
```

---

### 📌 Concetto chiave

Implementando questi magic methods puoi creare classi che si comportano come le collezioni native di Python.

