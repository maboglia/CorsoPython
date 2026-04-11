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

---

# 📌 Libreria `pathlib` – Scheda Completa

È la libreria moderna per gestire percorsi, file e directory.
Molto più pulita di `os.path`.

```python
from pathlib import Path
```

---

## 1) Creare un percorso

```python
from pathlib import Path

p = Path("cartella/file.txt")
print(p)
```

Percorso corrente:

```python
print(Path.cwd())
```

Home utente:

```python
print(Path.home())
```

---

## 2) Unire percorsi (operatore `/`)

```python
from pathlib import Path

p = Path("cartella") / "file.txt"
print(p)
```

---

## 3) Controllare esistenza

```python
p = Path("file.txt")

print(p.exists())
print(p.is_file())
print(p.is_dir())
```

---

## 4) Creare cartelle

```python
from pathlib import Path

Path("nuova").mkdir()
```

Creare cartelle annidate:

```python
Path("a/b/c").mkdir(parents=True, exist_ok=True)
```

---

## 5) Eliminare file

```python
Path("file.txt").unlink()
```

---

## 6) Eliminare cartella vuota

```python
Path("cartella").rmdir()
```

---

## 7) Leggere e scrivere file facilmente

### Scrivere testo

```python
from pathlib import Path

Path("file.txt").write_text("Ciao mondo", encoding="utf-8")
```

### Leggere testo

```python
testo = Path("file.txt").read_text(encoding="utf-8")
print(testo)
```

---

## 8) Leggere e scrivere binario

```python
Path("file.bin").write_bytes(b"\x01\x02\x03")
dati = Path("file.bin").read_bytes()
```

---

## 9) Listare directory

```python
from pathlib import Path

for f in Path(".").iterdir():
    print(f)
```

Solo file `.txt`:

```python
for f in Path(".").glob("*.txt"):
    print(f)
```

Ricorsivo:

```python
for f in Path(".").rglob("*.py"):
    print(f)
```

---

## 10) Informazioni su percorso

```python
p = Path("cartella/file.txt")

print(p.name)        # file.txt
print(p.stem)        # file
print(p.suffix)      # .txt
print(p.parent)      # cartella
print(p.absolute())  # percorso assoluto
```

---

## 11) Rinominare/spostare file

```python
p = Path("file.txt")

p.rename("nuovo.txt")
```

Oppure spostare:

```python
p.replace("backup/file.txt")
```

---

## 12) Ottenere dimensione file

```python
p = Path("file.txt")
print(p.stat().st_size)
```

---

## 13) Best practice

✅ usare `Path` sempre nei progetti moderni
✅ usare `glob/rglob` per ricerche file
✅ usare `read_text/write_text` per file testuali
⚠️ attenzione: `unlink()` cancella davvero

---

# 🔥 Confronto rapido os vs pathlib

| Operazione    | os                  | pathlib          |
| ------------- | ------------------- | ---------------- |
| join path     | `os.path.join(a,b)` | `Path(a)/b`      |
| esiste?       | `os.path.exists()`  | `Path.exists()`  |
| lista file    | `os.listdir()`      | `Path.iterdir()` |
| crea dir      | `os.makedirs()`     | `Path.mkdir()`   |
| cancella file | `os.remove()`       | `Path.unlink()`  |

📌 `pathlib` è più moderno e leggibile.
