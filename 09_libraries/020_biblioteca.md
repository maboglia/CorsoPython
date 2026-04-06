# 🏆 PROGETTO FINALE: Sistema Gestione Biblioteca

**Obiettivo:** Creare un programma che gestisca il prestito dei libri, calcoli le scadenze e salvi tutto in un database professionale.

---

## 🛠️ Come lavorano insieme i moduli?

1. **`pathlib`**: Serve a definire dove salvare il database, assicurandosi che il programma funzioni su qualsiasi cartella.
2. **`sqlite3`**: È il cuore del progetto. Memorizza i libri, i nomi degli utenti e le date.
3. **`datetime`**: Serve a registrare il momento esatto del prestito e a calcolare la data di restituzione (es. tra 15 giorni).

---

## 1. La Struttura dei Dati

Il nostro database si chiamerà `biblioteca.db` e conterrà una tabella chiamata `prestiti` con queste colonne:

* **Titolo**: Nome del libro.
* **Utente**: Chi ha preso il libro.
* **Inizio**: Data del prestito.
* **Scadenza**: Data entro cui restituirlo.

---

## 2. Lo Scheletro del Progetto (Da completare)

```python
import sqlite3
from datetime import datetime, timedelta
from pathlib import Path

# --- CONFIGURAZIONE PERCORSO (pathlib) ---
# Creiamo il percorso per il database nella cartella corrente
percorso_db = Path.cwd() / "biblioteca.db"

def inizializza_db():
    """Crea il database e la tabella se non esistono."""
    conn = sqlite3.connect(percorso_db)
    cursor = conn.cursor()
    # TODO: Crea la tabella 'prestiti' con le colonne: titolo, utente, inizio, scadenza
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS prestiti (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titolo TEXT,
            utente TEXT,
            inizio TEXT,
            scadenza TEXT
        )
    ''')
    conn.commit()
    conn.close()

def registra_prestito():
    """Registra un nuovo prestito calcolando le date."""
    titolo = input("Titolo del libro: ")
    utente = input("Nome utente: ")

    # --- LOGICA DEL TEMPO (datetime) ---
    # 1. Prendi la data di oggi
    oggi = datetime.now()
    
    # 2. Calcola la scadenza tra 14 giorni
    # TODO: Usa timedelta(days=14)
    data_scadenza = oggi + timedelta(days=14)

    # Formattiamo le date come stringhe leggibili (es. 2023-12-31)
    inizio_str = oggi.strftime("%d/%m/%Y")
    scadenza_str = data_scadenza.strftime("%d/%m/%Y")

    # --- SALVATAGGIO (sqlite3) ---
    conn = sqlite3.connect(percorso_db)
    cursor = conn.cursor()
    # TODO: Inserisci i dati nella tabella
    cursor.execute("INSERT INTO prestiti (titolo, utente, inizio, scadenza) VALUES (?, ?, ?, ?)", 
                   (titolo, utente, inizio_str, scadenza_str))
    conn.commit()
    conn.close()
    print(f"Prestito registrato! Scadenza: {scadenza_str}")

def visualizza_prestiti():
    """Mostra tutti i prestiti attivi."""
    conn = sqlite3.connect(percorso_db)
    cursor = conn.cursor()
    # TODO: Seleziona tutti i dati dalla tabella prestiti
    cursor.execute("SELECT * FROM prestiti")
    righe = cursor.fetchall()
    
    print("\n--- ELENCO PRESTITI ---")
    for riga in righe:
        print(f"ID: {riga[0]} | Libro: {riga[1]} | Utente: {riga[2]} | Scadenza: {riga[4]}")
    conn.close()

# --- AVVIO PROGRAMMA ---
if __name__ == "__main__":
    inizializza_db()
    while True:
        print("\n1. Nuovo Prestito | 2. Elenco | 3. Esci")
        scelta = input("Scegli: ")
        if scelta == "1": registra_prestito()
        elif scelta == "2": visualizza_prestiti()
        elif scelta == "3": break

```

---

## 🧐 Approfondimento per lo studente

### La magia di `timedelta`

Nel progetto abbiamo usato `timedelta(days=14)`. Questo oggetto è fondamentale perché Python gestisce automaticamente il passaggio tra mesi e anni. Se presti un libro il 28 dicembre, Python sa che tra 14 giorni saremo a gennaio dell'anno dopo!

### Perché `Path.cwd() / "nome.db"`?

L'operatore `/` usato con `Path` non è una divisione matematica. `pathlib` ha "sovrascritto" quell'operatore per permetterti di unire percorsi in modo elegante, sostituendo il vecchio e noioso `os.path.join()`.

---

## 🌟 Sfide Extra

1. **Cerca Scadenze**: Aggiungi una funzione che mostri solo i libri la cui scadenza è oggi (usa `datetime.now().strftime(...)` per il confronto).
2. **Cancellazione**: Aggiungi una funzione per eliminare un prestito dal database quando il libro viene restituito (usa il comando SQL `DELETE FROM prestiti WHERE id = ?`).
3. **Esporta in JSON**: Usa il modulo `json` per esportare l'elenco dei prestiti in un file `.json` di backup.

---

### Cosa abbiamo imparato?

Con questo progetto, hai creato un software che:

* Ha una **memoria a lungo termine** (Database).
* Capisce il **concetto di tempo** (Scadenze).
* Sa **dove si trova** nel computer (File System).
