# 🔢 **Utilizzo delle Variabili**

Memorizzare dati è solo il primo passo.
La vera potenza delle variabili emerge quando le **utilizzi** per eseguire operazioni, calcoli e trasformazioni.

Pensale come contenitori da cui puoi prendere informazioni per svolgere compiti utili — come calcolare sconti, aggiornare quantità o determinare il costo totale di un ordine.

---

# 📌 Utilizzare le variabili nei calcoli

Ecco un esempio semplice: calcolare il costo di 100 cupcake.

```python
# Calculate the total cost of 100 cupcakes
item_price = 0.50
item_quantity = 100
total_cost = item_price * item_quantity

print("Total cost for", item_quantity, "cupcakes is $", total_cost)
```

### ✔️ Cosa abbiamo fatto?

* Memorizzato un prezzo (`item_price`)
* Memorizzato una quantità (`item_quantity`)
* Calcolato il totale (`total_cost`)
* Stampato il risultato

---

## ⚠️ Nota importante

🔸 **Non puoi usare una variabile prima di assegnarle un valore.**
Se provi a farlo, Python genererà un errore:

```
NameError: name 'variabile' is not defined
```

Assicurati sempre di creare e valorizzare le variabili prima di usarle in un calcolo o in un print.

---

# 📝 **Compito**

Calcolare il costo totale di un prodotto alimentare usando variabili e operazioni aritmetiche.

### ✔️ Istruzioni

* `item_name` → `"Soda"`
* `item_price` → `6.99`
* `purchase_quantity` → `5`
* Calcolare `total_cost = item_price * purchase_quantity`

### 🧪 Codice richiesto

```python
item_name = "Soda"
item_price = 6.99
purchase_quantity = 5

total_cost = item_price * purchase_quantity

print("Item:", item_name)
print("Price per pack:", item_price)
print("Quantity purchased:", purchase_quantity)
print("Total cost:", total_cost)
```

