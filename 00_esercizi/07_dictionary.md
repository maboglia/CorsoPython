# **10 esercizi Python sui DIZIONARI**

Livello: **base → base/intermedio**

---

## 🧩 **Esercizio 1 — Creazione di un dizionario**

Crea un dizionario chiamato `product` che contenga:

* `"name"` → `"Milk"`
* `"price"` → `1.50`
* `"in_stock"` → `True`

Stampalo a schermo.

---

## 🧩 **Esercizio 2 — Accesso ai valori**

Dato il dizionario:

```python
inventory = {
    "Apples": 50,
    "Bananas": 30,
    "Oranges": 20
}
```

Stampa:

* la quantità di `"Bananas"`
* la quantità di `"Oranges"`

---

## 🧩 **Esercizio 3 — Aggiungere una coppia chiave-valore**

Dato il dizionario:

```python
cart = {
    "Bread": 2,
    "Milk": 1
}
```

Aggiungi il prodotto `"Eggs"` con quantità `12`
e stampa il dizionario aggiornato.

---

## 🧩 **Esercizio 4 — Modificare un valore**

Dato il dizionario:

```python
prices = {
    "Apple": 1.20,
    "Banana": 0.50,
    "Cherry": 2.50
}
```

Aggiorna il prezzo della `"Banana"` a `0.60`
e stampa il dizionario.

---

## 🧩 **Esercizio 5 — Rimozione di un elemento**

Dato il dizionario:

```python
stock = {
    "Milk": 10,
    "Cheese": 5,
    "Butter": 0
}
```

Rimuovi l’elemento `"Butter"` e stampa il dizionario risultante.

---

## 🧩 **Esercizio 6 — Verifica di una chiave**

Dato il dizionario:

```python
users = {
    "admin": "active",
    "guest": "inactive"
}
```

Scrivi un controllo che stampi:

* `"User exists"` se `"admin"` è presente
* `"User not found"` altrimenti

---

## 🧩 **Esercizio 7 — Iterazione su chiavi e valori**

Dato il dizionario:

```python
grades = {
    "Alice": 28,
    "Bob": 30,
    "Charlie": 25
}
```

Usa un ciclo `for` per stampare:

```
Student: Alice, Grade: 28
```

(per ogni studente)

---

## 🧩 **Esercizio 8 — Uso di `len()`**

Dato il dizionario:

```python
orders = {
    "order_1": 120,
    "order_2": 85,
    "order_3": 240
}
```

Stampa il numero totale di ordini.

---

## 🧩 **Esercizio 9 — Liste come valori**

Dato il dizionario:

```python
classroom = {
    "Math": ["Alice", "Bob"],
    "Science": ["Charlie", "Diana"]
}
```

Stampa:

* gli studenti del corso `"Math"`
* il primo studente del corso `"Science"`

---

## 🧩 **Esercizio 10 — Dizionario annidato**

Dato il dizionario:

```python
products = {
    "Milk": {"price": 1.50, "stock": 20},
    "Bread": {"price": 0.80, "stock": 50}
}
```

Stampa:

* il prezzo del `"Milk"`
* lo stock del `"Bread"`

---

## 🎯 Competenze allenate

✔ Creazione e accesso ai dizionari
✔ Aggiunta, modifica e rimozione
✔ Verifica chiavi con `in`
✔ Iterazione con `.items()`
✔ Dizionari annidati
✔ Liste come valori
✔ Uso di `len()`
