# Risposte http

Per **rispondere a richieste HTTP (cioè creare un server web o API)** in Python esistono diverse librerie e framework, da **molto semplici** a **professionali**.

Le principali sono:

* server HTTP base (standard library)
* micro-framework web
* framework completi
* server asincroni per API

---

# 1️⃣ `http.server` (libreria standard)

http.server

È il **server HTTP base incluso in Python**.
Serve per:

* test
* piccoli prototipi
* file server

---

## Server minimo

```python
from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        self.wfile.write(b"Ciao dal server Python")

server = HTTPServer(("localhost", 8000), MyHandler)
server.serve_forever()
```

Aprendo:

```
http://localhost:8000
```

il server risponde.

---

## Server statico rapido

Python include anche un comando velocissimo:

```bash
python -m http.server 8000
```

Serve una directory via HTTP.

---

# 2️⃣ `Flask` (micro-framework)

Flask

È uno dei framework web **più semplici e diffusi**.

Installazione:

```bash
pip install flask
```

---

## Server minimo

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Ciao dal server Flask"

app.run(port=5000)
```

URL:

```
http://localhost:5000
```

---

## Endpoint API

```python
from flask import jsonify

@app.route("/api/user")
def user():
    return jsonify({
        "name": "Mario",
        "age": 30
    })
```

Risposta JSON.

---

# 3️⃣ `FastAPI` (API moderne)

FastAPI

Framework moderno per:

* **REST API**
* alte prestazioni
* validazione automatica
* documentazione automatica

Installazione:

```bash
pip install fastapi uvicorn
```

---

## API minima

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "Hello"}
```

Avvio server:

```bash
uvicorn main:app --reload
```

---

## Documentazione automatica

FastAPI genera automaticamente:

```
http://localhost:8000/docs
```

Swagger UI.

---

# 4️⃣ `Django` (framework completo)

Django

È un framework **molto completo** che include:

* ORM
* autenticazione
* template
* routing
* admin panel

Installazione:

```bash
pip install django
```

Creazione progetto:

```bash
django-admin startproject mysite
```

---

# 5️⃣ Server asincroni

Per alte prestazioni.

---

## `uvicorn`

Uvicorn

Server ASGI molto veloce usato con:

* FastAPI
* Starlette

---

## `gunicorn`

Gunicorn

Server WSGI usato in produzione con:

* Flask
* Django

---

# 📊 Confronto rapido

| strumento     | tipo               | uso             |
| ------------- | ------------------ | --------------- |
| `http.server` | standard           | test            |
| `Flask`       | micro-framework    | piccoli servizi |
| `FastAPI`     | API moderne        | REST veloci     |
| `Django`      | framework completo | web app grandi  |
| `uvicorn`     | server ASGI        | produzione      |

---

💡 **Architettura tipica moderna Python**

```
FastAPI
   ↓
Uvicorn
   ↓
Reverse proxy (nginx)
```

---

Un aspetto molto interessante è che **in Python esistono due standard diversi per i server web**:

* **WSGI**
* **ASGI**

Capire la differenza tra questi due spiega **perché framework come Flask e FastAPI funzionano in modo diverso**.
