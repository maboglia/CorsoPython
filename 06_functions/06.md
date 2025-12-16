## 🔹 **xargs (`*args`)**

### **Idea chiave**

`*args` permette di definire funzioni che accettano **un numero variabile di argomenti posizionali**, senza sapere in anticipo quanti saranno.

---

## **Che cos’è `*args`?**

Quando in una funzione usi `*args`, Python raccoglie **tutti gli argomenti extra** passati senza nome e li inserisce in una **tupla**.

È utile quando:

* vuoi passare quantità variabili di valori;
* non conosci il numero di argomenti in anticipo;
* vuoi scrivere funzioni più flessibili e generiche.

---

## **Esempio base**

```python
def somma(*args):
    totale = 0
    for numero in args:
        totale += numero
    return totale

print(somma(1, 2))          # 3
print(somma(1, 2, 3, 4, 5)) # 15
```

### Cosa succede?

* Tutti gli argomenti vengono raccolti in una tupla chiamata `args`.
* La funzione può gestire **2, 5 o 100 argomenti**, senza modificarla.

---

## **Regole importanti**

* `args` è **solo un nome convenzionale**: può chiamarsi anche `*numeri`.
  Ma `*args` è lo standard.
* `*args` deve venire **dopo gli argomenti normali** nella definizione.

Esempio valido:

```python
def greet(msg, *names):
    for n in names:
        print(msg, n)
```

---

## **Usi tipici**

* aggregazione di valori numerici;
* passaggio di liste di parametri variabili;
* wrapper e decorator;
* funzioni generiche che devono gestire molti formati.

