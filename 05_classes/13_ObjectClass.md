## 13) The Object Class (`object`)

### 📌 Cos’è `object`

In Python, **`object` è la superclasse di tutte le classi**.

Questo significa che ogni classe che definisci:

```python
class Studente:
    pass
```

in realtà è equivalente a:

```python
class Studente(object):
    pass
```

➡️ Quindi **tutti gli oggetti Python derivano da `object`**.

---

## 🔹 Perché è importante

Grazie a `object`, tutte le classi ereditano automaticamente comportamenti base come:

* rappresentazione testuale (`__repr__`)
* confronto per identità (`__eq__` di default)
* gestione degli attributi (`__getattribute__`)
* introspezione (`__class__`, `__dict__`, ecc.)

---

## 🔹 Verifica pratica

```python
class Studente:
    pass

s = Studente()

print(isinstance(s, object))  # True
print(issubclass(Studente, object))  # True
```

---

## 🔹 Metodi principali ereditati da `object`

Alcuni metodi importanti definiti in `object` sono:

* `__init__()` → costruttore base
* `__str__()` → conversione in stringa per `print`
* `__repr__()` → rappresentazione tecnica
* `__eq__()` → confronto con `==` (di default confronta identità)
* `__hash__()` → usato per dict e set
* `__getattribute__()` → accesso agli attributi

---

## 🔹 Default behavior (comportamento predefinito)

Se non definisci `__str__`, Python usa quello di `object`:

```python
class Studente:
    pass

s = Studente()
print(s)
```

Output tipico:

```
<__main__.Studente object at 0x...>
```

➡️ è il comportamento base ereditato da `object`.

---

## 🔹 Concetto chiave: tutto è un oggetto

In Python:

* numeri (`int`)
* stringhe (`str`)
* liste (`list`)
* funzioni
* classi

sono tutti oggetti, quindi derivano da `object`.

Esempio:

```python
print(isinstance(5, object))       # True
print(isinstance("ciao", object))  # True
```

---

### 📌 Concetti chiave

* `object` è la radice della gerarchia delle classi
* ogni classe eredita implicitamente da `object`
* fornisce i metodi fondamentali del linguaggio OOP in Python
