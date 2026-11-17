# Modulo 4 – Funzioni (10 ore)

Le **funzioni** permettono di:

* organizzare il codice
* evitare ripetizioni
* migliorare leggibilità e manutenzione

👉 Senza funzioni, i programmi diventano lunghi, rigidi e difficili da mantenere.

---

## 4.1 Funzioni base (4 ore)

### Definizione e chiamata

Sintassi:

```python
def saluta():
    print("Ciao!")
```

Chiamata:

```python
saluta()
```

👉 Una funzione è un **blocco di codice riutilizzabile** che viene eseguito solo quando viene chiamato.

---

### Parametri e argomenti

```python
def saluta(nome):
    print(f"Ciao {nome}")
```

Chiamata:

```python
saluta("Anna")
```

* **parametro** → variabile nella definizione
* **argomento** → valore passato alla funzione

---

### Return values

Una funzione può **restituire un valore** con `return`.

```python
def somma(a, b):
    return a + b
```

Uso:

```python
risultato = somma(3, 4)
print(risultato)
```

⚠️ `return` termina l’esecuzione della funzione.

---

### Scope e namespace

Le variabili hanno un **ambito di visibilità**.

```python
x = 10  # variabile globale

def esempio():
    x = 5  # variabile locale
    print(x)

esempio()
print(x)
```

👉 Regola fondamentale:

* le variabili locali **non escono** dalla funzione

Keyword `global` (da spiegare ma sconsigliare):

```python
def cambia():
    global x
    x = 20
```

---

### Docstrings

Servono per **documentare le funzioni**.

```python
def somma(a, b):
    """
    Calcola la somma di due numeri.
    :param a: primo numero
    :param b: secondo numero
    :return: somma
    """
    return a + b
```

Visualizzazione:

```python
help(somma)
```

👉 Ottima abitudine fin dall’inizio.

---

## 4.2 Funzioni avanzate (6 ore)

### Parametri di default

```python
def saluta(nome="utente"):
    print(f"Ciao {nome}")
```

Chiamate:

```python
saluta()
saluta("Marco")
```

---

### Keyword arguments

```python
def presenta(nome, eta):
    print(f"{nome} ha {eta} anni")
```

```python
presenta(eta=25, nome="Anna")
```

👉 Migliora leggibilità e flessibilità.

---

### *args

Permette di passare un numero variabile di argomenti **posizionali**.

```python
def somma(*numeri):
    totale = 0
    for n in numeri:
        totale += n
    return totale
```

Uso:

```python
somma(1, 2, 3, 4)
```

---

### **kwargs

Permette di passare argomenti **con nome**.

```python
def stampa_dati(**dati):
    for chiave, valore in dati.items():
        print(chiave, valore)
```

Uso:

```python
stampa_dati(nome="Anna", eta=30, corso="Python")
```

---

### Funzioni come oggetti di prima classe

In Python:

* le funzioni possono essere assegnate a variabili
* passate come argomenti
* restituite da altre funzioni

```python
def saluta():
    print("Ciao")

f = saluta
f()
```

Esempio:

```python
def esegui(funzione):
    funzione()
```

---

### Lambda functions

Funzioni anonime, brevi.

```python
quadrato = lambda x: x ** 2
```

Uso tipico:

```python
numeri = [1, 2, 3, 4]
quadrati = list(map(lambda x: x**2, numeri))
```

👉 Usarle solo per **operazioni semplici**.

---

### Decoratori (introduzione)

Un decoratore è una funzione che **modifica il comportamento** di un’altra funzione.

Esempio concettuale:

```python
def decoratore(funzione):
    def wrapper():
        print("Prima")
        funzione()
        print("Dopo")
    return wrapper
```

Uso:

```python
@decoratore
def saluta():
    print("Ciao")
```

Output:

```
Prima
Ciao
Dopo
```

👉 Qui l’obiettivo è **capire l’idea**, non la complessità.

---

### Type hints per funzioni

```python
def somma(a: int, b: int) -> int:
    return a + b
```

Con stringhe:

```python
def saluta(nome: str) -> None:
    print(f"Ciao {nome}")
```

👉 Servono per:

* documentazione
* editor
* strumenti di analisi

---

## Riepilogo didattico

Questo modulo permette di:

* scrivere codice modulare
* creare librerie riutilizzabili
* preparare il terreno per OOP e moduli

È un **modulo chiave**: da qui in poi Python diventa “strutturato”.

---

