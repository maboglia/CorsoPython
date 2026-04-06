# Modulo `datetime`: Gestire il Tempo

Il tempo in programmazione è complesso (fusi orari, anni bisestili). `datetime` semplifica tutto.

* **La sfida dei formati:** Da non confondere `strftime` e `strptime`.
* **`strftime` (f = format):** Da oggetto a stringa (per stampare la data).
* **`strptime` (p = parse):** Da stringa a oggetto (per elaborare una data scritta dall'utente).

* **Operazioni matematiche:** Si possono sottrarre due date per ottenere un oggetto `timedelta` (la differenza di tempo).

---

```python
from datetime import datetime, timedelta, date

# Data e ora corrente
ora_corrente = datetime.now()
print(f"Ora corrente: {ora_corrente}")
print(f"Formato personalizzato: {ora_corrente.strftime('%d/%m/%Y %H:%M')}")

# Operazioni con le date
domani = date.today() + timedelta(days=1)
una_settimana_fa = datetime.now() - timedelta(weeks=1)

# Parsing da stringa
data_string = "2024-12-25"
natale = datetime.strptime(data_string, "%Y-%m-%d")
```
