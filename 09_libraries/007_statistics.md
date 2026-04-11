# Modulo `statistics`: L'Analizzatore di Voti

Questo modulo è utilissimo per introdurre i concetti base dell'analisi dati senza usare librerie pesanti come Pandas.

```python
import statistics

def analizza_voti():
    # Lista di voti di una classe
    voti = [24, 27, 30, 18, 22, 24, 26, 30, 24, 29]

    # 1. Calcola la media aritmetica
    # TODO: Usa statistics.mean()
    media = 

    # 2. Trova la moda (il voto più frequente)
    # TODO: Usa statistics.mode()
    voto_comune = 

    # 3. Calcola la mediana
    # TODO: Usa statistics.median()
    mediana = 

    print(f"Media dei voti: {media}")
    print(f"Voto più frequente: {voto_comune}")
    print(f"Valore mediano: {mediana}")

# Sfida Extra: Aggiungi un controllo che verifichi se la media è >= 18 (promosso)

```

---

# 📌 Libreria `statistics` – Scheda Completa

Serve per calcolare **statistiche descrittive**.

```python
import statistics
```

---

## 1) Media (`mean`)

```python
import statistics

dati = [10, 20, 30]
print(statistics.mean(dati))   # 20
```

---

## 2) Media pesata (`fmean`)

Più veloce e lavora su float:

```python
statistics.fmean([10, 20, 30])
```

---

## 3) Mediana (`median`)

```python
statistics.median([1, 2, 10])      # 2
statistics.median([1, 2, 10, 20])  # 6.0
```

---

## 4) Moda (`mode`)

```python
statistics.mode([1, 2, 2, 3])
```

📌 restituisce l’elemento più frequente.

⚠️ se ci sono più mode possibili può dare errore (versioni vecchie) o scegliere la prima.

---

## 5) Variance e deviazione standard

### Varianza popolazione

```python
statistics.pvariance([1, 2, 3])
```

### Varianza campionaria

```python
statistics.variance([1, 2, 3])
```

### Deviazione standard popolazione

```python
statistics.pstdev([1, 2, 3])
```

### Deviazione standard campionaria

```python
statistics.stdev([1, 2, 3])
```

📌 Differenza:

* popolazione → divide per `n`
* campione → divide per `n-1`

---

## 6) Quantili (`quantiles`)

```python
import statistics

dati = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(statistics.quantiles(dati, n=4))
```

📌 quartili.

---

## 7) Best practice statistics

✅ usare `mean`, `median`, `mode` per descrittive
✅ usare `stdev` per analisi dati
⚠️ per dataset grandi meglio `numpy`
