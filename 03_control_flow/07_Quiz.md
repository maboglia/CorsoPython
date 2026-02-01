## **7 – Quiz**

Questo **quiz** serve a verificare la comprensione di:

* operatori di confronto
* istruzioni condizionali
* operatore ternario
* operatori logici
* short-circuit evaluation
* confronti concatenati

Rispondi mentalmente o eseguendo il codice.

---

### **Domanda 1**

```python
print(5 == "5")
```

**Risultato:**
⬜ `True`
⬜ `False`

<details>
<summary>Soluzione</summary>

`False` – tipi diversi

</details>

---

### **Domanda 2**

```python
x = 10
print(0 < x < 20)
```

⬜ `True`
⬜ `False`

<details>
<summary>Soluzione</summary>

`True` – confronto concatenato valido

</details>

---

### **Domanda 3**

```python
print(False and print("Hello"))
```

⬜ Stampa `Hello`
⬜ Non stampa nulla

<details>
<summary>Soluzione</summary>

Non stampa nulla – short-circuit su `and`

</details>

---

### **Domanda 4**

```python
x = 0
print(x and 10)
```

⬜ `0`
⬜ `False`
⬜ `10`

<details>
<summary>Soluzione</summary>

`0` – `and` restituisce il primo valore falsy

</details>

---

### **Domanda 5**

```python
eta = 17
stato = "OK" if eta >= 18 else "NO"
print(stato)
```

⬜ `OK`
⬜ `NO`

<details>
<summary>Soluzione</summary>

`NO`

</details>

---

### **Domanda 6**

```python
print(not (True or False))
```

⬜ `True`
⬜ `False`

<details>
<summary>Soluzione</summary>

`False`

</details>

---

### **Domanda 7**

```python
a = 5
b = 10
print(a < b == 10)
```

⬜ `True`
⬜ `False`

<details>
<summary>Soluzione</summary>

`True` → equivale a `a < b and b == 10`

</details>

---

### **Autovalutazione**

* 6–7 risposte corrette → Ottima padronanza
* 4–5 risposte corrette → Buona comprensione
* <4 → Ripassa i paragrafi 1–6

---

**scheda 8 – For Loops**?
