# ✂️🔗 **Slicing e Concatenazione di Stringhe**

Lo **slicing** e la **concatenazione** sono due tecniche fondamentali per manipolare stringhe in Python.

* Lo **slicing** ti permette di estrarre parti specifiche di una stringa.
* La **concatenazione** ti permette di unire più stringhe in una sola.

Sono strumenti essenziali quando devi analizzare, riorganizzare o presentare dati testuali.

---

# ✂️ **Slicing**

Lo slicing utilizza la sintassi:

```
string[start:end]
```

* **start** → indice del primo carattere incluso nello slice
* **end** → indice del carattere *successivo* all’ultimo incluso (non incluso)

Esempio:

```python
fruit = "Strawberries"

# Slicing the string to get "Straw"
sliced_fruit = fruit[0:5]  # da S (indice 0) a w (indice 4)

print("Sliced part:", sliced_fruit)
```

---

# 🔗 **Concatenazione**

La concatenazione unisce più stringhe usando l'operatore `+`.

```python
part1 = "Straw"
part2 = "berry"

new_word = part1 + part2
print("Concatenated word:", new_word)

# Aggiungere uno spazio
print(part1 + " " + part2)
```

---

# 📝 **Compito**

Lavorerai con una stringa contenente un elenco di alimenti.
Usa **slicing** e **concatenazione** per estrarre alcune parole e costruire una frase.

### ✔️ Stringa fornita

```python
grocery_items = "milk, eggs, cheese, bread, apples"
```

### ✔️ Cosa devi estrarre tramite slicing

* `"milk"` → `dairy1`
* `"cheese"` → `dairy2`
* `"bread"` → `bakery1`

*(Hai piena libertà nel determinare gli indici corretti.)*

### ✔️ Costruisci la frase tramite concatenazione

```
We have dairy and bakery items: <dairy1>, <dairy2>, and <bakery1> in aisle 5
```

### 🧪 Esempio di soluzione

```python
grocery_items = "milk, eggs, cheese, bread, apples"

# Extracting items using slicing
dairy1 = grocery_items[0:4]        # "milk"
dairy2 = grocery_items[12:18]      # "cheese"
bakery1 = grocery_items[20:25]     # "bread"

# Concatenating the final message
message = "We have dairy and bakery items: " + dairy1 + ", " + dairy2 + ", and " + bakery1 + " in aisle 5"

print(message)
```
