# Librerie per le richieste http

In Python esistono diverse **librerie per lavorare con URL e richieste HTTP**. Alcune sono **incluse nella libreria standard**, altre sono **esterne ma molto usate**. Le principali categorie sono:

* gestione **URL**
* **richieste HTTP**
* **API REST**
* **client HTTP asincroni**

---

# 1️⃣ `urllib` (libreria standard)

urllib

È la libreria **standard di Python** per gestire:

* URL
* richieste HTTP
* encoding di query string

Moduli principali:

| modulo               | funzione            |
| -------------------- | ------------------- |
| `urllib.request`     | fare richieste HTTP |
| `urllib.parse`       | manipolare URL      |
| `urllib.error`       | gestione errori     |
| `urllib.robotparser` | parser robots.txt   |

---

## Esempio richiesta HTTP

```python
import urllib.request

response = urllib.request.urlopen("https://api.github.com")

data = response.read()
print(data)
```

---

## Parsing di URL

```python
from urllib.parse import urlparse

url = "https://example.com:8080/path?id=5"

parsed = urlparse(url)

print(parsed.scheme)
print(parsed.netloc)
print(parsed.path)
```

Output:

```
https
example.com:8080
/path
```

---

## Query string

```python
from urllib.parse import urlencode

params = {
    "q": "python",
    "page": 2
}

query = urlencode(params)

print(query)
```

Output:

```
q=python&page=2
```

---

# 2️⃣ `requests` (la libreria più usata)

Requests

È **la libreria HTTP più popolare in Python** perché è molto più semplice di `urllib`.

Installazione:

```bash
pip install requests
```

---

## Richiesta GET

```python
import requests

r = requests.get("https://api.github.com")

print(r.status_code)
print(r.text)
```

---

## GET con parametri

```python
params = {
    "q": "python"
}

r = requests.get("https://httpbin.org/get", params=params)

print(r.json())
```

---

## POST

```python
data = {
    "username": "mario",
    "password": "1234"
}

r = requests.post("https://httpbin.org/post", data=data)

print(r.json())
```

---

## Header

```python
headers = {
    "User-Agent": "PythonClient"
}

requests.get("https://httpbin.org/get", headers=headers)
```

---

# 3️⃣ `http.client` (basso livello)

http.client

È un **client HTTP molto basso livello** nella libreria standard.

Esempio:

```python
import http.client

conn = http.client.HTTPSConnection("api.github.com")

conn.request("GET", "/")

response = conn.getresponse()

print(response.status)
print(response.read())
```

Viene usato raramente perché `requests` è molto più semplice.

---

# 4️⃣ Client HTTP asincroni

Per programmi **async** (ad esempio con `asyncio`).

---

## `aiohttp`

aiohttp

Molto usato per:

* client HTTP asincroni
* server web async

Installazione:

```bash
pip install aiohttp
```

---

### Esempio

```python
import aiohttp
import asyncio

async def main():

    async with aiohttp.ClientSession() as session:

        async with session.get("https://api.github.com") as resp:

            print(resp.status)
            print(await resp.text())

asyncio.run(main())
```

---

# 5️⃣ Librerie per manipolare URL

---

## `yarl`

yarl

Molto usata insieme ad `aiohttp`.

```python
from yarl import URL

url = URL("https://example.com")

url = url.with_query({"q": "python"})

print(url)
```

---

# 📊 Confronto rapido

| libreria      | tipo     | uso            |
| ------------- | -------- | -------------- |
| `urllib`      | standard | URL + HTTP     |
| `requests`    | esterna  | HTTP semplice  |
| `http.client` | standard | HTTP low level |
| `aiohttp`     | esterna  | HTTP asincrono |
| `yarl`        | esterna  | gestione URL   |

---

💡 **Nella pratica reale:**

* **90% dei programmi Python usa `requests`**
* **`urllib.parse` è usato spesso per manipolare URL**
* **`aiohttp` è usato per applicazioni async e ad alte prestazioni**.
