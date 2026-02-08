# **Operatori di Appartenenza e Confronti di Tipo**

In questo capitolo approfondiremo due strumenti fondamentali che renderanno più precisa e potente la gestione dei dati nei tuoi programmi Python:
⭐ **gli operatori di appartenenza**
⭐ **i confronti di tipo**

---

## 🔍 Operatori di appartenenza: `in` e `not in`

Gli operatori di appartenenza permettono di verificare se un elemento è contenuto all’interno di un oggetto iterabile.
Ricorda: in Python, **stringhe**, **liste**, **tuple** e molti altri oggetti sono iterabili.

Le stringhe, in particolare, possono essere controllate per verificare la presenza di sottostringhe.

Esempio:

```python
itemName = "Strawberries"
in_name = "Straw" in itemName
print("Is 'Straw' in 'Strawberries'?", in_name)
```

---

## 🧪 Applicazione pratica

Nel sistema informativo del negozio potresti ricevere descrizioni dettagliate dai fornitori e voler verificare la presenza di parole chiave utili per classificazione o marketing:

```python
# Product description from supplier
product_description = "Fresh organic milk from local farms, pasteurized and homogenized."

# Check if the "organic" and "local" keywords are in the product description
is_organic = "organic" in product_description
is_local = "local" in product_description

# Print the presence of these keywords to decide on marketing strategies
print("Is the product organic?", is_organic)
print("Is the product locally sourced?", is_local)
```

---

## 🧠 Verifica dei tipi di dati

Per evitare errori nel checkout, nelle statistiche o nell’aggiornamento dell’inventario, è fondamentale assicurarsi che i dati siano del tipo corretto.

La funzione `type()` permette di verificare la natura effettiva di una variabile.

Esempio reale:

```python
# Sample data received from a cashier or inventory management system
product_name = "Almond Milk"
product_price = "3.49"
product_quantity = 30

# Checking if the data types are as expected
correct_name_type = type(product_name) == str
correct_price_type = type(product_price) == float  # Intentional error for demonstration
correct_quantity_type = type(product_quantity) == int

# Print the results to verify data types
print("Is product_name a string?", correct_name_type)
print("Is product_price a float?", correct_price_type)
print("Is product_quantity an integer?", correct_quantity_type)

print("Data type check complete. Please review and correct any 'False' outcomes for data corrections.")
```

---

# 📝 **Compito**

Stai registrando un nuovo prodotto nel sistema del negozio.
Usa ciò che hai imparato per analizzarne descrizione e dati.

### 1️⃣ Operatori di appartenenza

Controlla se le parole:

* `"raw"`
* `"Imported"`

sono contenute nella stringa `description`.

Assegna i risultati a:

* `contains_raw`
* `contains_Imported`

> Attenzione: Python distingue **maiuscole/minuscole** → `"Imported"` ≠ `"imported"`.

---

### 2️⃣ Confronti di tipo

Usa `type()` per verificare:

* se `price` è un *float*
* se `count` è un *int*

Assegna i risultati a:

* `price_is_float`
* `count_is_int`

---

# 📤 **Requisiti di Output**

Stampa esattamente le seguenti righe:

```
Contains 'raw': <contains_raw>
Contains 'Imported': <contains_Imported>
Is price a float?: <price_is_float>
Is count an integer?: <count_is_int>
```

