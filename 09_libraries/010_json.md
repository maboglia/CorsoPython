# 📌 Libreria `json` in Python – Scheda Completa

La libreria standard **`json`** serve per:

* convertire oggetti Python ↔ JSON
* leggere/scrivere file `.json`
* gestire API REST e configurazioni

📌 Modulo incluso in Python → **non serve installare nulla**.

```python
import json
```

---

# 1) JSON: concetti base

### JSON supporta:

* oggetti → `{ }` (dizionari)
* array → `[ ]` (liste)
* stringhe `"testo"`
* numeri `10`, `3.14`
* boolean `true / false`
* null `null`

📌 In Python corrispondono a:

| JSON       | Python     |
| ---------- | ---------- |
| object     | dict       |
| array      | list       |
| string     | str        |
| number     | int/float  |
| true/false | True/False |
| null       | None       |

---

# 2) ✅ Convertire Python → JSON string (`json.dumps`)

```python
import json

studente = {
    "nome": "Mario",
    "cognome": "Rossi",
    "eta": 20
}

json_str = json.dumps(studente)
print(json_str)
```

📌 Output:

```json
{"nome": "Mario", "cognome": "Rossi", "eta": 20}
```

---

# 3) Convertire JSON string → Python (`json.loads`)

```python
import json

json_str = '{"nome": "Mario", "eta": 20}'

obj = json.loads(json_str)
print(obj)
print(obj["nome"])
```

📌 Output:

```python
{'nome': 'Mario', 'eta': 20}
Mario
```

---

# 4) Scrittura su file JSON (`json.dump`)

```python
import json

dati = {
    "classe": "5A",
    "studenti": ["Mario", "Anna", "Luca"]
}

with open("classe.json", "w", encoding="utf-8") as f:
    json.dump(dati, f)
```

📌 crea file `classe.json`.

---

# 5) Lettura da file JSON (`json.load`)

```python
import json

with open("classe.json", "r", encoding="utf-8") as f:
    dati = json.load(f)

print(dati)
```

---

# 6) JSON formattato (pretty print)

Per scrivere JSON leggibile:

```python
json_str = json.dumps(dati, indent=4)
print(json_str)
```

Oppure su file:

```python
with open("classe.json", "w", encoding="utf-8") as f:
    json.dump(dati, f, indent=4)
```

---

# 7) Ordinare le chiavi (`sort_keys`)

```python
json_str = json.dumps(dati, indent=4, sort_keys=True)
print(json_str)
```

---

# 8) Gestire caratteri accentati (`ensure_ascii`)

Default: i caratteri speciali vengono codificati in Unicode.

Per mantenere lettere accentate normali:

```python
json_str = json.dumps(dati, ensure_ascii=False, indent=4)
print(json_str)
```

📌 Consigliato con UTF-8.

---

# 9) Scrivere JSON compatto

```python
json_str = json.dumps(dati, separators=(",", ":"))
print(json_str)
```

📌 Nessuno spazio → utile per API o compressione.

---

# 10) Tipi non serializzabili (problema comune)

Alcuni oggetti Python NON sono JSON serializzabili, es:

* datetime
* set
* oggetti custom

Esempio errore:

```python
import json
import datetime

obj = {"oggi": datetime.datetime.now()}
json.dumps(obj)   # TypeError
```

---

# 11) Risolvere: conversione manuale

```python
import json
import datetime

obj = {"oggi": str(datetime.datetime.now())}

print(json.dumps(obj))
```

---

# 12) Risolvere: parametro `default`

```python
import json
import datetime

def convertitore(o):
    if isinstance(o, datetime.datetime):
        return o.isoformat()
    raise TypeError("Tipo non supportato")

obj = {"oggi": datetime.datetime.now()}

print(json.dumps(obj, default=convertitore, indent=4))
```

---

# 13) Lettura sicura: gestione errori JSON

Se il JSON è malformato:

```python
import json

try:
    dati = json.loads("{nome:Mario}")  # errato
except json.JSONDecodeError as e:
    print("Errore JSON:", e)
```

---

# 14) Lettura di file JSON con gestione errori

```python
import json

try:
    with open("classe.json", "r", encoding="utf-8") as f:
        dati = json.load(f)
except FileNotFoundError:
    print("File non trovato")
except json.JSONDecodeError:
    print("JSON non valido")
```

---

# 15) Aggiornare un file JSON (lettura + modifica + riscrittura)

```python
import json

with open("classe.json", "r", encoding="utf-8") as f:
    dati = json.load(f)

dati["anno"] = 2026

with open("classe.json", "w", encoding="utf-8") as f:
    json.dump(dati, f, indent=4, ensure_ascii=False)
```

---

# 16) Esempio: lista di oggetti JSON

```python
import json

studenti = [
    {"nome": "Mario", "eta": 20},
    {"nome": "Anna", "eta": 22}
]

print(json.dumps(studenti, indent=4))
```

📌 Output:

```json
[
    {
        "nome": "Mario",
        "eta": 20
    },
    {
        "nome": "Anna",
        "eta": 22
    }
]
```

---

# 17) Accesso ai dati JSON dopo parsing

```python
with open("classe.json", "r", encoding="utf-8") as f:
    dati = json.load(f)

print(dati["classe"])
print(dati["studenti"][0])
```

---

# 18) Convertire JSON in modo robusto (chiavi mancanti)

```python
nome = dati.get("nome", "Sconosciuto")
```

📌 `get()` evita errori se la chiave manca.

---

# 19) Validazione base dei dati

JSON è sintatticamente corretto, ma i dati potrebbero essere sbagliati.

Esempio controllo:

```python
if "studenti" not in dati or not isinstance(dati["studenti"], list):
    raise ValueError("Formato JSON non valido")
```

---

# 20) Differenza tra dump/dumps e load/loads

| Funzione               | Input                 | Output         |
| ---------------------- | --------------------- | -------------- |
| `json.dump(obj, file)` | oggetto Python + file | scrive su file |
| `json.dumps(obj)`      | oggetto Python        | string JSON    |
| `json.load(file)`      | file                  | oggetto Python |
| `json.loads(stringa)`  | string JSON           | oggetto Python |

---

# 21) Parametri principali di `json.dumps()`

```python
json.dumps(obj,
    indent=4,
    sort_keys=True,
    ensure_ascii=False,
    separators=(",", ":"),
    default=str
)
```

---

# 22) Esempio completo: file configurazione JSON

### config.json

```json
{
  "db_host": "localhost",
  "db_user": "root",
  "db_pass": "1234",
  "db_name": "scuola"
}
```

### lettura config:

```python
import json

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

print(config["db_host"])
```

---

# 23) JSON e API REST (concetto tipico)

Un server REST spesso restituisce JSON.

Esempio risposta:

```json
{
  "id": 10,
  "nome": "Mario"
}
```

In Python, dopo parsing, diventa un dict:

```python
dati = json.loads(risposta_testo)
print(dati["nome"])
```

---

# 24) Salvare dati strutturati complessi

```python
registro = {
    "classe": "5A",
    "materie": [
        {"nome": "Informatica", "ore": 4},
        {"nome": "Matematica", "ore": 3}
    ],
    "studenti": [
        {"nome": "Mario", "voti": [7, 8, 6]},
        {"nome": "Anna", "voti": [9, 8, 9]}
    ]
}

with open("registro.json", "w", encoding="utf-8") as f:
    json.dump(registro, f, indent=4, ensure_ascii=False)
```

---

# 25) Best Practice consigliate

✅ usare `encoding="utf-8"`
✅ usare `ensure_ascii=False` per testi italiani
✅ usare `indent=4` per configurazioni e debug
✅ gestire `JSONDecodeError`
✅ usare `.get()` per chiavi facoltative
✅ convertire manualmente tipi complessi (`datetime`, `set`, ecc.)

---

# 26) Errori tipici

### ❌ JSONDecodeError

👉 JSON malformato (virgolette sbagliate, virgole mancanti)

### ❌ TypeError: not JSON serializable

👉 stai tentando di convertire datetime, set o oggetti custom

### ❌ Confondere load/dump e loads/dumps

👉 `load/dump` = file
👉 `loads/dumps` = stringhe

---

# 27) Mini-riepilogo operativo

📌 Leggere JSON da file:

```python
with open("file.json", "r", encoding="utf-8") as f:
    dati = json.load(f)
```

📌 Scrivere JSON su file:

```python
with open("file.json", "w", encoding="utf-8") as f:
    json.dump(dati, f, indent=4, ensure_ascii=False)
```

📌 Convertire oggetto Python → stringa JSON:

```python
json_str = json.dumps(dati)
```

📌 Convertire stringa JSON → oggetto Python:

```python
dati = json.loads(json_str)
```

