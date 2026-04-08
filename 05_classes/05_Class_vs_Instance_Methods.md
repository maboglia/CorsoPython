## 5) Class vs Instance Methods

(**Metodi di istanza vs metodi di classe**)

### 📌 Metodi di istanza (Instance Methods)

Sono i metodi più comuni.
Lavorano sui dati dell’oggetto e ricevono `self`.

Esempio:

```python
class Studente:
    def __init__(self, nome):
        self.nome = nome

    def saluta(self):          # metodo di istanza
        print("Ciao, sono", self.nome)
```

Uso:

```python
s1 = Studente("Marco")
s1.saluta()
```

➡️ Il metodo usa `self.nome`, cioè dati dell’istanza.

---

### 📌 Metodi di classe (Class Methods)

Sono metodi che lavorano sulla **classe**, non sulla singola istanza.
Usano il decoratore `@classmethod` e ricevono `cls`.

Esempio:

```python
class Studente:
    scuola = "ITIS"

    @classmethod
    def cambia_scuola(cls, nuova_scuola):
        cls.scuola = nuova_scuola
```

Uso:

```python
Studente.cambia_scuola("Liceo")
print(Studente.scuola)  # Liceo
```

➡️ Qui non serve creare un oggetto.

---

### 📌 Quando usare i class methods

Utili per:

* modificare attributi di classe
* creare metodi "factory" (costruttori alternativi)

Esempio factory:

```python
class Studente:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    @classmethod
    def da_stringa(cls, testo):
        nome, eta = testo.split("-")
        return cls(nome, int(eta))
```

Uso:

```python
s1 = Studente.da_stringa("Marco-18")
print(s1.nome, s1.eta)
```

---

### 📌 Static Methods (nota importante)

Esiste anche `@staticmethod`: non riceve né `self` né `cls`.

```python
class Calcoli:
    @staticmethod
    def somma(a, b):
        return a + b
```

Uso:

```python
print(Calcoli.somma(3, 5))
```

➡️ È una funzione "inserita" nella classe per organizzazione.

---

### 📌 Differenza riassunta

* **instance method** → lavora sull’oggetto (`self`)
* **class method** → lavora sulla classe (`cls`)
* **static method** → funzione indipendente, ma dentro la classe

