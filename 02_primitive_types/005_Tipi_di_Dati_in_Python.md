# 🧩 **Tipi di Dati in Python**

Per iniziare a programmare è fondamentale conoscere i **tipi di dati**: rappresentano le categorie con cui Python organizza e gestisce le informazioni.

Possiamo immaginare Python come un supermercato ben ordinato: ogni prodotto è collocato nel reparto corretto per essere facilmente trovato e utilizzato. Allo stesso modo, Python suddivide i dati in tipologie precise, così da poterli elaborare nel modo più adatto.

---

## 🧠 **Perché i tipi di dati sono importanti?**

In Python **ogni valore ha un tipo**.
Conoscerlo è essenziale perché determina **quali operazioni puoi eseguire**: non puoi sommare una stringa e un numero, ad esempio, così come non metteresti le arance nel reparto detersivi.

---

# 📚 Tipi di dati fondamentali

## 🔢 **Interi (`int`)**

Rappresentano numeri senza decimali.
Esempi tipici: quantità, conteggi, pezzi in un carrello.

**Esempi:**
`3`, `10`, `150`

---

## 🧮 **Numeri in virgola mobile (`float`)**

Numeri con la virgola (decimale).
Utile per prezzi, misure, pesi.

**Esempi:**
`1.99`, `2.50`, `0.75`

---

## 📝 **Stringhe (`str`)**

Sequenze di caratteri.
Sono usate per rappresentare testo, come nomi di prodotti o messaggi.

**Esempi:**
`"apple"`, `"banana"`, `"oat milk"`

---

## ✔️ **Booleani (`bool`)**

Possono essere solo due valori: `True` o `False`.
Utili per verificare condizioni, disponibilità, esiti di confronti.

**Esempi:**
`True`, `False`, `5 > 3`

---

# 🧪 Esempi pratici con `type()`

La funzione `type()` permette di vedere che tipo di dato Python assegna a un valore.

```python
# Intero
print(type(25))

# Numero in virgola mobile
print(type(6.25))

# Stringa
print(type("Olive Oil"))

# Booleano (risultato di un confronto)
print(type(120 > 95))
```

---

# 🎯 Comprendere i tipi di dati

Conoscere i tipi di dati ti aiuta a:

* scegliere le operazioni corrette
* evitare errori
* progettare programmi più chiari e strutturati

Come nel supermercato, anche in un programma tutto funziona meglio quando ogni dato è nel reparto giusto.

---

# 📝 Esercizio – Trascina e completa

Associa ogni valore al tipo corretto:

| Campo            | Tipo     | Valore corretto |
| ---------------- | -------- | --------------- |
| **Name**         | `string` | `"Oranges"`     |
| **Quantity**     | `int`    | `10`            |
| **Price**        | `float`  | `1.99`          |
| **Is Available** | `bool`   | `True`          |

*(Il valore `[1, 4, 5]` è una lista e non appartiene a nessuno dei campi richiesti.)*

