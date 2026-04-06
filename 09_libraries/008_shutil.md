# Modulo `shutil`: Il Gestore di File (Livello High-Level)

Mentre `os` lavora sui percorsi, `shutil` è la "ruspa" che serve per spostare e copiare intere cartelle o file con un solo comando.

```python
import shutil
import os

def gestore_archivi():
    file_origine = "appunti.txt"
    file_destinazione = "appunti_backup.txt"

    # Creiamo un file di prova se non esiste
    with open(file_origine, "w") as f:
        f.write("Questi sono i miei appunti di Python.")

    # 1. Copia il file
    # TODO: Usa shutil.copy(origine, destinazione)
    
    # 2. Crea un archivio compresso (ZIP) di una cartella
    # TODO: Usa shutil.make_archive("nome_zip", "zip", "cartella_da_zippare")
    # Nota: Assicurati che la cartella esista!

    print(f"Copia di {file_origine} creata con successo.")

# Sfida Extra: Scrivi una funzione che cerchi tutti i file .png e li sposti in una cartella 'Immagini'

```
