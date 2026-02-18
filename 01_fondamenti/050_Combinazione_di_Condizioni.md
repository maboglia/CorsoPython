# **Combinazione di Condizioni**

Ora che hai acquisito familiarità con i valori booleani, siamo pronti a fare un passo avanti: **combinare più condizioni**.
Questa abilità consente ai programmi di prendere decisioni più intelligenti e realistiche, soprattutto quando devono verificare più criteri contemporaneamente — proprio come avviene nella gestione di un negozio di alimentari.

---

## ✔️ Comprendere le condizioni combinate

In Python, possiamo combinare condizioni semplici usando gli **operatori logici**:

* **and** → restituisce `True` *solo* se entrambe le condizioni sono vere.
* **or** → restituisce `True` se almeno una condizione è vera.
* **not** → inverte il valore booleano (True diventa False e viceversa).

Questi operatori permettono di costruire espressioni complesse basate su molteplici criteri.

---

## ✔️ Applicazione d’esempio

### **Esempio 1: Usare `and` per controllare due condizioni**

Verifichiamo se un articolo è *deperibile* **e** ha una grande quantità in magazzino:

```python
# Define the perishable and stock status conditions
is_perishable = True
item_quantity = 110
perishable_highStockRisk = 100

# Using the (and) operator to combine two conditions
consider_discount = is_perishable and (item_quantity >= perishable_highStockRisk)

# Print the result
print("Is the item perishable and high in stock?", consider_discount)
```

---

### **Esempio 2: Usare `or` per verificare una condizione alternativa**

Controlliamo se un articolo è stagionale **oppure** festivo:

```python
# Define the seasonal and holiday status conditions 
seasonal_item = False
holiday_item = True

# Combine the conditions using OR
temporary_stock = seasonal_item or holiday_item

# Print the result
print("Is this a seasonal or holiday item?", temporary_stock)
```

---

### **Esempio 3: Usare `not` per invertire una condizione**

Verifichiamo se un articolo **non** è deperibile:

```python
# Define the item status condition
is_perishable = True

# Use NOT to invert the condition
long_shelf_life = not is_perishable

# Print the result
print("Does the item need to be sold quickly?", long_shelf_life)
```

**Output:**
`Does the item need to be sold quickly? False`

---

## 🧪 **Compito**

Ora tocca a te combinare condizioni per determinare se un articolo è idoneo a una promozione.

### **Cosa Devi Fare**

1. Definire una variabile booleana **movingProduct** che sia `True` se:

   * l’articolo è **in sconto**, **oppure**
   * l’articolo è **in scorte basse**
     (usa gli operatori logici).

2. Creare una variabile booleana **promotion** che sia `True` se:

   * l’articolo **non è in sconto**, **e**
   * ha **scorte sufficienti**.

3. Stampare:

```
Is the item eligible for promotion? <promotion>
```

---

# **Sfida: Logica Booleana**

È arrivato il momento di mettere alla prova ciò che hai imparato su operatori logici e condizioni combinate.
In questa sfida lavorerai con uno scenario realistico per un negozio di alimentari, dove diverse condizioni concorrono a determinare se un articolo dovrebbe essere scontato.

Preparati a usare **and**, **or**, **not** e gli operatori di confronto per prendere una decisione intelligente.

---

## 🧠 **Scenario**

Un articolo alimentare può essere soggetto a sconto sulla base di:

* **stagionalità**
* **livello delle scorte**
* **andamento delle vendite**
* **presenza o meno di uno sconto attivo**

Il tuo compito è gestire questa logica complessa attraverso variabili booleane combinate.

---

## ✔️ **Obiettivo della Sfida**

Dovrai determinare se l’articolo deve essere scontato.

### I tuoi compiti

### **1️⃣ Definire la variabile `overstock_risk`**

Deve essere `True` se:

* l’articolo **è stagionale**, **e**
* il suo `current_stock` **supera** `high_stock_threshold`

> Usa l’operatore **and** combinato con un confronto numerico.

---

### **2️⃣ Definire la variabile `discount_eligible`**

Deve essere `True` se:

* l’articolo **non** sta vendendo bene
  (`not selling_well`)
* l’articolo **non è già** in sconto
  (`not on_sale`)

> Usa l’operatore **not** e combinalo con **and**.

---

### **3️⃣ Creare la variabile `make_discount`**

Questa deve essere `True` se **almeno una** delle seguenti è vera:

* `overstock_risk`
* `discount_eligible`

> Usa l’operatore **or**.

---

## 🖨️ **Requisiti di output**

Alla fine devi stampare:

```
Should the item be discounted? <make_discount>
```
