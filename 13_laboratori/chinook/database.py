import mysql.connector


def connetti():
    DB = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "chinook"
    )
    return DB


def trova_tutti(DB, tabella):
    cursore = DB.cursor(dictionary=True) # dictionary=True per avere i risultati come dizionari invece che tuple
    
    query = f"""
        select * from {tabella}; 
    """

    cursore.execute(query)

    righe = cursore.fetchall()
    
    cursore.close()

    return righe


def disconnetti(DB):
    if DB.is_connected():
        DB.close()

def main():
    DB = connetti()
    righe = trova_tutti(DB, "album")
    for r in righe:
        print(r)
    disconnetti(DB)

if __name__ == "__main__":
    main()