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

---

## L'istruzione **`pass`**

L'istruzione **`pass`** in Python è letteralmente un'operazione nulla. Quando viene eseguita, non succede assolutamente nulla.

Potrebbe sembrare inutile, ma in un linguaggio come Python — dove i blocchi di codice sono definiti dall'indentazione e non dalle parentesi graffe — è uno strumento fondamentale per mantenere la validità sintattica.

---

## Perché si usa `pass`?

In Python, non puoi avere un blocco di codice vuoto (come dopo un `if`, `for`, `def` o `class`). Se lasci un blocco vuoto, il computer si arrabbia e ti restituisce un `IndentationError`.

`pass` serve a dire all'interprete: *"So che qui dovrebbe esserci del codice, ma per ora non voglio che accada nulla"*.

### 1. Placeholder (Segnaposto) per lo sviluppo

È utilissimo durante la fase di scrittura del codice. Se stai strutturando un programma ma non hai ancora implementato la logica di una funzione, la "tappi" con un `pass`.

```python
def funzione_complessa():
    # TODO: implementare la logica più tardi
    pass

if utente_loggato:
    # Gestiremo il login in un secondo momento
    pass
else:
    print("Effettua l'accesso")

```

### 2. Creazione di classi minime

Si usa spesso per definire nuove eccezioni o classi che non hanno bisogno di metodi aggiuntivi rispetto alla classe base.

```python
class ErrorePersonalizzato(Exception):
    pass

```

### 3. Cicli o condizionali "vuoti"

A volte vuoi che un ciclo giri senza fare nulla, o che una condizione specifica venga ignorata esplicitamente.

---

## `pass` vs `continue` vs `break`

È facile confonderli, ma hanno ruoli molto diversi all'interno dei cicli:

| Istruzione     | Cosa fa effettivamente?                                                            |
| -------------- | ---------------------------------------------------------------------------------- |
| **`pass`**     | **Nulla.** Il codice continua l'esecuzione riga dopo riga.                         |
| **`continue`** | **Salta** il resto del blocco corrente e passa alla prossima iterazione del ciclo. |
| **`break`**    | **Interrompe** completamente il ciclo e ne esce.                                   |

### Esempio di differenza:

```python
for i in range(3):
    if i == 1:
        pass  # Non fa nulla, stampa comunque 1
    print(i)

# Output con pass: 0, 1, 2
# Output con continue: 0, 2 (salta l'1)

```

---

> **Nota di stile:** Anche se `pass` è comodo, se lo usi come segnaposto è buona norma aggiungere un commento `# TODO` per ricordarti di sostituirlo con del codice vero in futuro!
