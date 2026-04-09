## 17) A Good Example of Inheritance (Un buon esempio di ereditarietà)

### 📌 Scenario realistico

Un buon uso dell’ereditarietà è quando esiste una relazione chiara **IS-A**.

Esempio classico:

* `Dipendente` **è una** `Persona`
* `Docente` **è un** `Dipendente`
* `Tecnico` **è un** `Dipendente`

Tutti condividono dati comuni (nome, stipendio), ma ognuno ha comportamenti specifici.

---

## ✅ Esempio completo

```python
class Persona:
    def __init__(self, nome):
        self.nome = nome

    def descrizione(self):
        return f"Persona: {self.nome}"


class Dipendente(Persona):
    def __init__(self, nome, stipendio):
        super().__init__(nome)
        self.stipendio = stipendio

    def descrizione(self):
        return f"Dipendente: {self.nome}, stipendio={self.stipendio}"


class Docente(Dipendente):
    def __init__(self, nome, stipendio, materia):
        super().__init__(nome, stipendio)
        self.materia = materia

    def descrizione(self):
        return f"Docente: {self.nome}, materia={self.materia}, stipendio={self.stipendio}"


class Tecnico(Dipendente):
    def __init__(self, nome, stipendio, reparto):
        super().__init__(nome, stipendio)
        self.reparto = reparto

    def descrizione(self):
        return f"Tecnico: {self.nome}, reparto={self.reparto}, stipendio={self.stipendio}"
```

---

## 🔹 Uso pratico (polimorfismo naturale)

```python
persone = [
    Persona("Anna"),
    Docente("Marco", 1800, "Informatica"),
    Tecnico("Luca", 1600, "Laboratorio")
]

for p in persone:
    print(p.descrizione())
```

Output:

```
Persona: Anna
Docente: Marco, materia=Informatica, stipendio=1800
Tecnico: Luca, reparto=Laboratorio, stipendio=1600
```

---

## 📌 Perché è un buon esempio?

Perché:

* c’è una gerarchia logica e naturale (**IS-A**)
* la superclasse contiene dati comuni (`nome`)
* la sottoclasse aggiunge attributi specifici (`materia`, `reparto`)
* ogni classe può ridefinire (`override`) lo stesso metodo (`descrizione`)
* funziona bene con liste di oggetti misti (polimorfismo)

---

### ✅ Concetti chiave

* ereditarietà utile quando c’è relazione **generale → specifico**
* `super()` evita duplicazione di codice
* l’override rende il comportamento adattabile
