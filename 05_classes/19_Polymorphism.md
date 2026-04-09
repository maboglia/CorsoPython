## 19) Polymorphism (Polimorfismo)

### 📌 Cos’è il polimorfismo

Il **polimorfismo** significa: *“stessa interfaccia, comportamenti diversi”*.

In pratica, oggetti di classi diverse possono essere usati nello stesso modo (stessi metodi), ma reagiscono in modo differente.

---

## 🔹 Esempio semplice

```python
class Cane:
    def verso(self):
        return "Bau!"

class Gatto:
    def verso(self):
        return "Miao!"
```

Uso polimorfico:

```python
animali = [Cane(), Gatto()]

for a in animali:
    print(a.verso())
```

Output:

```
Bau!
Miao!
```

➡️ Lo stesso codice (`a.verso()`) funziona per oggetti diversi.

---

## 🔹 Polimorfismo con ereditarietà

Spesso nasce con l’ereditarietà e l’override.

```python
class Figura:
    def area(self):
        raise NotImplementedError()

class Rettangolo(Figura):
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        return self.b * self.h

class Cerchio(Figura):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r
```

Uso:

```python
figure = [Rettangolo(10, 5), Cerchio(3)]

for f in figure:
    print(f.area())
```

➡️ `area()` è lo stesso metodo, ma calcola cose diverse.

---

## 🔹 Polimorfismo e funzioni generiche

Il vantaggio è che puoi scrivere codice generico:

```python
def stampa_area(figura):
    print("Area =", figura.area())
```

Funziona per qualsiasi oggetto che abbia `area()`.

---

### 📌 Concetti chiave

* polimorfismo = stesso metodo chiamato, risultati diversi
* riduce `if/else` e rende il codice più estendibile
* spesso ottenuto tramite override o ABC
* fondamentale per progettare sistemi flessibili
