## Scheda didattica: **Pandas (Python)**

### 1) Cos’è Pandas

**Pandas** è una libreria Python usata per:

* leggere e scrivere dati (CSV, Excel, JSON…)
* manipolare tabelle (dataset)
* fare analisi e pulizia dati
* gestire serie temporali e dati statistici

È lo standard per la **Data Analysis** in Python.

Installazione:

```bash
pip install pandas
```

Import:

```python
import pandas as pd
```

---

## 2) Strutture principali di Pandas

### 🔹 Series

È una **colonna** di dati con indice.

```python
s = pd.Series([10, 20, 30])
print(s)
```

Esempio con indice personalizzato:

```python
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
```

---

### 🔹 DataFrame

È una **tabella** (righe e colonne), simile a una tabella SQL o Excel.

```python
df = pd.DataFrame({
    "Nome": ["Anna", "Luca", "Marco"],
    "Età": [20, 22, 19]
})
print(df)
```

---

## 3) Lettura e scrittura file

### CSV

```python
df = pd.read_csv("file.csv")
```

Scrittura:

```python
df.to_csv("output.csv", index=False)
```

### Excel

```python
df = pd.read_excel("file.xlsx")
```

Scrittura:

```python
df.to_excel("output.xlsx", index=False)
```

### JSON

```python
df = pd.read_json("file.json")
```

---

## 4) Esplorazione dei dati

```python
df.head()      # prime 5 righe
df.tail()      # ultime 5 righe
df.shape       # (righe, colonne)
df.columns     # nomi colonne
df.dtypes      # tipi dati
df.info()      # info complete
df.describe()  # statistiche numeriche
```

---

## 5) Selezione di righe e colonne

### Selezione colonna

```python
df["Nome"]
```

### Selezione più colonne

```python
df[["Nome", "Età"]]
```

### Riga per indice numerico (iloc)

```python
df.iloc[0]       # prima riga
df.iloc[0:3]     # righe 0,1,2
df.iloc[0, 1]    # cella (riga 0, colonna 1)
```

### Riga per etichetta (loc)

```python
df.loc[0]
```

---

## 6) Filtri (condizioni)

```python
df[df["Età"] > 20]
```

Condizioni multiple:

```python
df[(df["Età"] > 18) & (df["Età"] < 22)]
```

Oppure:

```python
df[(df["Età"] == 20) | (df["Età"] == 22)]
```

---

## 7) Ordinamento

```python
df.sort_values("Età")
df.sort_values("Età", ascending=False)
```

---

## 8) Gestione valori mancanti (NaN)

Verifica:

```python
df.isnull()
df.isnull().sum()
```

Rimozione righe con NaN:

```python
df.dropna()
```

Sostituzione NaN:

```python
df.fillna(0)
```

Sostituzione con media:

```python
df["Età"] = df["Età"].fillna(df["Età"].mean())
```

---

## 9) Modifica e creazione colonne

Creare una colonna:

```python
df["AnnoNascita"] = 2025 - df["Età"]
```

Modifica valori:

```python
df["Età"] = df["Età"] + 1
```

---

## 10) Raggruppamenti (groupby)

Esempio:

```python
df.groupby("Classe")["Voto"].mean()
```

Più aggregazioni:

```python
df.groupby("Classe")["Voto"].agg(["mean", "max", "min"])
```

---

## 11) Statistiche rapide

```python
df["Età"].mean()
df["Età"].max()
df["Età"].min()
df["Età"].sum()
df["Età"].count()
```

---

## 12) Eliminare colonne o righe

Eliminare colonna:

```python
df.drop("Età", axis=1)
```

Eliminare riga:

```python
df.drop(0)
```

⚠️ Per rendere permanente:

```python
df.drop("Età", axis=1, inplace=True)
```

---

## 13) Unione di DataFrame (merge / join)

Esempio stile SQL JOIN:

```python
df1 = pd.DataFrame({"ID": [1,2], "Nome": ["Anna","Luca"]})
df2 = pd.DataFrame({"ID": [1,2], "Voto": [28,30]})

df_merge = pd.merge(df1, df2, on="ID")
```

---

## 14) Concatenazione (append di tabelle)

```python
df_tot = pd.concat([df1, df2])
```

---

## 15) Tabelle pivot (pivot_table)

```python
df.pivot_table(values="Voto", index="Classe", aggfunc="mean")
```

---

# Mini Esercitazione Completa

Dataset studenti:

```python
import pandas as pd

df = pd.DataFrame({
    "Nome": ["Anna", "Luca", "Marco", "Sara"],
    "Classe": ["3A", "3A", "3B", "3B"],
    "Voto": [8, 6, 9, 7]
})

print(df)
```

### 1) Media voti per classe

```python
print(df.groupby("Classe")["Voto"].mean())
```

### 2) Studenti con voto >= 8

```python
print(df[df["Voto"] >= 8])
```

### 3) Ordinamento decrescente per voto

```python
print(df.sort_values("Voto", ascending=False))
```

### 4) Nuova colonna “Esito”

```python
df["Esito"] = df["Voto"].apply(lambda x: "Promosso" if x >= 6 else "Bocciato")
print(df)
```

---

# Funzioni fondamentali da ricordare (riassunto)

| Funzione     | Significato             |
| ------------ | ----------------------- |
| `read_csv()` | Legge un CSV            |
| `to_csv()`   | Scrive un CSV           |
| `head()`     | Prime righe             |
| `info()`     | Info sul dataset        |
| `describe()` | Statistiche             |
| `loc[]`      | Selezione per etichetta |
| `iloc[]`     | Selezione per posizione |
| `groupby()`  | Raggruppa dati          |
| `merge()`    | Join tipo SQL           |
| `fillna()`   | Sostituisce NaN         |
| `drop()`     | Elimina righe/colonne   |

---

## Scheda didattica avanzata: **Pandas (Python)**

*(Data Analysis, pulizia dati, trasformazioni, serie temporali, pivot, join, performance)*

---

# 1) Concetti chiave avanzati

### DataFrame come struttura tabellare “intelligente”

Un DataFrame è:

* una tabella (righe/colonne)
* con **indici**
* con tipi dati (dtype)
* con funzioni di analisi, trasformazione e aggregazione

📌 Differenza importante:

* **colonne** = variabili
* **righe** = osservazioni
* **index** = identificatore (tipo chiave primaria)

---

# 2) Indici avanzati (Index, MultiIndex)

### Impostare una colonna come indice

```python
df = df.set_index("ID")
```

Ripristinare indice numerico:

```python
df = df.reset_index()
```

---

### MultiIndex (indice gerarchico)

```python
df = df.set_index(["Classe", "Studente"])
```

Selezione:

```python
df.loc["3A"]
```

Selezione di un valore specifico:

```python
df.loc[("3A", "Luca")]
```

📌 MultiIndex è utile in:

* dati multidimensionali
* tabelle pivot complesse
* reportistica

---

# 3) Selezioni avanzate (loc, iloc, query)

### Filtri con query()

Molto leggibile (simile SQL):

```python
df.query("Voto >= 6 and Classe == '3A'")
```

Con variabile esterna:

```python
soglia = 8
df.query("Voto >= @soglia")
```

---

# 4) Tipi di dato e conversioni (dtype)

Controllo tipi:

```python
df.dtypes
```

Conversione:

```python
df["Età"] = df["Età"].astype(int)
df["Voto"] = df["Voto"].astype(float)
```

Conversione sicura con errori gestiti:

```python
df["Voto"] = pd.to_numeric(df["Voto"], errors="coerce")
```

Conversione a categoria (ottimizza memoria):

```python
df["Classe"] = df["Classe"].astype("category")
```

📌 `category` è utile quando la colonna contiene valori ripetuti (es. classe, città, genere).

---

# 5) Pulizia dati (Data Cleaning)

### Rimuovere duplicati

```python
df.drop_duplicates()
df.drop_duplicates(subset=["Nome"])
```

---

### Gestione valori mancanti (NaN)

Conteggio:

```python
df.isnull().sum()
```

Rimozione:

```python
df.dropna()
df.dropna(subset=["Voto"])
```

Sostituzione:

```python
df.fillna(0)
```

Sostituzione per colonna:

```python
df["Voto"] = df["Voto"].fillna(df["Voto"].mean())
```

Sostituzione per gruppo:

```python
df["Voto"] = df.groupby("Classe")["Voto"].transform(lambda x: x.fillna(x.mean()))
```

📌 `transform()` è fondamentale perché mantiene la stessa lunghezza del DataFrame.

---

# 6) Operazioni su colonne (apply, map, replace)

### map() (per Series)

```python
df["Classe"] = df["Classe"].map({"3A": "Terza A", "3B": "Terza B"})
```

---

### apply() (per colonna o per riga)

```python
df["Esito"] = df["Voto"].apply(lambda x: "OK" if x >= 6 else "KO")
```

Su righe:

```python
df["Bonus"] = df.apply(lambda r: r["Voto"] + 1 if r["Assenze"] < 5 else r["Voto"], axis=1)
```

📌 `axis=1` = lavora riga per riga.

---

### replace()

```python
df["Classe"] = df["Classe"].replace("3A", "TerzaA")
```

---

# 7) Aggregazioni e GroupBy avanzato

### Media voto per classe

```python
df.groupby("Classe")["Voto"].mean()
```

---

### Aggregazioni multiple

```python
df.groupby("Classe")["Voto"].agg(["mean", "max", "min", "count"])
```

---

### GroupBy su più colonne

```python
df.groupby(["Classe", "Materia"])["Voto"].mean()
```

---

### transform() vs agg()

* `agg()` produce tabella ridotta
* `transform()` mantiene dimensione originale

Esempio: normalizzare voto rispetto alla classe

```python
df["VotoNorm"] = df["Voto"] - df.groupby("Classe")["Voto"].transform("mean")
```

---

# 8) Pivot e Pivot Table

### pivot()

Richiede valori unici:

```python
df_pivot = df.pivot(index="Studente", columns="Materia", values="Voto")
```

---

### pivot_table() (più potente)

Permette aggregazioni:

```python
df_pt = df.pivot_table(
    values="Voto",
    index="Classe",
    columns="Materia",
    aggfunc="mean"
)
```

Aggiungere totali:

```python
df_pt = df.pivot_table(values="Voto", index="Classe", columns="Materia",
                       aggfunc="mean", margins=True)
```

---

# 9) Join e Merge (equivalente SQL)

### Merge tipo INNER JOIN

```python
pd.merge(df_studenti, df_voti, on="IDStudente", how="inner")
```

Tipi di join:

* `"inner"` = solo match
* `"left"` = tutti i record del primo
* `"right"` = tutti i record del secondo
* `"outer"` = unione totale

---

### Merge su colonne diverse

```python
pd.merge(df1, df2, left_on="CodStud", right_on="ID")
```

---

### Join su index

```python
df1.join(df2, how="left")
```

📌 `join()` è comodo quando gli indici sono già chiavi.

---

# 10) Concatenazione (concat)

Unire righe:

```python
df_tot = pd.concat([df1, df2], axis=0)
```

Unire colonne:

```python
df_tot = pd.concat([df1, df2], axis=1)
```

---

# 11) Ordinamenti e ranking

Ordinamento:

```python
df.sort_values(["Classe", "Voto"], ascending=[True, False])
```

Ranking (posizione in classifica):

```python
df["Rank"] = df.groupby("Classe")["Voto"].rank(ascending=False)
```

---

# 12) Gestione stringhe (str)

Pandas offre metodi vettoriali per stringhe:

```python
df["Nome"].str.upper()
df["Nome"].str.lower()
df["Nome"].str.contains("an")
df["Nome"].str.startswith("Ma")
df["Nome"].str.replace(" ", "_")
```

Split in colonne:

```python
df[["Nome", "Cognome"]] = df["Studente"].str.split(" ", expand=True)
```

---

# 13) Date e Serie Temporali (Datetime)

Conversione:

```python
df["Data"] = pd.to_datetime(df["Data"])
```

Estrarre parti della data:

```python
df["Anno"] = df["Data"].dt.year
df["Mese"] = df["Data"].dt.month
df["Giorno"] = df["Data"].dt.day
df["GiornoSettimana"] = df["Data"].dt.day_name()
```

Filtrare per periodo:

```python
df[df["Data"] >= "2025-01-01"]
```

---

### Resample (raggruppamento temporale)

Impostiamo la data come indice:

```python
df = df.set_index("Data")
```

Media mensile:

```python
df.resample("M")["Voto"].mean()
```

Somma settimanale:

```python
df.resample("W")["Vendite"].sum()
```

📌 Frequenze utili:

* `"D"` giorno
* `"W"` settimana
* `"M"` mese
* `"Y"` anno
* `"H"` ora

---

# 14) Rolling e finestre mobili

Media mobile (rolling mean):

```python
df["MediaMobile"] = df["Vendite"].rolling(window=3).mean()
```

Somma mobile:

```python
df["SommaMobile"] = df["Vendite"].rolling(7).sum()
```

📌 Utile per trend, analisi economiche, sensori, IoT.

---

# 15) Gestione outlier e quantili

Quantili:

```python
df["Voto"].quantile(0.25)
df["Voto"].quantile(0.75)
```

Filtrare valori estremi:

```python
q1 = df["Voto"].quantile(0.25)
q3 = df["Voto"].quantile(0.75)
iqr = q3 - q1

df_filtrato = df[(df["Voto"] >= q1 - 1.5*iqr) & (df["Voto"] <= q3 + 1.5*iqr)]
```

---

# 16) Operazioni vettoriali e performance

📌 Regola d’oro: evitare cicli `for` su DataFrame.

### Esempio sbagliato

```python
for i in range(len(df)):
    df.loc[i, "Voto"] = df.loc[i, "Voto"] + 1
```

### Esempio corretto

```python
df["Voto"] = df["Voto"] + 1
```

---

# 17) Gestione memoria (dataset grandi)

Controllo uso memoria:

```python
df.memory_usage(deep=True)
```

Ottimizzazione:

* convertire stringhe ripetute in `category`
* usare `float32` invece di `float64`
* caricare CSV a blocchi (chunksize)

---

### Lettura CSV a blocchi

```python
for chunk in pd.read_csv("file.csv", chunksize=10000):
    print(chunk["Voto"].mean())
```

---

# 18) Lettura CSV avanzata

Separatore personalizzato:

```python
pd.read_csv("file.csv", sep=";")
```

Solo alcune colonne:

```python
pd.read_csv("file.csv", usecols=["Nome", "Voto"])
```

Parsing date automatico:

```python
pd.read_csv("file.csv", parse_dates=["Data"])
```

Gestione decimali italiani:

```python
pd.read_csv("file.csv", decimal=",")
```

---

# 19) Esportazione avanzata

CSV:

```python
df.to_csv("output.csv", index=False, sep=";")
```

Excel con più fogli:

```python
with pd.ExcelWriter("report.xlsx") as writer:
    df.to_excel(writer, sheet_name="Dati", index=False)
    df.groupby("Classe")["Voto"].mean().to_excel(writer, sheet_name="Medie")
```

---

# 20) Funzioni utili “da professionista”

### nlargest / nsmallest

```python
df.nlargest(5, "Voto")
df.nsmallest(5, "Voto")
```

### Value counts

```python
df["Classe"].value_counts()
```

### Crosstab (tabella di contingenza)

```python
pd.crosstab(df["Classe"], df["Esito"])
```

---

# 21) Esercizio completo avanzato (dataset studenti)

```python
import pandas as pd

df = pd.DataFrame({
    "Studente": ["Anna Rossi", "Luca Bianchi", "Marco Verdi", "Sara Neri", "Anna Rossi"],
    "Classe": ["3A", "3A", "3B", "3B", "3A"],
    "Materia": ["Matematica", "Informatica", "Matematica", "Informatica", "Matematica"],
    "Voto": [8, 7, 9, None, 6],
    "Data": ["2025-01-10", "2025-01-12", "2025-01-15", "2025-02-01", "2025-02-20"]
})

df["Data"] = pd.to_datetime(df["Data"])

# 1) Riempimento NaN con media per materia
df["Voto"] = df.groupby("Materia")["Voto"].transform(lambda x: x.fillna(x.mean()))

# 2) Creazione colonna Esito
df["Esito"] = df["Voto"].apply(lambda x: "Promosso" if x >= 6 else "Bocciato")

# 3) Pivot report: media voti per classe e materia
report = df.pivot_table(values="Voto", index="Classe", columns="Materia", aggfunc="mean")

# 4) Ranking studenti per classe
df["RankClasse"] = df.groupby("Classe")["Voto"].rank(ascending=False)

print(df)
print(report)
```

---

# 22) Checklist mentale (metodo di lavoro consigliato)

Quando ti danno un dataset:

✅ 1. `df.head()` e `df.info()`
✅ 2. controlla `df.isnull().sum()`
✅ 3. pulisci duplicati e NaN
✅ 4. converti tipi (`to_datetime`, `to_numeric`, `astype`)
✅ 5. analizza con `groupby`, `pivot_table`
✅ 6. esporta risultati in Excel/CSV

---

# 23) Funzioni avanzate fondamentali da ricordare

| Funzione                | Utilità                            |
| ----------------------- | ---------------------------------- |
| `set_index()`           | definisce indice                   |
| `reset_index()`         | ripristina indice                  |
| `query()`               | filtri stile SQL                   |
| `astype()`              | conversione tipi                   |
| `to_numeric()`          | conversione sicura numeri          |
| `to_datetime()`         | conversione date                   |
| `drop_duplicates()`     | rimuove duplicati                  |
| `groupby().agg()`       | aggregazioni                       |
| `groupby().transform()` | aggregazioni mantenendo dimensione |
| `pivot_table()`         | report multidimensionale           |
| `merge()`               | join SQL                           |
| `concat()`              | unione tabelle                     |
| `resample()`            | aggregazione temporale             |
| `rolling()`             | medie mobili                       |
| `str.`                  | funzioni su stringhe               |
| `rank()`                | classifica                         |

---

# 24) Errori tipici (da evitare)

❌ usare cicli `for` per elaborare righe
❌ non convertire tipi (`Voto` letto come stringa)
❌ ignorare NaN e duplicati
❌ fare pivot senza controllare chiavi uniche
❌ confondere `agg()` con `transform()`
❌ usare `pivot()` quando serve `pivot_table()`
❌ non sfruttare funzioni vettoriali (es. `str.contains()`)
