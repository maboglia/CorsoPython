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

---

# 📌 Libreria `datetime` – Scheda Completa

Serve per gestire **date, orari, timestamp, differenze temporali**.

```python
import datetime
```

---

## 1) Oggetti principali

| Classe      | Significato             |
| ----------- | ----------------------- |
| `date`      | solo data (AAAA-MM-GG)  |
| `time`      | solo ora (HH:MM:SS)     |
| `datetime`  | data + ora              |
| `timedelta` | differenza tra date/ore |

---

## 2) Data corrente

```python
from datetime import date

oggi = date.today()
print(oggi)          # 2026-04-11
print(oggi.year)
print(oggi.month)
print(oggi.day)
```

---

## 3) Ora corrente (datetime)

```python
from datetime import datetime

adesso = datetime.now()
print(adesso)
print(adesso.year, adesso.month, adesso.day)
print(adesso.hour, adesso.minute, adesso.second)
```

---

## 4) Creare date e datetime manualmente

```python
from datetime import date, datetime

d = date(2026, 4, 11)
dt = datetime(2026, 4, 11, 15, 30, 0)

print(d)
print(dt)
```

---

## 5) Formattazione (strftime)

```python
from datetime import datetime

adesso = datetime.now()
print(adesso.strftime("%d/%m/%Y"))      # 11/04/2026
print(adesso.strftime("%H:%M:%S"))      # 15:30:10
print(adesso.strftime("%d/%m/%Y %H:%M"))
```

### Codici più usati

| Codice | Significato    |
| ------ | -------------- |
| `%d`   | giorno (01-31) |
| `%m`   | mese (01-12)   |
| `%Y`   | anno 4 cifre   |
| `%H`   | ora (00-23)    |
| `%M`   | minuti         |
| `%S`   | secondi        |
| `%A`   | nome giorno    |
| `%B`   | nome mese      |

---

## 6) Parsing stringa → datetime (strptime)

```python
from datetime import datetime

s = "11/04/2026 15:30"
dt = datetime.strptime(s, "%d/%m/%Y %H:%M")

print(dt)
```

---

## 7) Differenza tra date (timedelta)

```python
from datetime import date

d1 = date(2026, 4, 11)
d2 = date(2026, 4, 20)

diff = d2 - d1
print(diff.days)   # 9
```

---

## 8) Sommare o sottrarre giorni

```python
from datetime import datetime, timedelta

adesso = datetime.now()

fra_7_giorni = adesso + timedelta(days=7)
ieri = adesso - timedelta(days=1)

print(fra_7_giorni)
print(ieri)
```

---

## 9) Timestamp Unix (secondi dal 1970)

```python
from datetime import datetime

ts = datetime.now().timestamp()
print(ts)
```

Da timestamp a datetime:

```python
from datetime import datetime

dt = datetime.fromtimestamp(1700000000)
print(dt)
```

---

## 10) Confronto tra date/datetime

```python
from datetime import date

d1 = date(2026, 4, 11)
d2 = date(2026, 4, 20)

print(d1 < d2)   # True
```

---

## 11) Best practice

✅ usare `datetime.now()` per data+ora
✅ usare `strftime` per stampare in formato leggibile
✅ usare `strptime` per leggere input utente
✅ usare `timedelta` per calcoli

