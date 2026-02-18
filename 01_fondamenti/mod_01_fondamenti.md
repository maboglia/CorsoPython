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

---

## Esercizi – Modulo 1: Fondamenti Python

## 🟢 Livello Base (riscaldamento / REPL)

### Esercizio 1 – Primo contatto

Apri la REPL Python ed esegui:

1. Una somma
2. Una moltiplicazione
3. Una divisione

👉 Scrivi cosa succede se dividi due interi.

---

### Esercizio 2 – Stampa a video

Scrivi un programma che stampi:

```
Benvenuto nel corso di Python!
```

Poi modificalo per stampare il tuo nome su una nuova riga.

---

### Esercizio 3 – Variabili

1. Crea una variabile `nome`
2. Crea una variabile `eta`
3. Stampale entrambe con `print()`

---

## 🟡 Livello Base–Intermedio

### Esercizio 4 – Input utente

Scrivi un programma che:

1. Chiede il nome all’utente
2. Chiede l’età
3. Stampa una frase del tipo:

```
Ciao Marco, hai 20 anni
```

💡 Attenzione al tipo restituito da `input()`.

---

### Esercizio 5 – Operazioni numeriche

Chiedi all’utente due numeri interi e stampa:

* la somma
* la differenza
* il prodotto
* la divisione

---

### Esercizio 6 – Conversione tipi

Cosa succede se fai:

```python
numero = input("Inserisci un numero: ")
print(numero + 1)
```

👉 Correggi il programma.

---

## 🟡 Stringhe

### Esercizio 7 – Metodi delle stringhe

Dato:

```python
testo = "  Python è Divertente  "
```

1. Rimuovi gli spazi iniziali e finali
2. Trasforma il testo in maiuscolo
3. Sostituisci “Divertente” con “Potente”

---

### Esercizio 8 – Lunghezza stringa

Chiedi una parola all’utente e stampa:

```
La parola contiene X caratteri
```

Suggerimento: `len()`.

---

### Esercizio 9 – Indicizzazione

Data la stringa:

```python
parola = "Programmazione"
```

1. Stampa il primo carattere
2. Stampa l’ultimo carattere
3. Stampa i primi 5 caratteri

---

## 🟠 Formattazione

### Esercizio 10 – F-string

Chiedi:

* nome
* cognome
* età

Stampa:

```
Nome: Mario Rossi – Età: 25
```

Usa **solo f-string**.

---

### Esercizio 11 – Calcolo futuro

Chiedi l’anno di nascita e stampa:

```
Nel 2030 avrai X anni
```

---

### Esercizio 12 – Prezzo formattato

Dato:

```python
prezzo = 7.5
```

Stampa:

```
Prezzo: 7.50 €
```

---

## 🔵 Raw strings e caratteri speciali

### Esercizio 13 – Percorsi

Stampa questo percorso **senza errori**:

```
C:\Users\Studente\Desktop\python
```

1. usando escape
2. usando raw string

---

## 🔴 Mini–verifica finale (riassuntivo)

### Esercizio 14 – Anagrafica

Scrivi un programma che:

1. Chiede nome, cognome ed età
2. Stampa una frase completa e ben formattata
3. Indica quanti caratteri ha il nome completo

Esempio output:

```
Mario Rossi ha 20 anni
Il nome completo contiene 11 caratteri
```

---

## ⭐ Extra (per studenti veloci)

### Esercizio 15 – Gioco semplice

Chiedi un numero all’utente e stampa:

* se è maggiore di 10
* se è uguale a 10
* se è minore di 10

(usa solo operatori di confronto)
