# Modulo 7 – Moduli e Package (6 ore)

Questo modulo insegna a:

* **organizzare il codice**
* **riusare funzionalità**
* lavorare in modo **professionale**

👉 È il passaggio da “script” a **progetto Python**.

---

## 7.1 Moduli (3 ore)

### Import e organizzazione del codice

Un **modulo** è un file `.py`.

```python
# matematica.py
def somma(a, b):
    return a + b
```

Uso:

```python
import matematica
print(matematica.somma(3, 4))
```

---

### Forme di import

```python
import matematica
import matematica as m
from matematica import somma
from matematica import somma, sottrai
```

⚠️ Evitare:

```python
from matematica import *
```

---

### Creazione di moduli

Struttura semplice:

```
progetto/
│
├── main.py
├── matematica.py
```

`main.py`:

```python
from matematica import somma
print(somma(5, 6))
```

---

### `__name__ == "__main__"`

Ogni modulo ha una variabile speciale `__name__`.

```python
def main():
    print("Eseguito direttamente")

if __name__ == "__main__":
    main()
```

* eseguito direttamente → `__main__`
* importato → nome del modulo

👉 Fondamentale per:

* test
* script riutilizzabili
* CLI

---

### Moduli utili della standard library

Alcuni da conoscere subito:

```python
import math
import random
import datetime
import os
import sys
import pathlib
```

Esempio:

```python
import random
print(random.randint(1, 10))
```

👉 Python “batteries included”.

---

## 7.2 Package e virtual environments (3 ore)

### Struttura dei package

Un **package** è una cartella con moduli.

```
app/
│
├── main.py
├── utils/
│   ├── __init__.py
│   ├── stringhe.py
│   └── numeri.py
```

Import:

```python
from utils.stringhe import formatta
```

---

### `__init__.py`

Indica che una cartella è un package.

```python
# utils/__init__.py
```

Può contenere:

```python
from .stringhe import formatta
```

👉 Permette import più puliti.

---

### Virtual environments (venv)

Un **virtual environment** isola:

* librerie
* versioni
* dipendenze

Creazione:

```bash
python -m venv venv
```

Attivazione:

* Windows:

```bash
venv\Scripts\activate
```

* Linux / macOS:

```bash
source venv/bin/activate
```

---

### Pip e gestione dipendenze

Installare librerie:

```bash
pip install requests
```

Verifica:

```bash
pip list
```

---

### `requirements.txt`

File che elenca le dipendenze.

Creazione:

```bash
pip freeze > requirements.txt
```

Contenuto:

```
requests==2.31.0
```

Installazione:

```bash
pip install -r requirements.txt
```

👉 Fondamentale per:

* collaborazione
* deploy
* riproducibilità

---

## Riepilogo didattico

Questo modulo permette di:

* strutturare progetti reali
* lavorare in team
* gestire ambienti e dipendenze

È la base per:

* applicazioni web
* CLI avanzate
* librerie Python

