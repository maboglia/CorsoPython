# gestione_magazzino.py
# Questo file contiene funzioni per gestire il magazzino, come visualizzare prodotti, categorie e fornitori.
import database_magazzino as db


print("\nProdotti:")

prodotti = db.get_all_products()

for prodotto in prodotti:
    print(prodotto)

print("\nProdotti:")

nome_prodotto = input("Inserisci il nome del prodotto da cercare: ")

prodotti = db.get_products_by_name(nome_prodotto)

for prodotto in prodotti:
    print(prodotto)

print("\nCategorie:")

categorie = db.get_all_categories()

for categoria in categorie:
    print(categoria)

print("\nFornitori:")

fornitori = db.get_all_suppliers()

for fornitore in fornitori:
    print(fornitore)
    
db.close_connection()