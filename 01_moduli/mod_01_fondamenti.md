# Modulo 1 – Fondamenti e Ambiente di Sviluppo (8 ore)

## 1.1 Introduzione (2 ore)

### Cos’è Python e perché è importante

**Python** è un linguaggio di programmazione:

* **ad alto livello** → più vicino al linguaggio umano che alla macchina
* **interpretato** → non si compila, si esegue direttamente
* **multipiattaforma** → Windows, Linux, macOS
* **general purpose** → web, automazione, AI, data science, scripting, IoT

👉 È molto usato perché:

* ha una **sintassi semplice e leggibile**
* permette di essere produttivi velocemente
* è uno standard di fatto in molti ambiti (AI, data analysis, scripting)

> Motto tipico: *“Less code, more readability”*

---

### Installazione di Python e setup dell’ambiente

**Python**

* si scarica da: python.org
* verificare l’installazione:

```bash
python --version
```

oppure:

```bash
python3 --version
```

**Editor / IDE**

* **VS Code** → leggero, estendibile, ottimo per didattica
* **PyCharm** → IDE completo, più “guidato”

Concetti importanti da chiarire agli studenti:

* file `.py`
* interprete Python
* cartella di lavoro (workspace / project)

---

### REPL interattiva e primi comandi

Il **REPL** (Read–Eval–Print–Loop) è la console interattiva di Python.

Avvio:

```bash
python
```

Esempi:

```python
>>> 2 + 3
5
>>> print("Ciao Python")
Ciao Python
>>> 10 * 5
50
```

💡 Utile per:

* fare test veloci
* capire subito come funziona un’istruzione

---

### Il concetto di “pythonico”

Scrivere codice **pythonico** significa:

* semplice
* leggibile
* elegante
* esplicito

Lo **Zen di Python**:

```python
import this
```

Frasi chiave da commentare:

* *“Simple is better than complex”*
* *“Readability counts”*
* *“There should be one — and preferably only one — obvious way to do it”*

👉 Python privilegia **chiarezza** rispetto a furbizie sintattiche.

---

## 1.2 Variabili e tipi di dato (3 ore)

### Tipizzazione dinamica

In Python:

* **non si dichiara il tipo**
* il tipo viene assegnato automaticamente

```python
x = 10        # int
x = "ciao"    # ora è una stringa
```

Confronto didattico:

> In Java/PHP il tipo è più esplicito
> In Python è il valore che “porta” il tipo

---

### Tipi base

#### int

```python
eta = 18
```

#### float

```python
prezzo = 9.99
```

#### str

```python
nome = "Mario"
```

#### bool

```python
is_attivo = True
```

Verifica del tipo:

```python
type(eta)
```

---

### Type hints (introduzione)

Servono per:

* **documentare il codice**
* aiutare editor e strumenti di analisi

```python
eta: int = 18
prezzo: float = 9.99
nome: str = "Mario"
```

⚠️ Non sono obbligatori e **non bloccano l’esecuzione**.

---

### Operatori ed espressioni

**Aritmetici**

```python
a + b
a - b
a * b
a / b
a // b   # divisione intera
a % b    # resto
```

**Confronto**

```python
a == b
a != b
a > b
a <= b
```

**Logici**

```python
and
or
not
```

Esempio:

```python
eta = 20
print(eta >= 18 and eta <= 65)
```

---

### Input / Output base

```python
nome = input("Inserisci il nome: ")
print("Ciao", nome)
```

⚠️ `input()` restituisce **sempre una stringa**

Conversione:

```python
eta = int(input("Inserisci l'età: "))
print(eta + 1)
```

---

## 1.3 Strings e formattazione (3 ore)

### Metodi delle stringhe

```python
testo = "  Python è Fantastico  "

testo.upper()
testo.lower()
testo.strip()
testo.replace("Fantastico", "potente")
```

Le stringhe sono **immutabili**:

```python
testo = testo.strip()
```

---

### Indicizzazione e slicing

```python
parola = "Python"

parola[0]     # 'P'
parola[-1]    # 'n'
```

Slicing:

```python
parola[0:3]   # 'Pyt'
parola[2:]    # 'thon'
parola[:4]    # 'Pyth'
```

Ottimo per spiegare:

* indici
* intervalli
* concetto di sequenza

---

### F-strings (formattazione moderna)

Metodo consigliato 🔥

```python
nome = "Anna"
eta = 25

print(f"Ciao {nome}, hai {eta} anni")
```

Con espressioni:

```python
print(f"Tra 5 anni avrai {eta + 5} anni")
```

Con formattazione numerica:

```python
prezzo = 9.5
print(f"Prezzo: {prezzo:.2f} €")
```

---

### Raw strings e caratteri speciali

Caratteri speciali:

```python
print("Ciao\nMondo")
print("Percorso: C:\\Users\\Mario")
```

**Raw string**:

```python
path = r"C:\Users\Mario\Documenti"
print(path)
```

👉 Fondamentale per:

* percorsi Windows
* regex (in moduli successivi)

---

## Suggerimento didattico finale

Per chiudere il modulo 1:

* mini esercizi su REPL
* programma “Anagrafica semplice”

```python
nome = input("Nome: ")
eta = int(input("Età: "))
print(f"{nome} avrà {eta + 1} anni l'anno prossimo")
```

