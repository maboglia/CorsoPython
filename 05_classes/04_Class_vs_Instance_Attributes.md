## 4) Class vs Instance Attributes

(**Attributi di classe vs attributi di istanza**)

### 📌 Attributi di istanza (Instance Attributes)

Sono attributi **specifici di ogni oggetto**.
Ogni istanza ha i propri valori.

Esempio:

```python
class Studente:
    def __init__(self, nome):
        self.nome = nome   # attributo di istanza
```

Uso:

```python
s1 = Studente("Marco")
s2 = Studente("Anna")

print(s1.nome)  # Marco
print(s2.nome)  # Anna
```

➡️ `nome` cambia da oggetto a oggetto.

---

### 📌 Attributi di classe (Class Attributes)

Sono attributi **condivisi da tutte le istanze** della classe.

Esempio:

```python
class Studente:
    scuola = "ITIS"   # attributo di classe

    def __init__(self, nome):
        self.nome = nome
```

Uso:

```python
s1 = Studente("Marco")
s2 = Studente("Anna")

print(s1.scuola)  # ITIS
print(s2.scuola)  # ITIS
```

➡️ `scuola` è uguale per tutti.

---

### 📌 Differenza pratica

* **instance attribute** → `self.nome` (appartiene al singolo oggetto)
* **class attribute** → `Studente.scuola` (appartiene alla classe)

---

### 📌 Attenzione: modifiche

Se cambi l’attributo di classe dalla classe:

```python
Studente.scuola = "Liceo"
```

tutte le istanze vedranno il cambiamento.

---

### 📌 Caso delicato: override sull’istanza

Se fai:

```python
s1.scuola = "IPSIA"
```

stai creando un attributo **di istanza** chiamato `scuola`, che **nasconde** quello di classe.

Quindi:

```python
print(s1.scuola)  # IPSIA
print(s2.scuola)  # Liceo
```

---

### 📌 Concetti chiave

* attributi di classe = condivisi
* attributi di istanza = individuali
* assegnare su `self` crea/modifica attributi dell’oggetto


