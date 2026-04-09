## 15) Multi-level Inheritance (Ereditarietà Multilivello)

### 📌 Cos’è

La **multi-level inheritance** si verifica quando una classe eredita da un’altra classe che a sua volta eredita da un’altra.

Quindi hai una catena del tipo:

`A → B → C`

dove:

* `B` eredita da `A`
* `C` eredita da `B`

---

## 🔹 Esempio pratico

```python
class Persona:
    def saluta(self):
        print("Ciao, sono una persona")

class Studente(Persona):
    def studia(self):
        print("Sto studiando")

class StudenteUniversitario(Studente):
    def esami(self):
        print("Sto preparando un esame")
```

Uso:

```python
u = StudenteUniversitario()

u.saluta()   # ereditato da Persona
u.studia()   # ereditato da Studente
u.esami()    # definito in StudenteUniversitario
```

---

## 🔹 Come funziona la ricerca dei metodi (Method Resolution)

Quando chiami un metodo su un oggetto, Python cerca:

1. nella classe dell’oggetto
2. nella classe padre
3. nella classe “nonna”
4. fino ad arrivare a `object`

Questa ricerca si chiama **MRO (Method Resolution Order)**.

---

## 🔹 Esempio con override multilivello

```python
class Persona:
    def ruolo(self):
        print("Persona")

class Studente(Persona):
    def ruolo(self):
        print("Studente")

class StudenteUniversitario(Studente):
    def ruolo(self):
        print("Studente universitario")
```

Uso:

```python
u = StudenteUniversitario()
u.ruolo()
```

Output:

```
Studente universitario
```

➡️ viene usata la versione più specifica.

---

### 📌 Quando è utile

È utile quando vuoi modellare livelli di specializzazione:

* Veicolo → Auto → AutoElettrica
* Utente → Dipendente → Manager
* Animale → Mammifero → Cane

---

### ⚠️ Attenzione

Se la catena diventa troppo lunga:

* aumenta la complessità
* rende difficile capire da dove arriva un metodo

Quindi va usata con moderazione.

---

### 📌 Concetti chiave

* ereditarietà a catena: classe figlia di una classe figlia
* la sottoclasse eredita tutto dai livelli superiori
* Python cerca metodi seguendo l’ordine MRO
