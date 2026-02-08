# 📝 **Regole di Denominazione delle Variabili**

Ottimo lavoro finora! Ora approfondiamo un aspetto fondamentale della programmazione: **come scegliere i nomi giusti per le variabili**.

Proprio come in un negozio ogni prodotto ha un’etichetta chiara per sapere subito cosa contiene, anche nel codice i nomi delle variabili devono essere **comprensibili, validi e ben strutturati**.

---

# 📌 Regole per la Denominazione delle Variabili

### 1️⃣ Iniziare con una lettera o un underscore

✔️ Validi: `item_name`, `_price`
❌ Non validi: `2item`, `5_price`

Python **non permette** di iniziare con un numero.

---

### 2️⃣ Usare solo lettere, numeri e underscore

✔️ `item_name1`
❌ `item-name` → il trattino crea errore
❌ `item$name` → caratteri speciali non permessi

---

### 3️⃣ Rispetto della sensibilità alle maiuscole

`item`, `Item` e `ITEM` sono **tre variabili diverse**.

Python distingue tra minuscole e maiuscole: è case-sensitive.

---

### 4️⃣ Evitare le parole riservate (keywords)

Non usare come variabili i nomi usati da Python per funzioni o istruzioni interne:
`print`, `if`, `type`, `class`, `for`…

❌ `print = 5`
✔️ `print_quantity = 5`

---

# ✅ Esempio di denominazione corretta

```python
# Correct variable names
item_name = "Apple"
_item_price = 0.99
item1_quantity = 10
storeName = "Green Valley Groceries"

print(item_name, _item_price, item1_quantity, storeName)
```

Tutte le regole sono rispettate:

* nomi chiari
* niente caratteri illegali
* nessuna parola riservata

---

# ❌ Esempio di denominazione scorretta

```python
# Incorrect variable names 
1item = "Banana"     # Cannot start with a number
item-name = "Orange" # Cannot contain a dash (-)
print = 5.0          # Cannot use reserved keywords
```

Queste variabili generano errori immediati.

---

# 🧠 Suggerimento pratico

Se ti accorgi che il nome che vuoi usare non è valido, prova versioni alternative come:

* `item_one`
* `first_item`
* `item_name`
* `print_quantity`

---

# 📝 **Compito**

Crea variabili corrette e significative che rappresentino un articolo alimentare: **"Bread"**.

### ✔️ Istruzioni

* `item_name` → `"Bread"`
* `item_price` → `4.52`
* `items_in_stock` → `230`
* Stampa i valori tramite `print()`

### 🧪 Codice richiesto

```python
item_name = "Bread"
item_price = 4.52
items_in_stock = 230

print("Item:", item_name)
print("Price:", item_price)
print("Quantity in stock:", items_in_stock)
```

