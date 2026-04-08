## 2) Creating Classes (Creare Classi)

### 📌 Sintassi base

In Python una classe si definisce con la parola chiave `class`:

```python
class NomeClasse:
    corpo_classe
```

Per convenzione il nome della classe usa il **PascalCase** (iniziale maiuscola).

---

### 📌 Struttura tipica di una classe

Una classe contiene:

* **attributi** (dati)
* **metodi** (funzioni interne alla classe)

Esempio:

```python
class Studente:
    
    def saluta(self):
        print("Ciao, sono uno studente!")
```

---

### 📌 Il parametro `self`

Nei metodi compare sempre `self` come primo parametro:

* `self` rappresenta **l’oggetto corrente**
* serve per accedere ai suoi dati e metodi

Uso:

```python
s1 = Studente()
s1.saluta()
```

Output:

```
Ciao, sono uno studente!
```

---

### 📌 Attributi aggiunti dinamicamente (possibile ma sconsigliato)

In Python puoi aggiungere attributi anche dopo la creazione:

```python
s1.nome = "Marco"
print(s1.nome)
```

Questo funziona, ma è meglio definire gli attributi nel costruttore (`__init__`), per chiarezza.

---

### 📌 Concetti chiave

* `class` definisce un nuovo tipo
* i metodi sono funzioni dentro la classe
* `self` collega il metodo all’istanza

---

**3) Constructors**?
