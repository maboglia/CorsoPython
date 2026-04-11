# Connessione al database MySQL
# scaricare mysql-connector-python con pip install mysql-connector-python
import mysql.connector


db = mysql.connector.connect(
    host= "localhost",
    user= "root",
    password= "root",
    database= "magazzino"
)

cursor = db.cursor()

def insert_product(id_prodotto, nome, prezzo_unitario, quantita_stock, id_categoria, id_fornitore):
    sql = "INSERT INTO prodotti (id_prodotto, nome, prezzo_unitario, quantita_stock, id_categoria, id_fornitore) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (id_prodotto, nome, prezzo_unitario, quantita_stock, id_categoria, id_fornitore)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "record inserted.")
    
def get_all_products():
    cursor.execute("SELECT * FROM prodotti")
    return cursor.fetchall()

def get_all_categories():
    cursor.execute("SELECT * FROM categorie")
    return cursor.fetchall()

def get_all_suppliers():
    cursor.execute("SELECT * FROM fornitori")
    return cursor.fetchall()

def get_products_by_name(nome):
    sql = "SELECT * FROM prodotti WHERE nome LIKE %s"
    val = ("%" + nome + "%",)
    cursor.execute(sql, val)
    return cursor.fetchall()


def update_product(id, nome=None, prezzo_unitario=None, quantita_stock=None):
    updates = []
    values = []
    
    if nome is not None:
        updates.append("nome = %s")
        values.append(nome)
    if prezzo_unitario is not None:
        updates.append("prezzo_unitario = %s")
        values.append(prezzo_unitario)
    if quantita_stock is not None:
        updates.append("quantita_stock = %s")
        values.append(quantita_stock)
    
    if not updates:
        print("No fields to update.")
        return
    
    sql = "UPDATE prodotti SET " + ", ".join(updates) + " WHERE id = %s"
    values.append(id)
    
    cursor.execute(sql, tuple(values))
    db.commit()
    print(cursor.rowcount, "record(s) updated.")
    
def delete_product(id):
    sql = "DELETE FROM prodotti WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "record(s) deleted.")

def close_connection():
    if cursor and db:
        cursor.close()
        db.close()