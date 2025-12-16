## 🔹 **Scope**

### **Idea chiave**

Lo *scope* determina **dove una variabile è visibile** all’interno del programma.

---

## **Tipi di Scope in Python**

Python segue il modello **LEGB**:

1. **L – Local**
   Variabili definite dentro una funzione.
   Sono accessibili solo lì.

2. **E – Enclosing**
   Variabili in funzioni esterne (nel caso di funzioni annidate).

3. **G – Global**
   Variabili definite nel file, fuori da qualunque funzione.

4. **B – Built-in**
   Funzioni e nomi integrati di Python (`len`, `print`, ecc.).

---

## **Esempio di scope locale**

```python
def saluta():
    nome = "Marco"  # variabile locale
    print(nome)

saluta()
print(nome)  # Errore: nome non esiste qui!
```

---

## **Uso della parola chiave `global`**

Da usare con prudenza: permette a una funzione di modificare una variabile globale.

```python
counter = 0

def incrementa():
    global counter
    counter += 1
```

---

## **Uso della parola chiave `nonlocal`**

Permette a una funzione interna di modificare una variabile della funzione esterna.

```python
def esterna():
    x = 10
    def interna():
        nonlocal x
        x += 1
    interna()
    print(x)
```

---

## **Linee guida importanti**

* Preferisci **variabili locali**: sono più sicure, chiare e facili da testare.
* Evita variabili globali per contenere stato complesso.
* Usa `nonlocal` solo quando serve davvero.

