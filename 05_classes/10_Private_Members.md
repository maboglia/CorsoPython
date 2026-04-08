## 10) Private Members (Membri Privati)

### 📌 Premessa importante

In Python **non esiste un vero "private"** come in Java o C++.

Python usa una convenzione:
👉 *“siamo tutti adulti”* (consenting adults).

---

## 🔹 1) Membri "protetti" con `_`

Se un attributo/metodo inizia con `_`, significa:

➡️ “non usarlo direttamente dall’esterno”

```python
class Studente:
    def __init__(self, nome):
        self._nome = nome   # convenzione: protected
```

È solo una convenzione, ma funziona bene in team.

---

## 🔹 2) Membri "privati" con `__` (Name Mangling)

Se usi `__nome`, Python applica il **name mangling**:
cambia internamente il nome per renderlo più difficile da accedere.

```python
class Studente:
    def __init__(self, nome):
        self.__nome = nome   # "privato"
```

Se provi ad accedere:

```python
s = Studente("Marco")
print(s.__nome)
```

Errore:

```
AttributeError
```

---

### 📌 Come viene trasformato internamente

Python rinomina `__nome` in:

```
_Studente__nome
```

Quindi tecnicamente puoi ancora accedere:

```python
print(s._Studente__nome)
```

➡️ Questo dimostra che non è vero private, ma un meccanismo di protezione.

---

## 🔹 3) Metodi privati

Vale lo stesso discorso:

```python
class Studente:
    def __metodo_privato(self):
        print("Metodo interno")

    def pubblico(self):
        self.__metodo_privato()
```

Uso:

```python
s = Studente()
s.pubblico()
```

---

### 📌 Concetti chiave

* `_x` → convenzione: "non toccare"
* `__x` → name mangling (più protetto)
* Python non blocca davvero l’accesso, ma scoraggia l’uso esterno

