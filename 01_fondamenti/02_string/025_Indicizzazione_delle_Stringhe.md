# 🔤 **Indicizzazione delle Stringhe e Funzione `len()`**

Le stringhe in Python sono **sequenze di caratteri**, e ogni carattere — inclusi spazi, virgole e simboli — possiede una posizione chiamata **indice**.
Capire come funziona l’indicizzazione è fondamentale per leggere, analizzare o modificare il testo nei tuoi programmi.

---

# 📌 Indicizzazione Positiva

Python assegna un indice a ogni carattere della stringa.
**L’indicizzazione parte da 0**, quindi:

* Primo carattere → indice **0**
* Secondo carattere → indice **1**
* Terzo carattere → indice **2**

E così via.

Esempio con la stringa `"Apple"`:

| A | p | p | l | e |
| - | - | - | - | - |
| 0 | 1 | 2 | 3 | 4 |

---

# 🔁 Indicizzazione Negativa

Python permette anche di contare i caratteri **partendo dalla fine**.

* Ultimo carattere → indice **-1**
* Penultimo → indice **-2**
* E così via…

La stessa stringa `"Apple"` vista da destra:

| A  | p  | p  | l  | e  |
| -- | -- | -- | -- | -- |
| -5 | -4 | -3 | -2 | -1 |

Questo è molto utile quando non conosci la lunghezza esatta della stringa.

---

# 🧪 Esempio base

```python
grocery_item = "Milk"

# Accessing the first and last character using indexing
first_character = grocery_item[0]   # 'M'
last_character = grocery_item[-1]   # 'k'

print("First character:", first_character)
print("Last character:", last_character)
```

---

# 📏 Usare `len()` per misurare la lunghezza della stringa

La funzione `len()` restituisce **il numero totale di caratteri**, inclusi gli spazi.

```python
store_name = "Green Valley Market"

length_of_name = len(store_name)      # Include gli spazi
character_after_space = store_name[6] # 'V'

print("Length of store name:", length_of_name)
print("Character after the space:", character_after_space)
```

---

# 📝 **Compito**

Dati tre prodotti nello stesso campo `grocery_item`, usa l’indicizzazione e `len()` per ricavare informazioni utili.

> **Puoi usare questa stringa come riferimento:**
> `"Milk Bread Eggs"`

### ✔️ Obiettivi

* Usa **len()** per ottenere la lunghezza totale della stringa → `length_of_item`
* Usa **indicizzazione positiva** per ottenere il **primo carattere di ogni parola**
  → `first_char`, `second_char`, `third_char`
* Usa **indicizzazione negativa** per ottenere l’**ultimo carattere di ogni parola**
  → `last_char1`, `last_char2`, `last_char3`

### 🧪 Codice guida

```python
grocery_item = "Milk Bread Eggs"

# Length of the string
length_of_item = len(grocery_item)

# Positive indexing (first character of each word)
first_char = grocery_item[0]      # 'M'
second_char = grocery_item[5]     # 'B'
third_char = grocery_item[11]     # 'E'

# Negative indexing (last character of each word)
last_char1 = grocery_item[3]      # 'k'
last_char2 = grocery_item[9]      # 'd'
last_char3 = grocery_item[-1]     # 's'

print("Length:", length_of_item)
print("First letters:", first_char, second_char, third_char)
print("Last letters:", last_char1, last_char2, last_char3)
```

