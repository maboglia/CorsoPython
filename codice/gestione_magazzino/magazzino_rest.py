from magazzino_service import MagazzinoService
#pip install flask
from flask import Flask, jsonify

app = Flask(__name__)

service = MagazzinoService()

@app.get('/api/prodotti')
def prodotti():
    return jsonify([product.to_dict() for product in service.getAllProducts()])


@app.get('/api/categorie')
def categorie():
    return jsonify([categorie.to_dict() for categorie in service.getAllCategories()])



app.run(debug=True)
