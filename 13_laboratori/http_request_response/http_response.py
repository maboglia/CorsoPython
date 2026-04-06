from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", title="Home Page", users = ["Mauro", "Giulia", "Luca"])

@app.route("/hello", methods=["GET"])
def hello():
    return "Ciao!"

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    return jsonify({"message": f"Benvenuto {username}"})

app.run(debug=True)