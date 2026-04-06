# Modulo `statistics`: L'Analizzatore di Voti

Questo modulo è utilissimo per introdurre i concetti base dell'analisi dati senza usare librerie pesanti come Pandas.

```python
import statistics

def analizza_voti():
    # Lista di voti di una classe
    voti = [24, 27, 30, 18, 22, 24, 26, 30, 24, 29]

    # 1. Calcola la media aritmetica
    # TODO: Usa statistics.mean()
    media = 

    # 2. Trova la moda (il voto più frequente)
    # TODO: Usa statistics.mode()
    voto_comune = 

    # 3. Calcola la mediana
    # TODO: Usa statistics.median()
    mediana = 

    print(f"Media dei voti: {media}")
    print(f"Voto più frequente: {voto_comune}")
    print(f"Valore mediano: {mediana}")

# Sfida Extra: Aggiungi un controllo che verifichi se la media è >= 18 (promosso)

```