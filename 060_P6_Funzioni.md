# 📘 Corso Python – Modulo 6

## Funzioni

---

### 1. Cos’è una funzione?

* Un blocco di codice che esegue un compito specifico.
* Può ricevere **input** (parametri) e restituire **output** (valore di ritorno).
* Si definisce con la parola chiave `def`.

```python
def saluta():
    print("Ciao dal corso Python!")

saluta()
```

---

### 2. Parametri e ritorno

```python
def somma(a, b):
    return a + b

risultato = somma(5, 3)
print(risultato)  # 8
```

---

### 3. Parametri di default

```python
def saluto(nome="Studente"):
    print("Ciao", nome)

saluto()          # Ciao Studente
saluto("Anna")    # Ciao Anna
```

---

### 4. Argomenti posizionali e nominati

```python
def info(nome, età):
    print(f"{nome} ha {età} anni")

info("Luca", 22)              # posizionali
info(età=30, nome="Giulia")   # nominati
```

---

### 5. Argomenti variabili

* `*args` → lista di valori
* `**kwargs` → dizionario di valori

```python
def somma_tutti(*args):
    return sum(args)

print(somma_tutti(1, 2, 3, 4))  # 10
```

```python
def mostra_dati(**kwargs):
    for k, v in kwargs.items():
        print(k, ":", v)

mostra_dati(nome="Anna", corso="Python")
```

---

### 6. Funzioni anonime (`lambda`)

* Piccole funzioni in una sola riga.

```python
quadrato = lambda x: x**2
print(quadrato(5))  # 25
```

---

### 7. Scope delle variabili

* **Locale**: visibile solo dentro la funzione.
* **Globale**: definita fuori da tutte le funzioni.

```python
x = 10  # variabile globale

def funzione():
    x = 5  # variabile locale
    print("Dentro:", x)

funzione()
print("Fuori:", x)
```

---

### 8. Buone pratiche

✅ Scrivere funzioni piccole e con uno scopo chiaro
✅ Usare nomi descrittivi
✅ Documentare con docstring

```python
def area_rettangolo(base, altezza):
    """Calcola l'area di un rettangolo"""
    return base * altezza
```

