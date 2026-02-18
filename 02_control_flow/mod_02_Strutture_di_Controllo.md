# Modulo 2 – Strutture di Controllo (10 ore)

Le **strutture di controllo** permettono di:

* prendere decisioni
* ripetere istruzioni
* controllare il flusso di esecuzione di un programma

👉 Senza di esse, i programmi sarebbero solo una sequenza lineare di istruzioni.

---

## 2.1 Condizioni (4 ore)

### If, elif, else

La struttura condizionale più comune è:

```python
if condizione:
    istruzioni
elif altra_condizione:
    istruzioni
else:
    istruzioni
```

* La condizione deve restituire `True` o `False`
* I blocchi sono definiti dall’**indentazione**

Esempio:

```python
eta = int(input("Inserisci età: "))

if eta >= 18:
    print("Maggiorenne")
else:
    print("Minorenne")
```

---

### Operatori di confronto

| Operatore | Significato       |
| --------- | ----------------- |
| `==`      | uguale            |
| `!=`      | diverso           |
| `>`       | maggiore          |
| `<`       | minore            |
| `>=`      | maggiore o uguale |
| `<=`      | minore o uguale   |

Esempio:

```python
x = 10
print(x > 5)    # True
```

---

### Operatori logici

| Operatore | Significato     |
| --------- | --------------- |
| `and`     | entrambe vere   |
| `or`      | almeno una vera |
| `not`     | negazione       |

Esempio:

```python
eta = 20
patente = True

if eta >= 18 and patente:
    print("Puoi guidare")
```

---

### Espressioni booleane

Un’espressione booleana è un’espressione che restituisce `True` o `False`.

```python
numero = 8
risultato = numero > 0 and numero % 2 == 0
print(risultato)
```

👉 Molto utile per:

* controlli
* condizioni complesse
* validazione dati

---

### Operatore ternario

Versione compatta di `if-else`.

Sintassi:

```python
valore_se_vero if condizione else valore_se_falso
```

Esempio:

```python
numero = 7
tipo = "Pari" if numero % 2 == 0 else "Dispari"
print(tipo)
```

💡 Usarlo solo per condizioni **semplici**.

---

### Pattern matching – `match-case` (Python 3.10+)

Alternativa moderna a molti `if-elif`.

```python
scelta = int(input("Scegli (1-3): "))

match scelta:
    case 1:
        print("Inserisci")
    case 2:
        print("Modifica")
    case 3:
        print("Elimina")
    case _:
        print("Scelta non valida")
```

👉 Migliora:

* leggibilità
* manutenzione
* chiarezza dei menu

---

## 2.2 Cicli (6 ore)

I **cicli** permettono di ripetere istruzioni.

---

### While loop

Ripete finché la condizione è vera.

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

⚠️ Attenzione ai **cicli infiniti**.

---

### For loop e iterazione

Il `for` in Python itera su **sequenze**.

```python
for i in range(1, 6):
    print(i)
```

Esempio con lista:

```python
nomi = ["Anna", "Luca", "Marco"]

for nome in nomi:
    print(nome)
```

---

### Range

```python
range(inizio, fine, passo)
```

Esempi:

```python
range(5)          # 0 → 4
range(1, 10)      # 1 → 9
range(0, 20, 2)   # numeri pari
```

---

### Enumerate

Permette di avere **indice + valore**.

```python
nomi = ["Anna", "Luca", "Marco"]

for indice, nome in enumerate(nomi, start=1):
    print(indice, nome)
```

---

### Break e continue

**break** → esce dal ciclo
**continue** → salta l’iterazione corrente

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)
```

```python
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)
```

---

### Else nei cicli

L’`else` viene eseguito **solo se il ciclo termina normalmente**.

```python
numeri = [1, 3, 5, 7]

for n in numeri:
    if n == 4:
        print("Trovato")
        break
else:
    print("Numero non trovato")
```

---

### List comprehension (introduzione)

Modo compatto per creare liste.

Sintassi:

```python
[espressione for elemento in sequenza]
```

Esempio:

```python
quadrati = [x**2 for x in range(1, 6)]
```

Con condizione:

```python
pari = [x for x in range(10) if x % 2 == 0]
```

👉 Da introdurre come **lettura**, non subito come scrittura.

---

## Riepilogo didattico

Questo modulo serve a:

* imparare a **decidere**
* imparare a **ripetere**
* leggere e scrivere **flussi logici**

Ottimo per:

* flowchart
* debug
* primi programmi “veri”

---

## Scheda Esercizi – Modulo 2

## Strutture di Controllo (10 ore)

---

## 🟢 2.1 Condizioni – Livello Base

### Esercizio 1 – Numero positivo o negativo

Chiedi un numero intero all’utente e stampa:

* “Numero positivo”
* “Numero negativo”
* “Numero zero”

---

### Esercizio 2 – Maggiorenne

Chiedi l’età e stampa:

* “Maggiorenne” se ≥ 18
* “Minorenne” altrimenti

---

### Esercizio 3 – Confronto tra due numeri

Chiedi due numeri e stampa:

* quale dei due è maggiore
* oppure “I numeri sono uguali”

---

### Esercizio 4 – Voto scolastico

Chiedi un voto (0–10) e stampa:

* Insufficiente
* Sufficiente
* Buono
* Ottimo

(Scegli tu le soglie)

---

## 🟡 Condizioni – Livello Intermedio

### Esercizio 5 – Operatori logici

Chiedi:

* età
* se l’utente ha la patente (`sì` / `no`)

Stampa:

```
Puoi guidare
```

solo se entrambe le condizioni sono vere.

---

### Esercizio 6 – Accesso riservato

Chiedi:

* username
* password

Se username è `"admin"` **e** password è `"1234"` stampa:

```
Accesso consentito
```

altrimenti:

```
Accesso negato
```

---

### Esercizio 7 – Orario

Chiedi un’ora (0–23) e stampa:

* Mattina
* Pomeriggio
* Sera
* Notte

---

## 🟠 Espressioni booleane e ternary operator

### Esercizio 8 – Booleani

Scrivi un’espressione booleana che verifichi se un numero:

* è maggiore di 0
* ed è pari

Stampa il risultato (`True` o `False`).

---

### Esercizio 9 – Operatore ternario

Chiedi un numero e assegna a una variabile:

* `"Pari"` se il numero è pari
* `"Dispari"` altrimenti

Usa **solo** il ternary operator.

---

## 🔵 Pattern matching (`match-case`)

### Esercizio 10 – Menu

Chiedi un numero da 1 a 3 e stampa:

1. Inserisci
2. Modifica
3. Elimina
   Altro → “Scelta non valida”

Usa `match-case`.

---

### Esercizio 11 – Giorno della settimana

Chiedi un numero (1–7) e stampa il giorno corrispondente.

---

## 🟢 2.2 Cicli – Livello Base

### Esercizio 12 – While

Stampa i numeri da 1 a 10 usando `while`.

---

### Esercizio 13 – Contatore

Chiedi un numero e stampa tutti i numeri da 0 a quel numero.

---

### Esercizio 14 – For

Stampa i numeri da 1 a 20 usando `for`.

---

### Esercizio 15 – Range

Stampa solo i numeri pari da 0 a 50.

---

## 🟡 Cicli – Livello Intermedio

### Esercizio 16 – Somma

Chiedi 5 numeri all’utente e stampa la loro somma.

---

### Esercizio 17 – Enumerate

Data la lista:

```python
nomi = ["Anna", "Luca", "Marco", "Sara"]
```

Stampa:

```
1 - Anna
2 - Luca
...
```

---

### Esercizio 18 – Break

Chiedi numeri all’utente finché inserisce `0`.
Quando inserisce `0`, il ciclo termina.

---

### Esercizio 19 – Continue

Stampa i numeri da 1 a 20 saltando i multipli di 3.

---

### Esercizio 20 – Else nei cicli

Chiedi un numero e verifica se è presente in una lista predefinita.
Usa `else` associato al ciclo.

---

## 🔴 List comprehension (introduzione)

### Esercizio 21 – Quadrati

Crea una lista contenente i quadrati dei numeri da 1 a 10:

```
[1, 4, 9, 16, ...]
```

---

### Esercizio 22 – Numeri pari

Da una lista di numeri, crea una nuova lista con solo i numeri pari.

---

### Esercizio 23 – Stringhe

Da una lista di parole, crea una nuova lista con:

* solo parole lunghe più di 5 caratteri

---

## ⭐ Mini–verifica finale

### Esercizio 24 – Menu interattivo

Crea un programma che mostri un menu finché l’utente non sceglie “0 – Esci”.

Usa:

* `while`
* `if` o `match-case`
* `break`

---

## 💡 Suggerimento didattico

Questo modulo è perfetto per:

* far **ragionare sul flusso**
* disegnare **flowchart**
* confrontare `if` vs `match`
* anticipare strutture dati e funzioni

