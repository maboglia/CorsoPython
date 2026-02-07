## 📘 **Types of Functions**

In Python esistono diverse tipologie di funzioni, utili in contesti differenti. Conoscerle aiuta a strutturare meglio il codice e a scegliere la soluzione più adatta.

### 🔹 **Funzioni senza valore di ritorno**

Sono funzioni che *eseguono un’azione* ma non restituiscono alcun valore (`return` assente).

```python
def show_total(total):
    print(f"Your total is: {total}")
```

### 🔹 **Funzioni con valore di ritorno**

Restituiscono un risultato utilizzabile nel resto del programma.

```python
def calculate_discount(price):
    return price * 0.10

discount = calculate_discount(100)
print(discount)
```

### 🔹 **Funzioni pure**

Danno lo stesso output a parità di input e *non modificano* variabili esterne. Sono più prevedibili.

```python
def square(n):
    return n * n
```

### 🔹 **Funzioni impure**

Producono effetti esterni (stampa, modifica variabili globali, input/output).

```python
count = 0

def increment():
    global count
    count += 1
```

### 🔹 **Funzioni annidate**

Definite all’interno di altre funzioni.

```python
def outer():
    def inner():
        print("Inside inner function")
    inner()
```

### 🔹 **Funzioni lambda (anonime)**

Funzioni brevi create senza `def`.

```python
square = lambda x: x * x
print(square(5))
```

Questi tipi coprono la maggior parte dei casi d’uso nelle applicazioni Python e saranno utili negli esercizi dei moduli successivi.
