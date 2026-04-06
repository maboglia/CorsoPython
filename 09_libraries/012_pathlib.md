# 12. Modulo `pathlib`: Gestire i percorsi come oggetti

Mentre il modulo `os` tratta i percorsi dei file come semplici stringhe, `pathlib` li tratta come **oggetti**. È il modo moderno e più leggibile di scrivere codice oggi.

* **Concetto chiave:** Non più concatenazione manuale di cartelle, ma uso dell'operatore `/`.
* **Metodi principali:**
* `Path.cwd()`: Ottiene la cartella corrente.
* `Path.exists()`: Verifica se il file esiste.
* `Path.read_text()`: Legge tutto il file in una stringa (senza bisogno di `open`).

### 💡 Esercizio: "Il Cercatore di Estensioni"

```python
from pathlib import Path

def analizza_cartella():
    # 1. Crea un oggetto Path per la cartella corrente
    cartella = Path.cwd()
    
    print(f"Sto analizzando: {cartella}")

    # 2. Itera su tutti i file .txt
    # TODO: Usa cartella.glob("*.txt")
    for file in cartella.glob("*.txt"):
        # 3. Stampa nome e dimensione
        # TODO: Usa file.name e file.stat().st_size
        print(f"File: {file.name} - Dimensione: {file.stat().st_size} bytes")

# Sfida: Crea una funzione che legga il contenuto di un file usando solo .read_text()

```
