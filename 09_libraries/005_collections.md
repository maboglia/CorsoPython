# 5. Modulo `collections`: Strutture dati "Speciali"

Questo è un modulo per un livello intermedio, ottimo per mostrare come scrivere codice più pulito.

* **`Counter`**: Perfetto per esercizi di analisi del testo (es. "conta quante volte appare ogni parola").
* **`defaultdict`**: Risolve il fastidioso errore `KeyError`. Se cerchi una chiave che non esiste, la crea lui con un valore di default (es. 0 o una lista vuota).
* **`namedtuple`**: Per creare oggetti leggeri senza dover scrivere una classe intera.

---

```python
from collections import Counter, defaultdict, namedtuple

# Counter - conteggio elementi
parole = ["mela", "banana", "mela", "arancia", "banana", "mela"]
conteggio = Counter(parole)
print(conteggio)  # Counter({'mela': 3, 'banana': 2, 'arancia': 1})
print(conteggio.most_common(2))  # I 2 elementi più comuni

# defaultdict - dizionario con valore predefinito
gruppi = defaultdict(list)
studenti = [("Mario", "A"), ("Lucia", "B"), ("Paolo", "A"), ("Anna", "B")]

for nome, classe in studenti:
    gruppi[classe].append(nome)

# namedtuple - tupla con nomi
Punto = namedtuple("Punto", ["x", "y"])
p1 = Punto(3, 4)
print(f"Coordinate: x={p1.x}, y={p1.y}")
```
