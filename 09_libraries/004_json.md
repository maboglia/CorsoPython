# 4. Modulo `json`: Lo standard dello scambio dati

JSON è la lingua franca del web. 

* **La distinzione "s":**
* `json.dump()` e `json.load()` lavorano con i **file**.
* `json.dumps()` e `json.loads()` lavorano con le **stringhe** (la "s" sta per string).

* **Esempio pratico:**

```python
import json
dati = {"studente": "Mario", "voti": [28, 30, 27]}
stringa_json = json.dumps(dati) # Serializzazione

```

### 3.4 Modulo `json` - Gestione JSON

```python
import json

# Dati Python -> JSON
dati = {
    "nome": "Mario",
    "età": 30,
    "città": "Roma",
    "hobby": ["calcio", "lettura", "viaggi"]
}

# Conversione in stringa JSON
json_string = json.dumps(dati, indent=2, ensure_ascii=False)
print(json_string)

# Salvataggio su file
with open("dati.json", "w", encoding="utf-8") as file:
    json.dump(dati, file, indent=2, ensure_ascii=False)

# Lettura da file
with open("dati.json", "r", encoding="utf-8") as file:
    dati_caricati = json.load(file)
    print(dati_caricati)
```
