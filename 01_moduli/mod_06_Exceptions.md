# Modulo 6 – Gestione Errori e File (8 ore)

Questo modulo introduce due competenze **fondamentali per il mondo reale**:

* gestione degli errori
* lettura e scrittura di file

👉 Senza queste, un programma funziona *solo in condizioni ideali*.

---

## 6.1 Eccezioni (4 ore)

### Perché servono le eccezioni

Un’**eccezione** è un errore che avviene **durante l’esecuzione** del programma.

Esempio:

```python
numero = int("abc")  # ValueError
```

👉 Le eccezioni permettono di:

* intercettare errori
* evitare crash
* gestire situazioni impreviste

---

### Try, except, finally

Struttura base:

```python
try:
    operazioni
except TipoErrore:
    gestione_errore
finally:
    istruzioni_finali
```

Esempio:

```python
try:
    n = int(input("Numero: "))
    print(10 / n)
except ValueError:
    print("Inserisci un numero valido")
except ZeroDivisionError:
    print("Divisione per zero")
finally:
    print("Fine programma")
```

---

### Tipi di eccezioni comuni

| Eccezione           | Quando             |
| ------------------- | ------------------ |
| `ValueError`        | valore non valido  |
| `TypeError`         | tipo errato        |
| `ZeroDivisionError` | divisione per zero |
| `IndexError`        | indice fuori range |
| `KeyError`          | chiave mancante    |
| `FileNotFoundError` | file inesistente   |

---

### Raise e custom exceptions

Sollevare manualmente un errore:

```python
eta = -5
if eta < 0:
    raise ValueError("Età non valida")
```

Eccezione personalizzata:

```python
class SaldoNegativoError(Exception):
    pass
```

```python
if saldo < 0:
    raise SaldoNegativoError("Saldo insufficiente")
```

👉 Migliora la chiarezza del codice.

---

### Best practices nella gestione errori

✔ intercettare **solo** le eccezioni necessarie
✔ messaggi chiari
✔ non usare `except:` generico
✔ separare logica e gestione errori

❌ usare le eccezioni per controllare il flusso normale

---

### Context managers e `with`

Gestiscono automaticamente le risorse.

```python
with open("file.txt") as f:
    contenuto = f.read()
```

👉 Il file viene chiuso **anche in caso di errore**.

---

## 6.2 File I/O (4 ore)

### Lettura e scrittura file di testo

Scrittura:

```python
with open("testo.txt", "w") as f:
    f.write("Ciao Python\n")
```

Lettura:

```python
with open("testo.txt", "r") as f:
    contenuto = f.read()
```

Lettura riga per riga:

```python
for riga in f:
    print(riga.strip())
```

---

### Context manager per file

Modalità comuni:

| Modalità | Significato             |
| -------- | ----------------------- |
| `"r"`    | lettura                 |
| `"w"`    | scrittura (sovrascrive) |
| `"a"`    | append                  |
| `"rb"`   | binario                 |

---

### CSV

```python
import csv

with open("dati.csv", newline="") as f:
    reader = csv.reader(f)
    for riga in reader:
        print(riga)
```

Scrittura:

```python
with open("dati.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["nome", "eta"])
    writer.writerow(["Anna", 30])
```

---

### JSON

```python
import json

dati = {"nome": "Mario", "eta": 25}

with open("dati.json", "w") as f:
    json.dump(dati, f)
```

Lettura:

```python
with open("dati.json") as f:
    dati = json.load(f)
```

👉 JSON ↔ dizionari Python.

---

### Path e pathlib

```python
from pathlib import Path

path = Path("file.txt")

if path.exists():
    print(path.read_text())
```

Scrittura:

```python
path.write_text("Ciao")
```

👉 Più moderno e portabile di `os.path`.

---

### File binari (cenni)

```python
with open("immagine.png", "rb") as f:
    dati = f.read()
```

Usati per:

* immagini
* PDF
* file audio

---

## Riepilogo didattico

Questo modulo permette di:

* scrivere programmi robusti
* gestire input/output reali
* preparare applicazioni complete

È il ponte verso:

* CLI
* database
* applicazioni professionali

