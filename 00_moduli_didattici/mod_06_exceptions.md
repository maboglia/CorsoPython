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
