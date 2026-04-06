# Moduli built-in di Python: Guida Rapida

Python è famoso per la sua filosofia **"batteries included"**: la sua libreria standard è vastissima e permette di fare quasi tutto senza installare pacchetti esterni.

Ecco una panoramica dei moduli built-in più utilizzati e dei loro metodi principali.

---

## 🛠️ Interazione con il Sistema Operativo

Questi moduli sono fondamentali per gestire file, cartelle e parametri di sistema.

### 1. `os` (Operating System)

Permette di interagire con il sistema operativo sottostante.

* `os.getcwd()`: Restituisce la directory di lavoro corrente.
* `os.listdir(path)`: Elenca i file e le cartelle in un percorso.
* `os.mkdir(dir)`: Crea una nuova cartella.
* `os.path.join(path, *paths)`: Unisce diversi segmenti di percorso in modo intelligente (gestendo `/` o `\`).
* `os.path.exists(path)`: Verifica se un file o una cartella esiste.

### 2. `sys` (System-specific parameters)

Fornisce l'accesso a variabili e funzioni utilizzate dall'interprete Python.

* `sys.argv`: Una lista che contiene gli argomenti passati da riga di comando.
* `sys.exit()`: Esce dal programma.
* `sys.path`: Una lista di stringhe che specifica i percorsi di ricerca per i moduli.

---

## 🔢 Matematica e Logica

### 3. `math`

Fornisce funzioni matematiche per numeri reali.

* `math.sqrt(x)`: Radice quadrata.
* `math.ceil(x)` / `math.floor(x)`: Arrotondamento per eccesso o per difetto.
* `math.pi`: La costante Pi greco.
* `math.pow(x, y)`: Elevamento a potenza.

### 4. `random`

Utilizzato per generare numeri pseudo-casuali.

* `random.random()`: Restituisce un float tra 0.0 e 1.0.
* `random.randint(a, b)`: Restituisce un intero casuale tra `a` e `b` inclusi.
* `random.choice(sequence)`: Sceglie un elemento a caso da una lista o tupla.
* `random.shuffle(list)`: Mescola gli elementi di una lista sul posto.

---

## 📅 Gestione Dati e Tempo

### 5. `datetime`

Indispensabile per manipolare date e orari.

* `datetime.datetime.now()`: Restituisce la data e l'ora attuali.
* `datetime.date(year, month, day)`: Crea un oggetto data.
* `strftime(format)`: Formatta una data in una stringa leggibile (es. `"%d/%m/%Y"`).
* `strptime(string, format)`: Converte una stringa in un oggetto datetime.

### 6. `json`

Per codificare e decodificare dati in formato JSON (standard nel web).

* `json.dumps(obj)`: Converte un dizionario/lista Python in una stringa JSON.
* `json.loads(string)`: Converte una stringa JSON in un oggetto Python.
* `json.dump(obj, file)`: Scrive dati JSON direttamente in un file.

---

## 🔍 Manipolazione Testo e Dati complessi

### 7. `re` (Regular Expressions)

Per la ricerca e manipolazione avanzata di stringhe tramite espressioni regolari.

* `re.search(pattern, string)`: Cerca la prima corrispondenza del pattern.
* `re.findall(pattern, string)`: Restituisce una lista di tutte le corrispondenze.
* `re.sub(pattern, repl, string)`: Sostituisce le occorrenze del pattern con una stringa.

### 8. `collections`

Offre tipi di dati specializzati che estendono i classici `dict`, `list`, `set` e `tuple`.

* `Counter`: Conta gli elementi in un iterabile.
* `namedtuple()`: Crea tuple i cui elementi sono accessibili anche tramite nome.
* `defaultdict`: Un dizionario che non solleva errori se una chiave è assente, ma crea un valore di default.

---

### Tabella Riassuntiva Rapida

| Modulo | Scopo Principale | Metodo Simbolo |
| --- | --- | --- |
| **os** | File system | `os.path.join()` |
| **sys** | Interprete | `sys.argv` |
| **math** | Calcoli scientifici | `math.sqrt()` |
| **datetime** | Gestione tempo | `datetime.now()` |
| **json** | Scambio dati | `json.loads()` |
| **random** | Casualità | `random.randint()` |

