# 13. Modulo `sqlite3`: Il tuo primo Database

Molti studenti pensano che serva un server complesso per usare i database. Invece, Python ha **SQLite** integrato: un database potente che salva tutto in un unico file `.db`.

* **Concetto chiave:** Linguaggio SQL (Structured Query Language).
* **Flusso di lavoro:** Connessione → Cursore → Esecuzione comando → Commit (salvataggio).

## 💡 Esercizio: "Il Registro dei Videogiochi"

```python
import sqlite3

def gestore_database():
    # 1. Connettiti al database (lo crea se non esiste)
    connessione = sqlite3.connect("videogiochi.db")
    cursore = connessione.cursor()

    # 2. Crea una tabella
    cursore.execute("CREATE TABLE IF NOT EXISTS giochi (titolo TEXT, anno INTEGER)")

    # 3. Inserisci un dato
    titolo = input("Inserisci titolo gioco: ")
    anno = int(input("Anno di uscita: "))
    # TODO: Usa cursore.execute("INSERT INTO giochi VALUES (?, ?)", (titolo, anno))
    
    # 4. Salva e chiudi
    connessione.commit()
    connessione.close()
    print("Dati salvati con successo!")

# Sfida: Scrivi una funzione che legga tutti i giochi dal database usando "SELECT * FROM giochi"

```
