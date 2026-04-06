# Modulo `math` & `random`: Il Generatore di Cerchi

In questo esercizio uniamo la geometria alla casualità. L'obiettivo è generare raggi casuali e calcolare le aree.

```python
import math
import random

def geometria_casuale():
    # 1. Genera un raggio casuale tra 1 e 10 (float)
    # TODO: Usa random.uniform(1, 10)
    raggio = 

    # 2. Calcola l'area del cerchio (Area = pi * r^2)
    # TODO: Usa math.pi e math.pow() oppure l'operatore **
    area = 

    # 3. Arrotonda il risultato per eccesso
    # TODO: Usa math.ceil()
    area_arrotondata = 

    print(f"Raggio generato: {raggio:.2f}")
    print(f"L'area del cerchio è: {area:.2f}")
    print(f"Area arrotondata per eccesso: {area_arrotondata}")

# Sfida Extra: Genera 5 cerchi e trova quello con l'area maggiore usando max()

```

### 3.3 Modulo `random` - Numeri Casuali

```python
import random

# Numeri casuali
print(random.randint(1, 100))      # Intero tra 1 e 100
print(random.random())             # Float tra 0 e 1
print(random.uniform(1.5, 10.5))   # Float tra 1.5 e 10.5

# Scelte casuali
colori = ["rosso", "blu", "verde", "giallo"]
print(random.choice(colori))       # Un elemento casuale
print(random.sample(colori, 2))    # Due elementi casuali senza ripetizione

# Mescolamento
carte = ["A", "K", "Q", "J"]
random.shuffle(carte)
print(carte)
```
