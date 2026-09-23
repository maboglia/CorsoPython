# Python — Ambienti virtuali con `venv`

## 1. Perché usare un ambiente virtuale?

Un ambiente virtuale permette di creare uno spazio Python **isolato** per un progetto.

Senza ambienti virtuali, installando:

```bash
pip install requests
```

il pacchetto viene installato nell'ambiente Python corrente e può entrare in conflitto con altri progetti.

Con `venv` ogni progetto può avere:

* una propria versione delle librerie;
* dipendenze indipendenti dagli altri progetti;
* un ambiente facilmente ricreabile.

Esempio:

```text
progetto-a/
├── .venv/
├── main.py
└── requirements.txt

progetto-b/
├── .venv/
├── main.py
└── requirements.txt
```

I due progetti possono avere versioni differenti delle stesse librerie.

---

## 2. Creare un ambiente virtuale

Dalla directory del progetto:

```bash
python3 -m venv .venv
```

oppure:

```bash
python -m venv .venv
```

Viene creata la directory:

```text
.venv/
```

La scelta del nome `.venv` è una convenzione molto diffusa.

Altri nomi possibili:

```bash
python3 -m venv venv
python3 -m venv env
python3 -m venv ambiente
```

---

## 3. Attivare l'ambiente

### Linux / macOS

```bash
source .venv/bin/activate
```

Il prompt diventa, ad esempio:

```text
(.venv) mauro@pc:~/progetti/mio-progetto$
```

### Windows CMD

```cmd
.venv\Scripts\activate
```

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

---

## 4. Verificare l'ambiente attivo

Una volta attivato:

```bash
python --version
```

e:

```bash
which python
```

su Linux/macOS.

Esempio:

```text
/home/mauro/progetti/mio-progetto/.venv/bin/python
```

Su Windows:

```cmd
where python
```

L'idea fondamentale è:

> **il comando `python` deve puntare al Python contenuto nel `.venv`.**

---

## 5. Installare pacchetti

Con l'ambiente attivo:

```bash
python -m pip install requests
```

È preferibile utilizzare:

```bash
python -m pip
```

invece di:

```bash
pip
```

per essere certi di utilizzare il `pip` associato al Python dell'ambiente attivo.

Esempio:

```bash
python -m pip install flask
python -m pip install requests
```

---

## 6. Visualizzare i pacchetti installati

```bash
python -m pip list
```

Oppure:

```bash
python -m pip freeze
```

La differenza principale è che `pip freeze` produce un formato particolarmente adatto a `requirements.txt`.

Esempio:

```bash
python -m pip freeze > requirements.txt
```

---

## 7. Ricreare l'ambiente

Su un altro computer:

```bash
python3 -m venv .venv
```

poi:

```bash
source .venv/bin/activate
```

e infine:

```bash
python -m pip install -r requirements.txt
```

Il progetto torna ad avere le dipendenze necessarie.

---

# 8. Disattivare l'ambiente

Quando abbiamo finito di lavorare:

```bash
deactivate
```

Il prefisso:

```text
(.venv)
```

scompare dal prompt.

---

# 9. Eliminare un ambiente virtuale

Un ambiente `venv` non richiede una procedura particolare di disinstallazione.

Prima:

```bash
deactivate
```

poi si elimina semplicemente la directory.

Linux/macOS:

```bash
rm -rf .venv
```

Windows:

```cmd
rmdir /s .venv
```

È quindi buona pratica **non inserire `.venv` nel repository Git**.

Nel `.gitignore`:

```gitignore
.venv/
venv/
env/
```

---

# 10. Come vedere gli ambienti virtuali esistenti?

Qui c'è una distinzione importante.

`venv` **non mantiene un registro centrale degli ambienti virtuali**.

Se abbiamo:

```text
progetto1/.venv
progetto2/.venv
progetto3/.venv
```

Python non possiede un comando equivalente a:

```bash
python --list-venvs
```

che li elenchi tutti.

Un ambiente `venv` è semplicemente **una directory contenente un'installazione Python isolata**.

## Cercare i `.venv` nel proprio spazio di lavoro

Linux/macOS:

```bash
find ~ -type d -name ".venv" 2>/dev/null
```

Oppure cercare anche nomi tradizionali:

```bash
find ~ -type d \( -name ".venv" -o -name "venv" -o -name "env" \) 2>/dev/null
```

Per esempio:

```text
/home/mauro/progetti/app1/.venv
/home/mauro/progetti/app2/.venv
/home/mauro/corsi/python/esercizio/.venv
```

---

# 11. Elenco degli ambienti con `pyenv`

Se si utilizza **pyenv**, la situazione è diversa.

Possiamo avere:

```bash
pyenv versions
```

per vedere le versioni Python gestite da `pyenv`.

Se utilizziamo `pyenv-virtualenv`:

```bash
pyenv virtualenvs
```

Esempio:

```text
  3.12.5/env1
  3.12.5/myproject
  3.13.1/data-analysis
```

Questi sono ambienti gestiti da `pyenv`, non semplicemente directory `venv` create manualmente.

---

# 12. Ambiente attualmente attivo

Possiamo controllare la variabile:

```bash
echo $VIRTUAL_ENV
```

Esempio:

```text
/home/mauro/progetti/python/app/.venv
```

Se non c'è un ambiente attivo, normalmente non viene restituito alcun valore.

Un altro controllo utile:

```bash
which python
```

e:

```bash
python -m pip --version
```

Ad esempio:

```text
pip 25.x from /home/mauro/progetti/app/.venv/lib/python3.13/site-packages/pip
```

Questo ci permette di verificare **esattamente quale ambiente stiamo utilizzando**.

---

# 13. `venv` e IDE

IDE come **Eclipse, PyCharm e VS Code** possono individuare e utilizzare un ambiente virtuale.

Per esempio, in un progetto:

```text
mio-progetto/
│
├── .venv/
│   ├── bin/
│   ├── lib/
│   └── ...
│
├── src/
│   └── main.py
│
├── requirements.txt
└── README.md
```

L'IDE può essere configurato per utilizzare:

```text
mio-progetto/.venv/bin/python
```

In questo caso non è necessariamente necessario attivare manualmente il `venv` dal terminale dell'IDE.

---

# 14. Workflow consigliato

Per un nuovo progetto Python:

```bash
mkdir mio-progetto
cd mio-progetto
```

Creazione:

```bash
python3 -m venv .venv
```

Attivazione:

```bash
source .venv/bin/activate
```

Aggiornamento di `pip`:

```bash
python -m pip install --upgrade pip
```

Installazione delle dipendenze:

```bash
python -m pip install requests
```

Salvataggio:

```bash
python -m pip freeze > requirements.txt
```

Lavoro:

```bash
python main.py
```

Fine:

```bash
deactivate
```

---

## Schema riassuntivo

| Operazione            | Comando                                     |
| --------------------- | ------------------------------------------- |
| Creare ambiente       | `python -m venv .venv`                      |
| Attivare Linux/macOS  | `source .venv/bin/activate`                 |
| Attivare Windows      | `.venv\Scripts\activate`                    |
| Verificare Python     | `python --version`                          |
| Individuare Python    | `which python`                              |
| Installare pacchetto  | `python -m pip install nome`                |
| Elencare pacchetti    | `python -m pip list`                        |
| Salvare dipendenze    | `python -m pip freeze > requirements.txt`   |
| Installare dipendenze | `python -m pip install -r requirements.txt` |
| Disattivare           | `deactivate`                                |
| Cercare `.venv`       | `find ~ -type d -name ".venv"`              |
| Ambienti pyenv        | `pyenv virtualenvs`                         |

### Concetto chiave da ricordare

```text
Python
  │
  ├── Progetto A
  │     └── .venv
  │           ├── Python
  │           └── pacchetti A
  │
  ├── Progetto B
  │     └── .venv
  │           ├── Python
  │           └── pacchetti B
  │
  └── Progetto C
        └── .venv
              ├── Python
              └── pacchetti C
```

**`venv` non gestisce una lista globale degli ambienti:** ogni ambiente è una directory autonoma. Se vuoi sapere quali hai già creato, devi cercare le directory (`.venv`, `venv`, ecc.) oppure usare un gestore come `pyenv-virtualenv`.
