# Modulo 10 – Testing e Debugging (4 ore)

Questo modulo insegna **come scrivere codice che funziona davvero** e, soprattutto, **come capire perché non funziona**.

👉 È il passaggio da *“scrivo codice”* a *“scrivo software”*.

---

## Debug con `print` e `logging`

### Debug “povero” ma efficace: `print()`

```python
def dividi(a, b):
    print("a:", a, "b:", b)
    return a / b
```

✔ utile per capire il flusso
❌ da evitare in produzione

---

### Logging professionale

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Avvio programma")
logging.error("Errore critico")
```

Livelli:

* DEBUG
* INFO
* WARNING
* ERROR
* CRITICAL

👉 Il logging **non sporca l’output** ed è configurabile.

---

## Debugger integrato

### Debugger di VS Code / PyCharm

Concetti chiave:

* breakpoint
* step over / step into
* watch variables
* call stack

Esempio concettuale:

```python
def calcola():
    x = 10
    y = 0
    return x / y
```

👉 Fermarsi **prima dell’errore** è il superpotere del debugger.

---

## Unit testing con `unittest`

### Primo test

```python
import unittest

def somma(a, b):
    return a + b

class TestSomma(unittest.TestCase):
    def test_base(self):
        self.assertEqual(somma(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
```

Concetti chiave:

* test automatici
* risultati ripetibili
* regressioni sotto controllo

---

## Introduzione a `pytest`

Più semplice e moderno.

```python
def test_somma():
    assert somma(2, 3) == 5
```

Esecuzione:

```bash
pytest
```

👉 Ideale per didattica e progetti reali.

---

## Test-Driven Development (TDD)

Ciclo TDD:

1. ❌ scrivi un test che fallisce
2. ✅ scrivi il codice minimo
3. 🔁 refactor

Esempio concettuale:

```python
def test_divisione():
    assert dividi(10, 2) == 5
```

👉 Il test guida il design del codice.

---

## Code quality e linting

### `pylint`

Analizza:

* stile
* errori
* complessità

```bash
pylint main.py
```

---

### `black`

Formatter automatico.

```bash
black .
```

👉 Nessuna discussione sullo stile: **black decide**.

---

## Best practices didattiche

✔ testare le funzioni pure
✔ test piccoli e leggibili
✔ logging al posto di print
✔ debugger > intuizione

❌ “funziona sul mio PC”

---

## Riepilogo finale del corso

Con questo modulo lo studente:

* capisce gli errori
* previene bug futuri
* scrive codice mantenibile
* ragiona da sviluppatore professionista

È il **sigillo finale** del percorso Python.

