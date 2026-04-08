## 8) Performing Arithmetic Operations (Operazioni Aritmetiche)

### 📌 Idea principale

In Python puoi far funzionare operatori come `+ - * /` su oggetti personalizzati implementando i **magic methods aritmetici**.

Esempio: `a + b` chiama automaticamente `a.__add__(b)`.

---

### 📌 Operatore `+` con `__add__`

Supponiamo di avere una classe `Money`:

```python
class Money:
    def __init__(self, euro):
        self.euro = euro

    def __add__(self, other):
        return Money(self.euro + other.euro)

    def __str__(self):
        return f"{self.euro} €"
```

Uso:

```python
m1 = Money(10)
m2 = Money(25)

m3 = m1 + m2
print(m3)
```

Output:

```
35 €
```

---

### 📌 Altri operatori comuni

* `__sub__(self, other)` → `-`
* `__mul__(self, other)` → `*`
* `__truediv__(self, other)` → `/`
* `__floordiv__(self, other)` → `//`
* `__mod__(self, other)` → `%`
* `__pow__(self, other)` → `**`

---

### 📌 Esempio: moltiplicazione per numero

```python
class Money:
    def __init__(self, euro):
        self.euro = euro

    def __mul__(self, n):
        return Money(self.euro * n)

    def __str__(self):
        return f"{self.euro} €"
```

Uso:

```python
m = Money(10)
print(m * 3)
```

Output:

```
30 €
```

---

### 📌 Operazioni inverse (`__radd__`, `__rmul__`)

Se vuoi permettere `3 * m` invece di `m * 3`:

```python
def __rmul__(self, n):
    return self.__mul__(n)
```

---

### 📌 Concetti chiave

* gli operatori sugli oggetti si implementano con magic methods
* `+` → `__add__`
* puoi creare oggetti che si comportano come numeri reali


