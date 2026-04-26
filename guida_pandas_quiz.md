# Guida passo passo — Implementare il quiz con pandas

> Scheda di riferimento per il corso Data Analyst · Modulo: Basi di dati con pandas

---

## Passo 1 — Setup e importazioni

Ogni progetto pandas inizia con l'importazione delle librerie e la configurazione dell'ambiente. `pd` è l'alias universale per pandas.

```python
# pip install pandas numpy
import pandas as pd
import numpy as np
import random

# Seed per risultati riproducibili
random.seed(42)
np.random.seed(42)
```

**Nota:** senza `seed`, ogni run del quiz mescolerà le domande in modo diverso.

---

## Passo 2 — Struttura delle domande come DataFrame

Le domande del quiz si archiviano in un DataFrame: ogni riga è una domanda, ogni colonna un campo. Questo permette di filtrare, mescolare e analizzare i risultati con pandas.

```python
domande = pd.DataFrame([
    {
        "id": 1,
        "difficolta": "facile",
        "topic": "Creazione DataFrame",
        "testo": "Quale codice crea un DataFrame da dizionario?",
        "opzioni": ["pd.DataFrame(data)", "pd.dataframe(data)",
                    "DataFrame(data)", "pd.create(data)"],
        "risposta_corretta": 0,
        "spiegazione": "pd.DataFrame() con D maiuscola è il costruttore corretto."
    },
    {
        "id": 2,
        "difficolta": "medio",
        "topic": "groupby",
        "testo": "Cosa calcola df.groupby('cat')['val'].sum()?",
        "opzioni": ["Somma totale", "Conteggio righe per gruppo",
                    "Somma per ogni gruppo", "Media per gruppo"],
        "risposta_corretta": 2,
        "spiegazione": "groupby raggruppa le righe, .sum() somma i valori dentro ogni gruppo."
    },
    # ... aggiungi tutte le domande
])
```

**Colonne chiave del DataFrame:**

| Colonna             | Tipo | Descrizione                          |
| ------------------- | ---- | ------------------------------------ |
| `id`                | int  | identificatore unico                 |
| `difficolta`        | str  | `"facile"`, `"medio"`, `"difficile"` |
| `topic`             | str  | argomento pandas                     |
| `opzioni`           | list | lista di 4 stringhe                  |
| `risposta_corretta` | int  | indice 0–3 della risposta giusta     |
| `spiegazione`       | str  | testo mostrato dopo la risposta      |

---

## Passo 3 — Mescolamento e selezione domande

pandas permette di mescolare le righe con `.sample()` e filtrare per difficoltà con una maschera booleana.

```python
def prepara_quiz(df, n=5, difficolta=None, seed=42):
    """
    Restituisce n domande casuali, opzionalmente filtrate per difficoltà.
    """
    if difficolta:
        # Filtro booleano: seleziona solo le righe con la difficoltà scelta
        df = df[df["difficolta"] == difficolta]

    # .sample() mescola le righe in modo casuale
    quiz = df.sample(n=min(n, len(df)), random_state=seed)

    # reset_index per avere indici 0, 1, 2, ...
    return quiz.reset_index(drop=True)


# Esempio di utilizzo
quiz_misto    = prepara_quiz(domande, n=8)
quiz_facile   = prepara_quiz(domande, n=5, difficolta="facile")
quiz_difficile = prepara_quiz(domande, n=5, difficolta="difficile")
```

**Metodi pandas usati:**

| Metodo                      | Cosa fa                                     |
| --------------------------- | ------------------------------------------- |
| `df[maschera_booleana]`     | filtra le righe dove la condizione è `True` |
| `df.sample(n=k)`            | restituisce k righe casuali                 |
| `df.reset_index(drop=True)` | rinumera gli indici da 0                    |

---

## Passo 4 — Gestione di una singola domanda

Per ogni domanda del quiz, si estrae la riga dal DataFrame con `.iloc[]` e si accede ai campi come colonne.

```python
def mostra_domanda(quiz_df, indice):
    """
    Mostra una domanda e raccoglie la risposta dell'utente.
    Restituisce True se corretta, False altrimenti.
    """
    # .iloc[i] seleziona la riga all'indice intero i
    riga = quiz_df.iloc[indice]

    print(f"\n--- Domanda {indice + 1}/{len(quiz_df)} ---")
    print(f"[{riga['difficolta'].upper()}] {riga['topic']}")
    print(f"\n{riga['testo']}\n")

    # Le opzioni sono una lista nella cella del DataFrame
    for i, opzione in enumerate(riga["opzioni"]):
        print(f"  {i}) {opzione}")

    risposta = int(input("\nLa tua risposta (0-3): "))
    corretta = risposta == riga["risposta_corretta"]

    if corretta:
        print("✓ Corretto!")
    else:
        indice_giusto = riga["risposta_corretta"]
        print(f"✗ Sbagliato. Risposta giusta: {riga['opzioni'][indice_giusto]}")

    print(f"  → {riga['spiegazione']}")
    return corretta
```

---

## Passo 5 — Loop principale del quiz e raccolta risultati

I risultati vengono accumulati in una lista di dizionari e poi convertiti in DataFrame per l'analisi finale.

```python
def esegui_quiz(quiz_df):
    """
    Esegue il quiz completo e restituisce un DataFrame con i risultati.
    """
    risultati = []  # lista di dizionari, diventerà un DataFrame

    for i in range(len(quiz_df)):
        riga = quiz_df.iloc[i]
        corretta = mostra_domanda(quiz_df, i)

        # Ogni risposta viene salvata come dizionario
        risultati.append({
            "domanda_id":  riga["id"],
            "topic":       riga["topic"],
            "difficolta":  riga["difficolta"],
            "corretta":    corretta
        })

    # Convertiamo la lista in DataFrame per analizzare i risultati
    return pd.DataFrame(risultati)
```

**Perché usare un DataFrame per i risultati?**
Perché pandas permette di fare aggregazioni e statistiche in una riga di codice (vedi passo 6).

---

## Passo 6 — Analisi dei risultati con pandas

Con il DataFrame dei risultati si possono calcolare statistiche aggregate in modo conciso.

```python
def analizza_risultati(risultati_df):
    """
    Stampa statistiche finali usando groupby, mean e value_counts.
    """
    totale   = len(risultati_df)
    corrette = risultati_df["corretta"].sum()   # True vale 1, False vale 0
    pct      = corrette / totale * 100

    print(f"\n{'='*40}")
    print(f"RISULTATO FINALE: {corrette}/{totale} ({pct:.0f}%)")
    print(f"{'='*40}")

    # Punteggio per difficoltà con groupby
    print("\nPerformance per difficoltà:")
    per_diff = (
        risultati_df
        .groupby("difficolta")["corretta"]
        .agg(["sum", "count"])           # somma e conteggio per gruppo
        .rename(columns={"sum": "corrette", "count": "totale"})
    )
    per_diff["percentuale"] = (per_diff["corrette"] / per_diff["totale"] * 100).round(0)
    print(per_diff)

    # Topic con più errori
    print("\nArgomenti da ripassare:")
    errori = risultati_df[risultati_df["corretta"] == False]
    if not errori.empty:
        print(errori["topic"].value_counts().to_string())
    else:
        print("  Nessun errore — ottimo!")
```

**Metodi pandas usati:**

| Metodo                   | Cosa fa                                  |
| ------------------------ | ---------------------------------------- |
| `series.sum()`           | somma (True=1, False=0 per booleani)     |
| `groupby().agg([...])`   | aggrega con più funzioni insieme         |
| `.rename(columns={...})` | rinomina le colonne del risultato        |
| `value_counts()`         | conta le occorrenze di ogni valore unico |
| `df[df["col"] == False]` | filtra le righe con risposta sbagliata   |

---

## Passo 7 — Salvataggio e caricamento dati

pandas permette di salvare i risultati in CSV per sessioni successive o analisi esterne.

```python
def salva_sessione(risultati_df, filepath="risultati_quiz.csv"):
    """
    Salva i risultati in CSV. Se il file esiste, appende i nuovi dati.
    """
    try:
        # Legge i dati esistenti e li combina con quelli nuovi
        storico = pd.read_csv(filepath)
        risultati_df["sessione"] = len(storico) // len(risultati_df) + 1
        aggiornato = pd.concat([storico, risultati_df], ignore_index=True)
    except FileNotFoundError:
        # Prima sessione: il file non esiste ancora
        risultati_df["sessione"] = 1
        aggiornato = risultati_df

    aggiornato.to_csv(filepath, index=False)
    print(f"Risultati salvati in '{filepath}'")


def carica_storico(filepath="risultati_quiz.csv"):
    """
    Carica lo storico e mostra il trend di miglioramento.
    """
    try:
        storico = pd.read_csv(filepath)
        trend = storico.groupby("sessione")["corretta"].mean() * 100
        print("\nTrend per sessione (% corrette):")
        print(trend.round(1).to_string())
        return storico
    except FileNotFoundError:
        print("Nessuno storico trovato.")
        return pd.DataFrame()
```

**Metodi pandas usati:**

| Metodo                         | Cosa fa                              |
| ------------------------------ | ------------------------------------ |
| `pd.read_csv(path)`            | legge un CSV come DataFrame          |
| `df.to_csv(path, index=False)` | salva in CSV senza la colonna indice |
| `pd.concat([df1, df2])`        | unisce due DataFrame verticalmente   |

---

## Passo 8 — Main: assemblare tutto

La funzione `main()` orchestra tutti i passi precedenti.

```python
def main():
    # 1. Crea il DataFrame delle domande (vedi passo 2)
    domande = crea_domande()

    # 2. Chiedi le preferenze all'utente
    print("=== QUIZ PANDAS — Fine corso Basi di Dati ===\n")
    scelta = input("Difficoltà? [facile / medio / difficile / tutte]: ").strip()
    difficolta = scelta if scelta in ["facile", "medio", "difficile"] else None

    # 3. Prepara il quiz (passo 3)
    quiz = prepara_quiz(domande, n=8, difficolta=difficolta)
    print(f"\nQuiz pronto: {len(quiz)} domande\n")

    # 4. Esegui il quiz (passi 4-5)
    risultati = esegui_quiz(quiz)

    # 5. Analizza e salva (passi 6-7)
    analizza_risultati(risultati)
    salva_sessione(risultati)
    carica_storico()


if __name__ == "__main__":
    main()
```

---

## Riepilogo — metodi pandas per questa implementazione

| Metodo                       | Passo | Uso nel quiz                                  |
| ---------------------------- | ----- | --------------------------------------------- |
| `pd.DataFrame([...])`        | 2     | crea l'archivio domande e i risultati         |
| `df[maschera]`               | 3, 6  | filtra per difficoltà, filtra risposte errate |
| `df.sample(n)`               | 3     | mescola le domande casualmente                |
| `df.reset_index()`           | 3     | rinumera dopo filtro/sample                   |
| `df.iloc[i]`                 | 4     | accede alla riga i-esima per indice intero    |
| `series.sum()`               | 6     | conta le risposte corrette                    |
| `groupby().agg()`            | 6     | punteggio aggregato per difficoltà/topic      |
| `value_counts()`             | 6     | frequenza errori per argomento                |
| `pd.concat()`                | 7     | unisce storico e nuovi risultati              |
| `pd.read_csv()` / `to_csv()` | 7     | persistenza dati tra sessioni                 |

---

*Scheda per il corso Data Analyst — Basi di dati con pandas*
