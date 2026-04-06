# File I/O 

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

