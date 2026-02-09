# 📘 Corso Python – Modulo 9

## Moduli e Librerie

---

### 1. Cos’è un modulo?

* Un **file Python** (`.py`) che contiene funzioni, classi o variabili.
* Permette di **organizzare** il codice e **riutilizzarlo**.

```python
# modulo mio_modulo.py
def saluta(nome):
    return f"Ciao {nome}!"
```

```python
# programma principale
import mio_modulo
print(mio_modulo.saluta("Anna"))
```

---

### 2. Importazione

* Import completo:

  ```python
  import math
  print(math.sqrt(16))  # 4.0
  ```

* Import parziale:

  ```python
  from math import sqrt
  print(sqrt(25))  # 5.0
  ```

* Alias:

  ```python
  import math as m
  print(m.pi)
  ```

---

### 3. Moduli standard utili

* **math** → funzioni matematiche
* **random** → numeri casuali
* **datetime** → date e orari
* **os** → interazione con sistema operativo
* **sys** → parametri ed esecuzione
* **statistics** → medie, varianze, ecc.

Esempi:

```python
import random, datetime

print(random.randint(1, 6))  # simulazione dado
print(datetime.date.today()) # data di oggi
```

---

### 4. Pacchetti

* Un **pacchetto** è una cartella con più moduli e un file `__init__.py`.
* Struttura:

  ```
  mio_pacchetto/
      __init__.py
      modulo1.py
      modulo2.py
  ```

---

### 5. Librerie esterne

* Installazione con **pip**:

  ```bash
  pip install requests
  ```

* Uso:

  ```python
  import requests
  risposta = requests.get("https://api.github.com")
  print(risposta.status_code)
  ```

---

### 6. Dove trovare librerie

* **PyPI (Python Package Index):**
  👉 [https://pypi.org](https://pypi.org)
* Migliaia di librerie disponibili:

  * Flask, Django → web
  * NumPy, Pandas → dati
  * Matplotlib → grafici
  * TensorFlow, PyTorch → AI

---

### 7. Buone pratiche

✅ Organizzare il codice in più file/moduli
✅ Usare nomi chiari per i moduli
✅ Non reinventare la ruota: usare librerie già esistenti
✅ Documentarsi su PyPI

---

