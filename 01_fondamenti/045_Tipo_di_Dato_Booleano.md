# **Tipo di Dato Booleano**

In questo capitolo esploreremo uno dei tipi di dato più importanti in programmazione: il **Booleano**.
Anche se molto semplice — perché può assumere solo due valori, **True** o **False** — il tipo Boolean permette ai programmi di prendere decisioni, reagire a condizioni e controllare il flusso dell’esecuzione.

Nel contesto del nostro negozio di alimentari, i booleani possono aiutarci a capire se un prodotto è disponibile, se un prezzo supera una certa soglia o se un cliente ha diritto a uno sconto.

---

## ✔️ Comprendere i tipi di dato Boolean

Un **Boolean** rappresenta un valore logico:

* **True**
* **False**

I booleani derivano spesso da **operazioni di confronto**, che verificano la relazione tra due valori. In Python, gli operatori di confronto più comuni sono:

* Uguale a → `==`
* Diverso da → `!=`
* Maggiore di → `>`
* Minore di → `<`
* Maggiore o uguale a → `>=`
* Minore o uguale a → `<=`

Questi operatori restituiscono sempre un valore booleano.

---

## ✔️ Applicazione di esempio

Nell’esempio seguente, controlliamo se una quantità di latte è considerata “scorta bassa”, confrontando la quantità disponibile con una soglia minima:

```python
# Define the quantity of the item and the low stock threshold
milk_quantity = 12
low_stock_threshold = 10

# Check if the item quantity is below the low stock threshold
low_stock = milk_quantity <= low_stock_threshold

# Print the result
print("Is the item low in stock?", low_stock)
```

---

## 🧪 **Compito**

In questa attività verificherai se un acquisto è idoneo a ricevere uno sconto, utilizzando un confronto che restituisce un valore booleano.

### **Cosa Devi Fare**

1. Definire una variabile chiamata **total_cost** e assegnarle il valore `25.00`.
2. Creare una variabile booleana chiamata **discountEligible** confrontando `total_cost` con la soglia dello sconto (`20.00`) usando l’operatore `>=`.
3. Stampare il risultato mostrando se l’acquisto è idoneo o meno.

### **Requisiti di Output**

Devi stampare:

```
Is the purchase eligible for a discount? <discountEligible>
```

