# Esempi progressivi Pandas (da base → avanzato)

Di seguito una sequenza di esempi pensata come **percorso didattico**: ogni step introduce concetti nuovi.

---

# LIVELLO 1 — BASE (creazione e selezione)

## 1) Creare un DataFrame

```python
import pandas as pd

df = pd.DataFrame({
    "Nome": ["Anna", "Luca", "Marco"],
    "Eta": [20, 22, 19],
    "Citta": ["Roma", "Milano", "Torino"]
})

print(df)
```

---

## 2) Prime informazioni sul dataset

```python
print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
```

---

## 3) Selezione colonne e righe

```python
print(df["Nome"])         # colonna singola
print(df[["Nome", "Eta"]]) # più colonne

print(df.iloc[0])         # prima riga
print(df.iloc[0:2])       # prime due righe
```

---

# LIVELLO 2 — FILTRI E ORDINAMENTO

## 4) Filtrare righe con condizioni

```python
df_over20 = df[df["Eta"] > 20]
print(df_over20)
```

Condizioni multiple:

```python
df_filtrato = df[(df["Eta"] > 18) & (df["Citta"] == "Roma")]
print(df_filtrato)
```

---

## 5) Ordinare i dati

```python
df_ordinato = df.sort_values("Eta", ascending=False)
print(df_ordinato)
```

---

# LIVELLO 3 — MODIFICA DATI E NUOVE COLONNE

## 6) Creare una colonna calcolata

```python
df["AnnoNascita"] = 2025 - df["Eta"]
print(df)
```

---

## 7) Modificare valori

```python
df["Eta"] = df["Eta"] + 1
print(df)
```

---

## 8) Colonna con logica (apply)

```python
df["Maggiorenne"] = df["Eta"].apply(lambda x: "SI" if x >= 18 else "NO")
print(df)
```

---

# LIVELLO 4 — GESTIONE NaN E CLEANING

## 9) Dataset con valori mancanti

```python
df = pd.DataFrame({
    "Nome": ["Anna", "Luca", "Marco", "Sara"],
    "Voto": [8, None, 7, None]
})

print(df)
print(df.isnull().sum())
```

---

## 10) Riempire NaN con valore fisso o media

```python
df["Voto"] = df["Voto"].fillna(0)
print(df)
```

Oppure con media:

```python
df["Voto"] = df["Voto"].fillna(df["Voto"].mean())
print(df)
```

---

# LIVELLO 5 — GROUPBY E STATISTICHE

## 11) Dataset voti per classe

```python
df = pd.DataFrame({
    "Studente": ["Anna", "Luca", "Marco", "Sara", "Paolo"],
    "Classe": ["3A", "3A", "3B", "3B", "3A"],
    "Voto": [8, 6, 9, 7, 5]
})

print(df)
```

---

## 12) Media voti per classe

```python
medie = df.groupby("Classe")["Voto"].mean()
print(medie)
```

---

## 13) Più statistiche insieme

```python
stats = df.groupby("Classe")["Voto"].agg(["mean", "max", "min", "count"])
print(stats)
```

---

# LIVELLO 6 — PIVOT TABLE (report multidimensionale)

## 14) Voti per materia

```python
df = pd.DataFrame({
    "Studente": ["Anna", "Anna", "Luca", "Luca", "Marco", "Marco"],
    "Classe": ["3A", "3A", "3A", "3A", "3B", "3B"],
    "Materia": ["Matematica", "Informatica", "Matematica", "Informatica", "Matematica", "Informatica"],
    "Voto": [8, 9, 6, 7, 9, 8]
})

print(df)
```

---

## 15) Report: media voti per classe e materia

```python
report = df.pivot_table(
    values="Voto",
    index="Classe",
    columns="Materia",
    aggfunc="mean"
)

print(report)
```

---

# LIVELLO 7 — MERGE (JOIN stile SQL)

## 16) Unire studenti e voti

```python
studenti = pd.DataFrame({
    "ID": [1, 2, 3],
    "Nome": ["Anna", "Luca", "Marco"]
})

voti = pd.DataFrame({
    "ID": [1, 1, 2, 3],
    "Materia": ["Matematica", "Informatica", "Matematica", "Matematica"],
    "Voto": [8, 9, 6, 9]
})

df_merge = pd.merge(studenti, voti, on="ID")
print(df_merge)
```

---

# LIVELLO 8 — STRINGHE (str)

## 17) Pulizia e trasformazione testi

```python
df = pd.DataFrame({
    "Studente": ["Anna Rossi", "Luca  Bianchi", " Marco Verdi "]
})

df["Studente"] = df["Studente"].str.strip()
df["Studente"] = df["Studente"].str.replace("  ", " ")

print(df)
```

Separare nome e cognome:

```python
df[["Nome", "Cognome"]] = df["Studente"].str.split(" ", expand=True)
print(df)
```

---

# LIVELLO 9 — DATE e SERIE TEMPORALI

## 18) Gestire date con datetime

```python
df = pd.DataFrame({
    "Data": ["2025-01-10", "2025-01-15", "2025-02-01"],
    "Vendite": [100, 150, 120]
})

df["Data"] = pd.to_datetime(df["Data"])
print(df)
```

Estrarre mese:

```python
df["Mese"] = df["Data"].dt.month
print(df)
```

---

## 19) Resample (raggruppamento mensile)

```python
df = df.set_index("Data")
mensile = df.resample("M")["Vendite"].sum()
print(mensile)
```

---

# LIVELLO 10 — ROLLING (finestre mobili)

## 20) Media mobile su vendite

```python
df["MediaMobile2"] = df["Vendite"].rolling(window=2).mean()
print(df)
```

---

# LIVELLO 11 — TRANSFORM (avanzato e fondamentale)

## 21) Riempire NaN con media per gruppo

```python
df = pd.DataFrame({
    "Classe": ["3A", "3A", "3B", "3B"],
    "Voto": [8, None, 7, None]
})

df["Voto"] = df.groupby("Classe")["Voto"].transform(lambda x: x.fillna(x.mean()))
print(df)
```

📌 Questo è un esempio tipico “da data analyst”.

---

# LIVELLO 12 — RANKING e classifiche

## 22) Classifica studenti per classe

```python
df = pd.DataFrame({
    "Studente": ["Anna", "Luca", "Sara", "Marco"],
    "Classe": ["3A", "3A", "3B", "3B"],
    "Voto": [8, 6, 9, 7]
})

df["Rank"] = df.groupby("Classe")["Voto"].rank(ascending=False)
print(df)
```

---

# LIVELLO 13 — DATA CLEANING COMPLETO (workflow realistico)

## 23) Caso reale: dati sporchi + duplicati + NaN

```python
df = pd.DataFrame({
    "Studente": [" Anna Rossi", "Luca Bianchi", "Luca Bianchi", "Sara Neri"],
    "Classe": ["3A", "3A", "3A", "3B"],
    "Voto": ["8", None, "7", "6"]
})

# Pulizia stringhe
df["Studente"] = df["Studente"].str.strip()

# Conversione voto a numerico
df["Voto"] = pd.to_numeric(df["Voto"], errors="coerce")

# Eliminazione duplicati
df = df.drop_duplicates()

# Riempimento NaN con media classe
df["Voto"] = df.groupby("Classe")["Voto"].transform(lambda x: x.fillna(x.mean()))

print(df)
```

---

# LIVELLO 14 — MINI-PROGETTO AVANZATO (report finale)

## 24) Report completo (groupby + pivot + export excel)

```python
import pandas as pd

df = pd.DataFrame({
    "Studente": ["Anna", "Anna", "Luca", "Luca", "Marco", "Sara"],
    "Classe": ["3A", "3A", "3A", "3A", "3B", "3B"],
    "Materia": ["Matematica", "Informatica", "Matematica", "Informatica", "Matematica", "Informatica"],
    "Voto": [8, 9, 6, 7, 9, 8]
})

# Media voto per studente
media_studente = df.groupby("Studente")["Voto"].mean()

# Report pivot: classe vs materia
report = df.pivot_table(values="Voto", index="Classe", columns="Materia", aggfunc="mean")

# Export Excel
with pd.ExcelWriter("report.xlsx") as writer:
    df.to_excel(writer, sheet_name="Dati", index=False)
    media_studente.to_excel(writer, sheet_name="MediaStudente")
    report.to_excel(writer, sheet_name="ReportClassi")

print(media_studente)
print(report)
```

---

# Riassunto livelli

* **Base**: DataFrame, head, iloc, colonne
* **Intermedio**: filtri, sort, nuove colonne, apply
* **Pulizia**: NaN, duplicati, conversioni tipo
* **Analisi**: groupby, agg
* **Report**: pivot_table
* **Relazioni**: merge
* **Time series**: datetime, resample, rolling
* **Avanzato**: transform, ranking, export Excel multi-foglio

