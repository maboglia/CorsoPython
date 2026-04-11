import mysql.connector

magazzino = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "magazzino"
)

cursore = magazzino.cursor()

query = """
    select 
        p.nome as 'nome_prodotto',
        p.prezzo_unitario as prezzo, 
        p.quantita_stock as stock, 
        c.nome as 'categoria', 
        f.ragione_sociale as 'fornitore' 
    from prodotti p
    join fornitori f using (id_fornitore)
    join categorie c using (id_categoria)
    order by categoria, fornitore
    ; 
"""

cursore.execute(query)

prodotti = cursore.fetchall()

cursore.close()
magazzino.close()


