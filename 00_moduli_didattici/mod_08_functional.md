# Modulo 8 – Programmazione Funzionale (4 ore)

La **programmazione funzionale** è uno stile di programmazione che:

* usa le funzioni come elementi principali
* evita effetti collaterali
* lavora con dati immutabili (quando possibile)

👉 In Python è **ibrida**: funzionale + imperativa + OOP.

---

## Concetti chiave

* **funzioni di ordine superiore** → funzioni che ricevono o restituiscono funzioni
* **lazy evaluation** → i dati vengono calcolati solo quando servono
* **immutabilità** → i dati non vengono modificati

---

## Map, Filter, Reduce

### `map()`

Applica una funzione a ogni elemento.

```python
numeri = [1, 2, 3, 4]

quadrati = list(map(lambda x: x**2, numeri))
```

Equivalente (più pythonico):

```python
quadrati = [x**2 for x in numeri]
```

---

### `filter()`

Filtra gli elementi secondo una condizione.

```python
pari = list(filter(lambda x: x % 2 == 0, numeri))
```

Equivalente:

```python
pari = [x for x in numeri if x % 2 == 0]
```

---

### `reduce()`

Riduce una sequenza a un solo valore.

```python
from functools import reduce

somma = reduce(lambda a, b: a + b, numeri)
```

👉 Da usare solo quando migliora chiarezza.

---

## Iteratori e generatori

Un **iteratore** è un oggetto che produce valori uno alla volta.

```python
numeri = iter([1, 2, 3])
print(next(numeri))
```

Molti oggetti Python sono iterabili:

* liste
* tuple
* stringhe
* file

---

## Generator functions e `yield`

Un **generatore** produce valori senza memorizzarli tutti.

```python
def contatore(n):
    for i in range(n):
        yield i
```

Uso:

```python
for x in contatore(5):
    print(x)
```

👉 Vantaggi:

* meno memoria
* gestione di grandi dati

---

## Lazy evaluation

I generatori producono valori **solo quando richiesti**.

```python
gen = (x**2 for x in range(1000000))
```

Nessun calcolo finché non si itera.

---

## Funzioni di ordine superiore

Funzioni che:

* accettano funzioni
* restituiscono funzioni

```python
def applica(funzione, valore):
    return funzione(valore)
```

Uso:

```python
applica(lambda x: x * 2, 5)
```

---

## Approccio funzionale vs imperativo

### Imperativo

```python
risultato = []
for x in numeri:
    if x % 2 == 0:
        risultato.append(x**2)
```

### Funzionale

```python
risultato = [x**2 for x in numeri if x % 2 == 0]
```

👉 Funzionale:

* più compatto
* più leggibile (se usato bene)

---

## Best practices didattiche

✔ preferire list/dict comprehension
✔ usare generatori per grandi dataset
✔ evitare lambda complesse
✔ privilegiare leggibilità

❌ codice “furbesco”

---

## Riepilogo didattico

Questo modulo serve a:

* scrivere codice più espressivo
* migliorare prestazioni
* leggere codice Python moderno

È ideale come:

* modulo di approfondimento
* ponte verso data science
* rifinitura dello stile pythonico

