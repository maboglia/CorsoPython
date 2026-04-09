## 20) Duck Typing (Tipizzazione “a papera”)

### 📌 Cos’è il Duck Typing

Il **duck typing** è un principio tipico di Python:

> “Se cammina come un’anatra e starnazza come un’anatra, allora è un’anatra.”

In altre parole: **non importa il tipo reale dell’oggetto**, importa che abbia i metodi/attributi richiesti.

Python non controlla la classe, ma il **comportamento**.

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

Funzione generica:

```python
def fai_parlare(animale):
    print(animale.verso())
```

Uso:

```python
fai_parlare(Cane())
fai_parlare(Gatto())
```

Output:

```
Bau!
Miao!
```

➡️ La funzione non controlla se è Cane o Gatto: basta che esista `verso()`.

---

## 🔹 Duck Typing senza ereditarietà

Le classi possono essere completamente scollegate:

```python
class Persona:
    def verso(self):
        return "Ciao!"

fai_parlare(Persona())
```

Funziona lo stesso.

---

## 🔹 Vantaggio principale

Permette codice:

* flessibile
* riutilizzabile
* estendibile senza modificare funzioni esistenti

---

## ⚠️ Svantaggio

Se un oggetto non implementa il metodo richiesto, l’errore avviene a runtime:

```python
class Pesce:
    pass

fai_parlare(Pesce())
```

Errore:

```
AttributeError: 'Pesce' object has no attribute 'verso'
```

---

## 🔹 Controllo prudente (opzionale)

Puoi verificare con `hasattr()`:

```python
def fai_parlare(animale):
    if hasattr(animale, "verso"):
        print(animale.verso())
    else:
        print("Questo oggetto non può parlare")
```

---

### 📌 Differenza rispetto a Java/C++

In Java spesso serve implementare un’interfaccia (`implements`).

In Python invece basta che l’oggetto abbia i metodi giusti: **non serve dichiarare nulla**.

---

### 📌 Concetti chiave

* Python usa tipizzazione dinamica basata sul comportamento
* non conta la classe, conta se l’oggetto “fa” ciò che serve
* rende il codice molto flessibile ma richiede attenzione agli errori runtime
