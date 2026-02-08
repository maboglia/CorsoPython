# **Operatori di Appartenenza e Confronti di Tipo**

In questo capitolo approfondiamo due strumenti fondamentali per lavorare in modo più preciso ed efficiente con i dati nei tuoi programmi Python:
🔍 **gli operatori di appartenenza**
🔎 **i confronti di tipo**

Questi strumenti diventano indispensabili quando si gestiscono informazioni provenienti da sistemi di cassa, inventari o cataloghi di prodotti—contesti tipici di un negozio di alimentari.

---

## 🧩 **Operatori di Appartenenza: “in” e “not in”**

Gli operatori di appartenenza permettono di verificare rapidamente se un elemento è contenuto all’interno di un oggetto iterabile.
In Python, stringhe, liste, tuple e molti altri oggetti possono essere "iterati", quindi puoi controllarne facilmente il contenuto.

Grazie a quanto hai già imparato su indicizzazione e slicing, sai che le stringhe sono iterabili: questo ti permette di verificare se una **sottostringa** compare all’interno di una stringa più lunga.

Esempio:

```python
itemName = "Strawberries"
in_name = "Straw" in itemName
print("Is 'Straw' in 'Strawberries'?", in_name)
```

Nel contesto di un negozio, potresti usarli per categorizzare prodotti, identificare keyword importanti o marcare articoli speciali.

---

## 🧪 **Applicazione nel Mondo Reale**

Il fornitore invia una descrizione di un prodotto; il sistema deve capire se sono presenti parole chiave come *organic*, *local*, *raw*, ecc.

Esempio:

```python
product_description = "Fresh organic milk from local farms."

is_organic = "organic" in product_description
is_local = "local" in product_description
```

---

## 🧷 **Confronti di Tipo con `type()`**

Nella gestione dei dati di un negozio, è essenziale verificare che ogni campo abbia il tipo corretto:

* stringhe per i nomi
* float per i prezzi
* interi per le quantità

Un errore di tipo può portare a problemi nel checkout, nel calcolo dei totali o nell’aggiornamento delle scorte.

La funzione `type()` permette di verificare rapidamente se un valore è del tipo atteso:

```python
correct_name_type = type(product_name) == str
correct_price_type = type(product_price) == float
correct_quantity_type = type(product_quantity) == int
```

---

# 📝 **Compito**

Stai aggiungendo un nuovo prodotto al sistema del negozio.
Dovrai verificare parole chiave nella descrizione e controllare i tipi dei dati forniti.

### **1️⃣ Usa gli operatori di appartenenza**

Controlla se le parole:

* `"raw"`
* `"Imported"`

sono presenti nella variabile `description`.

Salva i risultati in:

* `contains_raw`
* `contains_Imported`

> Attenzione! Python distingue tra maiuscole e minuscole: `"imported"` ≠ `"Imported"`.

---

### **2️⃣ Controlla i tipi dei dati**

Verifica con `type()` se:

* `price` è un **float**
* `count` è un **int**

Assegna i risultati a:

* `price_is_float`
* `count_is_int`

---

# 📤 **Requisiti di Output**

Il tuo programma deve stampare:

```
Contains 'raw': <contains_raw>
Contains 'Imported': <contains_Imported>
Is price a float?: <price_is_float>
Is count an integer?: <count_is_int>
```
