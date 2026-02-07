## 📘 **Arguments**

Gli *argomenti* permettono di passare dati alla funzione, rendendola flessibile e personalizzabile.

**Punti chiave**

* Si definiscono tra parentesi dopo il nome della funzione
* Sono variabili disponibili dentro la funzione
* Ordine e numero degli argomenti devono essere rispettati

**Esempi**

```python
# Funzione con un argomento
def saluta(nome):
    print(f"Ciao, {nome}!")

saluta("Marco")  # Output: Ciao, Marco!

# Funzione con più argomenti
def somma(a, b):
    return a + b

risultato = somma(5, 3)  # risultato = 8

# Argomenti con valori di default
def presenta(nome, eta=18):
    print(f"{nome} ha {eta} anni")

presenta("Luca")          # Output: Luca ha 18 anni
presenta("Sara", 25)      # Output: Sara ha 25 anni
```

**Attenzione**: passare troppi o troppo pochi argomenti causa errori!
