# 🚀 Flask Starter Kit: Guida Completa

Questa scheda riassume come creare una Web App con Flask che gestisce sia pagine HTML che API REST.

## 1️⃣ Setup e Struttura

Per prima cosa, installa il framework:

```bash
pip install flask

```

Organizza i file in questo modo per rispettare le convenzioni di Flask:

```text
flask_app/
│
├── app.py              # Logica del server
├── data/               # Database (JSON)
│   └── users.json
└── templates/          # Pagine HTML (Jinja2)
    └── home.html

```

---

## 2️⃣ Logica Applicativa (`app.py`)

Ho integrato la creazione automatica delle cartelle e una gestione degli errori più robusta.

```python
from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)

DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "users.json")

# Assicura che la cartella data esista all'avvio
os.makedirs(DATA_DIR, exist_ok=True)

def load_users():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_users(users):
    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=2)

# --- ROTTE HTML ---

@app.route("/")
def home():
    users = load_users()
    return render_template("home.html", users=users)

# --- API REST ---

@app.route("/api/users", methods=["GET"])
def get_users():
    return jsonify(load_users())

@app.route("/api/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    users = load_users()
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json()
    
    # Validazione minima
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Missing name or email"}), 400

    users = load_users()
    new_user = {
        "id": max([u["id"] for u in users], default=0) + 1,
        "name": data["name"],
        "email": data["email"]
    }
    
    users.append(new_user)
    save_users(users)
    return jsonify(new_user), 201

@app.route("/api/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    users = load_users()
    new_users = [u for u in users if u["id"] != user_id]
    
    if len(users) == len(new_users):
        return jsonify({"error": "User not found"}), 404
        
    save_users(new_users)
    return jsonify({"message": f"User {user_id} deleted"}), 200

# Gestione errore 404 globale (JSON)
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found"}), 404

if __name__ == "__main__":
    app.run(debug=True, port=5000)

```

---

## 3️⃣ Il Template (`templates/home.html`)

Flask usa **Jinja2** per inserire dati Python nel codice HTML.

```html
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>Gestione Utenti</title>
    <style>
        body { font-family: sans-serif; margin: 40px; line-height: 1.6; }
        .user-card { border: 1px solid #ddd; padding: 10px; margin-bottom: 5px; border-radius: 5px; }
    </style>
</head>
<body>
    <h1>Elenco Utenti Registrati</h1>
    <div id="user-list">
        {% for user in users %}
        <div class="user-card">
            <strong>{{ user.name }}</strong> — <code>{{ user.email }}</code> (ID: {{ user.id }})
        </div>
        {% else %}
        <p>Nessun utente trovato.</p>
        {% endfor %}
    </div>
</body>
</html>

```

---

## 4️⃣ Riepilogo Concetti Chiave

| Funzione             | Scopo                                                               |
| -------------------- | ------------------------------------------------------------------- |
| `@app.route('/')`    | Collega un URL a una funzione Python.                               |
| `request.get_json()` | Estrae i dati inviati in formato JSON (per le POST).                |
| `jsonify()`          | Converte dizionari Python in stringhe JSON per il client.           |
| `render_template()`  | Cerca file nella cartella `/templates` e inietta le variabili.      |
| `<int:user_id>`      | Cattura una parte dell'URL e la passa come argomento (tipo intero). |

---

### 💡 Suggerimento per il test

Per testare la creazione dell'utente senza browser, usa il terminale:

```bash
curl -X POST http://127.0.0.1:5000/api/users \
     -H "Content-Type: application/json" \
     -d '{"name": "Giulia", "email": "giulia@example.com"}'

```

---

## Con database sqlite

Passare da un file JSON a un database **SQLite** è il salto di qualità necessario per gestire dati in modo professionale. SQLite è perfetto perché è "zero-config": il database è un semplice file `.db` nel tuo progetto, ma lo interroghiamo con SQL (o tramite un ORM).

Per rendere tutto più semplice e "Pythonico", useremo **Flask-SQLAlchemy**, l'estensione standard che trasforma le tabelle del database in classi Python.

---

### 1️⃣ Installazione

Ti serve l'estensione per gestire il database:

```bash
pip install flask-sqlalchemy

```

---

### 2️⃣ Il concetto di ORM (Object-Relational Mapping)

Invece di scrivere query SQL manuali, useremo gli oggetti. L'ORM fa da "ponte" tra il tuo codice Python e le tabelle del database.

---

### 3️⃣ Applicazione aggiornata con SQLite (`app.py`)

Ecco come cambia il codice. Nota come spariscono le funzioni `load_users` e `save_users` manuali:

```python
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configurazione Database (creerà il file site.db)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data', 'users.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- MODELLO DATI ---
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}

# Creazione del database se non esiste
with app.app_context():
    if not os.path.exists('data'):
        os.makedirs('data')
    db.create_all()

# --- ROTTE ---

@app.route("/")
def home():
    users = User.query.all() # Prende tutti gli utenti dal DB
    return render_template("home.html", users=users)

@app.route("/api/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users])

@app.route("/api/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict())

@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Dati incompleti"}), 400
    
    new_user = User(name=data['name'], email=data['email'])
    
    try:
        db.session.add(new_user)
        db.session.commit() # Salva definitivamente nel DB
        return jsonify(new_user.to_dict()), 201
    except:
        db.session.rollback()
        return jsonify({"error": "Email già esistente"}), 400

@app.route("/api/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "Utente eliminato"})

if __name__ == "__main__":
    app.run(debug=True)

```

---

### 4️⃣ Perché SQLite è meglio del JSON?

| Caratteristica  | File JSON                                             | SQLite (SQLAlchemy)                                      |
| --------------- | ----------------------------------------------------- | -------------------------------------------------------- |
| **Concorrenza** | Rischio di corruzione se due utenti scrivono insieme. | Gestisce gli accessi simultanei in sicurezza.            |
| **Velocità**    | Devi caricare l'intero file in RAM ogni volta.        | Cerca solo i dati necessari (molto più veloce).          |
| **Integrità**   | Puoi scrivere dati errati per sbaglio.                | Vincoli (es. email deve essere unica) nativi.            |
| **Ricerca**     | Devi scrivere cicli `for` complessi.                  | Query potenti (es. `User.query.filter_by(name='Luca')`). |

---

### 🔍 Cosa è cambiato nel codice?

1. **Modello (Classe `User`)**: Abbiamo definito lo schema della tabella. Ogni istanza della classe sarà una riga del DB.
2. **`db.session`**: È il "blocco note" di Flask. Aggiungi i cambiamenti con `add()` e poi li scrivi "sulla pietra" con `commit()`.
3. **Query integrate**: Metodi come `User.query.all()` o `User.query.get_or_404()` rendono la lettura dei dati immediata e pulita.

---

## Form html

Con un form HTML chiudiamo il cerchio: l'utente può interagire con il database direttamente dal browser senza usare strumenti tecnici come cURL o Postman.

Per farlo, dobbiamo modificare la rotta principale `@app.route("/")` in modo che accetti sia la visualizzazione (**GET**) che l'invio dei dati (**POST**).

---

### 1️⃣ Il Flusso dei Dati

Ecco come si muovono le informazioni quando premiamo "Invia" sul form:

---

### 2️⃣ Aggiornamento del Template (`templates/home.html`)

Aggiungiamo un semplice form sopra la lista degli utenti. Useremo l'attributo `name` nei campi input, perché è così che Flask identificherà i dati.

```html
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>Gestione Utenti</title>
    <style>
        body { font-family: sans-serif; margin: 40px; max-width: 600px; }
        .user-card { border: 1px solid #ddd; padding: 10px; margin-bottom: 5px; border-radius: 5px; display: flex; justify-content: space-between; }
        form { background: #f4f4f4; padding: 20px; border-radius: 8px; margin-bottom: 30px; }
        input { display: block; width: 95%; margin-bottom: 10px; padding: 8px; }
        button { background: #28a745; color: white; border: none; padding: 10px; cursor: pointer; width: 100%; }
        .btn-del { background: #dc3545; padding: 5px 10px; font-size: 0.8em; }
    </style>
</head>
<body>

    <h1>Nuovo Utente</h1>
    <form method="POST">
        <input type="text" name="nome_utente" placeholder="Nome completo" required>
        <input type="email" name="email_utente" placeholder="Email" required>
        <button type="submit">Aggiungi Utente</button>
    </form>

    <hr>

    <h1>Utenti Registrati</h1>
    <div>
        {% for user in users %}
        <div class="user-card">
            <span><strong>{{ user.name }}</strong> ({{ user.email }})</span>
        </div>
        {% else %}
        <p>Nessun utente presente.</p>
        {% endfor %}
    </div>

</body>
</html>

```

---

### 3️⃣ Aggiornamento della Logica (`app.py`)

Dobbiamo modificare la rotta `home` per gestire l'invio del form. Useremo `request.form` invece di `request.get_json()`.

```python
from flask import Flask, render_template, request, redirect, url_for, flash
# ... (importazioni precedenti e configurazione DB rimangono uguali)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Recuperiamo i dati dai campi 'name' del form HTML
        nome = request.form.get("nome_utente")
        email = request.form.get("email_utente")

        if nome and email:
            new_user = User(name=nome, email=email)
            try:
                db.session.add(new_user)
                db.session.commit()
                # Redirect alla stessa pagina per "pulire" il form
                return redirect(url_for('home'))
            except:
                db.session.rollback()
                return "Errore: Email probabilmente già esistente.", 400

    # Se GET, mostriamo la pagina normalmente
    users = User.query.all()
    return render_template("home.html", users=users)

```

---

### 🛠️ Cosa è cambiato?

1. **`request.form`**: Quando un form HTML viene inviato, i dati non arrivano come JSON, ma come "form-data". Flask li rende disponibili in questo dizionario speciale.
2. **`redirect(url_for('home'))`**: Questa è una *best practice* chiamata **Post/Redirect/Get**. Serve a evitare che, se l'utente aggiorna la pagina (F5) dopo aver inviato il form, il browser provi a inviare nuovamente i dati creando duplicati.
3. **Metodi Multipli**: La funzione `home()` ora fa due lavori: mostra la lista (GET) e salva i dati (POST).

### 📝 Riepilogo delle differenze

| Tipo Richiesta | Sorgente Dati          | Metodo Flask         | Tipico Utilizzo              |
| -------------- | ---------------------- | -------------------- | ---------------------------- |
| **Form HTML**  | `<form>`               | `request.form.get()` | App Web classiche            |
| **API REST**   | JSON (JavaScript/cURL) | `request.get_json()` | Mobile App / Single Page App |

---

## ORM

Flask (in realtà `json.dumps`) non sa come convertire automaticamente un tuo oggetto Python (es. `Studente`) in JSON.

Devi trasformarlo in **dict** prima di restituirlo.

---

## Soluzione consigliata: `dataclass` + `asdict()`

```python
from dataclasses import dataclass, asdict
from flask import jsonify

@dataclass
class Studente:
    id: int
    nome: str
    email: str
```

Poi nel controller Flask:

```python
@app.get("/studenti")
def get_studenti():
    cursor.execute("SELECT id, nome, email FROM studenti")
    rows = cursor.fetchall()

    studenti = [Studente(*row) for row in rows]

    return jsonify([asdict(s) for s in studenti])
```

---

## Se hai usato cursore `dictionary=True`

Allora è ancora più semplice, perché hai già dizionari:

```python
cursor = conn.cursor(dictionary=True)

@app.get("/studenti")
def get_studenti():
    cursor.execute("SELECT id, nome, email FROM studenti")
    rows = cursor.fetchall()  # lista di dict

    return jsonify(rows)
```

---

## Se NON usi dataclass: metodo `to_dict()`

```python
class Studente:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email
        }
```

Controller:

```python
return jsonify([s.to_dict() for s in studenti])
```

---

## Trucco veloce (ma meno pulito)

```python
return jsonify([s.__dict__ for s in studenti])
```

Funziona se l’oggetto contiene solo attributi semplici.

---

### Nota importante

Se dentro hai tipi non serializzabili (es. `datetime`, `Decimal`) devi convertirli (stringa o float), altrimenti Flask darà lo stesso errore.

