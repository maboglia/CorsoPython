## 7) Comparing Objects (Confrontare Oggetti)

### 📌 Problema

In Python, se confronti due oggetti con `==`, di default Python confronta **l’identità** (cioè se sono lo stesso oggetto in memoria), non i valori interni.

Esempio:

```python
class Studente:
    def __init__(self, nome):
        self.nome = nome

s1 = Studente("Marco")
s2 = Studente("Marco")

print(s1 == s2)   # False (default)
```

➡️ Anche se hanno lo stesso nome, sono oggetti diversi.

---

### 📌 `is` vs `==`

* `is` → verifica se è **lo stesso oggetto**
* `==` → verifica se sono **uguali** (dipende da `__eq__`)

Esempio:

```python
print(s1 is s2)   # False
```

---

### 📌 Definire l’uguaglianza con `__eq__`

Per confrontare i contenuti si implementa:

```python id="dyp7wx"
class Studente:
    def __init__(self, nome):
        self.nome = nome

    def __eq__(self, other):
        return self.nome == other.nome


s1 = Studente("Marco")
s2 = Studente("Marco")

print(s1 == s2)   # True
```

Ora il confronto funziona come ci aspettiamo.

---

### 📌 Attenzione: controllo del tipo

È buona pratica verificare che `other` sia del tipo corretto:

```python id="xfl8ir"
def __eq__(self, other):
    if not isinstance(other, Studente):
        return False
    return self.nome == other.nome
```

---

### 📌 Confronti ordinati: `< > <= >=`

Per ordinare oggetti (es. sort) puoi definire:

* `__lt__`  (less than `<`)
* `__le__`  (`<=`)
* `__gt__`  (`>`)
* `__ge__`  (`>=`)

Esempio:

```python id="l1q3mz"
class Studente:
    def __init__(self, nome, voto):
        self.nome = nome
        self.voto = voto

    def __lt__(self, other):
        return self.voto < other.voto
```

Uso:

```python id="hcrf5t"
s1 = Studente("Marco", 7)
s2 = Studente("Anna", 9)

print(s1 < s2)  # True
```

---

### 📌 Concetti chiave

* senza `__eq__`, `==` confronta l’identità
* con `__eq__`, `==` confronta i contenuti
* con `__lt__` e simili puoi ordinare oggetti

