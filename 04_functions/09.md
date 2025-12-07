## 🔹 **Debugging**

### **Idea chiave**

Il *debugging* è il processo di **identificazione e correzione degli errori** nel codice.

---

## **Tipi comuni di errori in Python**

1. **SyntaxError** – errore di sintassi, ad esempio parentesi mancanti.
2. **NameError** – variabile o funzione non definita.
3. **TypeError** – tipo di dato incompatibile.
4. **IndexError / KeyError** – indice o chiave non esistente in lista/dizionario.
5. **ValueError** – valore non corretto per una funzione.

---

## **Strumenti per il debugging**

### 1. **Print statement**

Il metodo più semplice: stampare variabili per controllarne i valori.

```python
def somma(a, b):
    print("a:", a, "b:", b)
    return a + b

somma(5, 7)
```

### 2. **Uso di `assert`**

Verifica che una condizione sia vera, altrimenti genera errore.

```python
x = 10
assert x > 0, "x deve essere positivo"
```

### 3. **Modulo `pdb`**

Debugger interattivo: permette di fermare l’esecuzione e ispezionare variabili.

```python
import pdb

x = 5
pdb.set_trace()  # Qui il codice si ferma
y = 10
```

---

## **Buone pratiche di debugging**

* Testa piccole parti di codice prima di integrarle.
* Scrivi messaggi chiari quando usi `assert` o `print`.
* Evita di lasciare `print` di debug in produzione.
* Usa un IDE con debugger integrato per risparmiare tempo.

