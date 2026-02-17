
---

# 🔎 Cos’è `if __name__ == "__main__":`

`if __name__ == "__main__":` è uno dei concetti più importanti della **modularità e riuso del codice**.

In Python ogni file `.py` è un **modulo**.

Quando un file viene eseguito, Python assegna automaticamente una variabile speciale:

```python
__name__
```

Questa variabile vale:

* `"__main__"` → se il file è eseguito direttamente
* il nome del modulo → se il file è importato

---

# 🎯 A cosa serve?

Serve a distinguere:

* 🔹 codice eseguito solo quando il file parte direttamente
* 🔹 codice che deve essere disponibile quando il file è importato

---

# 🧠 Esempio base

### File: `calcoli.py`

```python
def somma(a, b):
    return a + b

print("Modulo caricato")
```

Se esegui:

```bash
python calcoli.py
```

Output:

```
Modulo caricato
```

Se invece fai:

```python
import calcoli
```

⚠ Anche in questo caso verrà stampato `"Modulo caricato"`
Perché il codice è eseguito al momento dell'import.

---

# ✅ Soluzione con `__main__`

```python
def somma(a, b):
    return a + b

if __name__ == "__main__":
    print("Esecuzione diretta del file")
    print(somma(2, 3))
```

### Caso 1 – Esecuzione diretta

```bash
python calcoli.py
```

Output:

```
Esecuzione diretta del file
5
```

### Caso 2 – Import

```python
import calcoli
```

👉 Non stampa nulla
👉 La funzione `somma` è disponibile

---

# 📦 Perché è fondamentale nei corsi?

Permette di:

✔ Scrivere codice riutilizzabile
✔ Separare logica da test manuali
✔ Creare script eseguibili
✔ Costruire progetti modulari

---

# 🧩 Caso reale: test rapido

```python
def main():
    print("Avvio applicazione")

if __name__ == "__main__":
    main()
```

Buona pratica professionale:

* tutta la logica sta in funzioni
* il blocco `__main__` avvia il programma

---

# 🔬 Cosa succede davvero?

Quando esegui:

```bash
python file.py
```

Python:

1. Carica il file
2. Imposta `__name__ = "__main__"`
3. Esegue il codice

Quando importi:

```python
import file
```

Python:

1. Carica il file
2. Imposta `__name__ = "file"`
3. Esegue il codice (una sola volta)
4. Espone funzioni e classi

---

# 🎓 Esempio didattico completo

```python
def quadrato(x):
    return x * x

def main():
    numero = int(input("Inserisci un numero: "))
    print("Risultato:", quadrato(numero))

if __name__ == "__main__":
    main()
```

👉 Può essere:

* usato come script
* importato in un altro programma
* testato automaticamente

---

# 🚀 In una frase

`if __name__ == "__main__":`
serve a dire:

> "Esegui questo codice solo se il file è avviato direttamente, non se viene importato."

