## 🔹 **Keyword Arguments**

I *keyword arguments* permettono di chiamare una funzione specificando il nome dei parametri, rendendo il codice più chiaro e flessibile.
Non è necessario rispettare l’ordine dei parametri: basta indicarne il nome.

### ✔️ Esempio base

```python
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet(age=30, name="Alice")
```

➡️ Anche se l’ordine è invertito, Python capisce comunque quale valore assegnare a ciascun parametro.

### ✔️ Quando usarli

* Per rendere il codice più leggibile
* Per evitare errori in funzioni con molti parametri
* Per combinare parametri *positional* e *keyword*

### ✔️ Positional + Keyword

```python
def order(item, quantity, price):
    print(f"{quantity}x {item} cost {price}€ each.")

order("Apple", price=1.20, quantity=5)
```

I positional (`"Apple"`) vanno prima dei keyword, altrimenti Python genera un errore.

I *keyword arguments* migliorano la chiarezza del codice, soprattutto in funzioni ricche di parametri o in progetti complessi.
