## 16) Multiple Inheritance (Ereditarietà Multipla)

### 📌 Cos’è

La **multiple inheritance** si ha quando una classe eredita da **più classi base** contemporaneamente.

Schema:

`C(A, B)`

➡️ La classe `C` eredita attributi e metodi sia da `A` che da `B`.

---

## 🔹 Esempio base

```python
class Volante:
    def vola(self):
        print("Sto volando")

class Nuotatore:
    def nuota(self):
        print("Sto nuotando")

class Anatra(Volante, Nuotatore):
    pass


a = Anatra()
a.vola()
a.nuota()
```

Output:

```
Sto volando
Sto nuotando
```

---

## 🔹 Problema tipico: conflitto di metodi

Se entrambe le classi base hanno lo stesso metodo:

```python
class A:
    def info(self):
        print("Metodo di A")

class B:
    def info(self):
        print("Metodo di B")

class C(A, B):
    pass

c = C()
c.info()
```

Output:

```
Metodo di A
```

➡️ Python sceglie il metodo della prima classe indicata (`A`).

---

## 🔹 MRO (Method Resolution Order)

Python risolve i metodi seguendo un ordine preciso chiamato **MRO**.

Puoi vederlo così:

```python
print(C.mro())
```

Output tipico:

```
[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
```

---

## 🔹 Uso corretto con `super()`

Nella multiple inheritance è importante usare `super()` (non chiamare direttamente la classe padre).

Esempio cooperativo:

```python
class A:
    def saluta(self):
        print("A")
        super().saluta()

class B:
    def saluta(self):
        print("B")
        super().saluta()

class Base:
    def saluta(self):
        print("Base")

class C(A, B, Base):
    pass

c = C()
c.saluta()
```

Output:

```
A
B
Base
```

➡️ `super()` segue l’MRO e permette la cooperazione tra classi.

---

### ⚠️ Attenzione (Diamond Problem)

Caso classico:

```
    A
   / \
  B   C
   \ /
    D
```

Python gestisce questo problema con l’MRO (algoritmo C3), evitando chiamate doppie se usi `super()` correttamente.

---

### 📌 Concetti chiave

* una classe può ereditare da più classi
* in caso di conflitto vale l’ordine di dichiarazione
* l’MRO stabilisce la catena di ricerca dei metodi
* con multiple inheritance è fondamentale usare `super()`

