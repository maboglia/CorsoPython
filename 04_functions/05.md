## 🔹 **Default Arguments**

I *default arguments* consentono di assegnare ai parametri un valore predefinito.
Se l’utente non fornisce un valore per quel parametro, Python utilizza automaticamente il valore di default.

### ✔️ Esempio base

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")
    
greet("Alice")          # usa il default: "Hello"
greet("Bob", "Hi")      # usa il valore passato: "Hi"
```

### ✔️ Perché usarli

* Per evitare errori quando un parametro non viene fornito
* Per ridurre il codice ripetuto
* Per dare maggiore flessibilità alle funzioni

### ✔️ Attenzione ai valori mutabili

Mai usare liste o dizionari come valori di default:

```python
def add_item(item, items=[]):   # ⚠️ errore classico
    items.append(item)
    return items
```

Usare invece:

```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

I *default arguments* permettono di semplificare le funzioni e di renderle più robuste, purché si usino con attenzione.

---

Quando usi **liste, dizionari o altri oggetti mutabili come valori di default**, Python li crea **una sola volta**, nel momento in cui la funzione viene definita — **non ogni volta che la funzione viene chiamata**.

### 🔥 Perché è un problema?

Perché **tutte le chiamate successive** alla funzione con quel parametro mancante **condivideranno lo stesso oggetto mutabile**.

---

## ❌ Esempio del problema

```python
def add_item(item, items=[]):   
    items.append(item)
    return items

print(add_item("apple"))   # ['apple']
print(add_item("orange"))  # ['apple', 'orange']  <-- ERRORE!
print(add_item("pear"))    # ['apple', 'orange', 'pear']
```

### Cosa succede?

* La lista `items` viene creata **solo al momento della definizione** della funzione.
* A ogni chiamata, Python riusa **la stessa lista**, invece di crearne una nuova.

---

## ✔️ Soluzione corretta

Usare un valore immutabile come default (es. `None`) e poi creare la lista dentro la funzione:

```python
def add_item(item, items=None):
    if items is None:
        items = []          # nuova lista ogni volta
    items.append(item)
    return items
```

Ora funziona come previsto:

```python
print(add_item("apple"))   # ['apple']
print(add_item("orange"))  # ['orange']
```

---

## 📌 Perché succede davvero?

Perché i valori di default sono memorizzati in una struttura interna (`__defaults__`)
e vengono valutati **una sola volta**, non a ogni chiamata.

Gli oggetti immutabili (numero, stringa, tuple) non danno problemi.
Gli oggetti mutabili invece *cambiano*, e il cambiamento rimane tra una chiamata e l’altra.

---

## 🧠 Regola d’oro

> **Non usare mai oggetti mutabili come default.
> Usa `None`, poi inizializza dentro la funzione.**

