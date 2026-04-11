# 📌 Libreria `math` in Python

La libreria standard **`math`** fornisce funzioni matematiche avanzate:

* radici, potenze, logaritmi
* trigonometria
* arrotondamenti precisi
* costanti matematiche (π, e, inf, NaN)

📌 Modulo incluso in Python → nessuna installazione.

```python
import math
```

---

# 1) 🔹 Costanti principali

```python
import math

print(math.pi)      # π
print(math.e)       # numero di Nepero
print(math.tau)     # 2π
print(math.inf)     # infinito
print(math.nan)     # Not a Number
```

📌 Valori:

* `math.pi ≈ 3.14159`
* `math.e ≈ 2.71828`
* `math.tau = 2*pi`

---

# 2) 🔹 Valore assoluto

⚠️ `abs()` è funzione built-in (non di math):

```python
x = -10
print(abs(x))
```

---

# 3) ✅ Radici e potenze

### Radice quadrata

```python
math.sqrt(25)   # 5.0
```

### Potenza

```python
math.pow(2, 3)  # 8.0
```

⚠️ `math.pow()` restituisce sempre float.

Meglio spesso usare `**`:

```python
2 ** 3   # 8
```

---

# 4) Funzioni di arrotondamento (math)

### Floor (arrotonda per difetto)

```python
math.floor(4.9)   # 4
```

### Ceil (arrotonda per eccesso)

```python
math.ceil(4.1)    # 5
```

### Trunc (taglia la parte decimale)

```python
math.trunc(4.9)   # 4
math.trunc(-4.9)  # -4
```

📌 Differenza importante:

* `floor(-4.9) = -5`
* `trunc(-4.9) = -4`

---

# 5) Arrotondamento standard (`round()`)

⚠️ `round()` è built-in:

```python
round(4.56, 1)   # 4.6
round(4.56)      # 5
```

---

# 6) Fattoriale

```python
math.factorial(5)   # 120
```

⚠️ accetta solo interi >= 0.

---

# 7) Massimo comun divisore e minimo comune multiplo

### MCD (GCD)

```python
math.gcd(12, 18)   # 6
```

### mcm (LCM) (Python 3.9+)

```python
math.lcm(12, 18)   # 36
```

---

# 8) Logaritmi

### Logaritmo naturale (base e)

```python
math.log(10)
```

### Logaritmo in base 10

```python
math.log10(1000)  # 3.0
```

### Logaritmo in base 2

```python
math.log2(8)      # 3.0
```

### Logaritmo con base generica

```python
math.log(8, 2)    # 3.0
```

---

# 9) Esponenziali

```python
math.exp(1)   # e^1
math.exp(2)   # e^2
```

---

# 10) Trigonometria

⚠️ Tutte le funzioni lavorano in **radianti**, NON in gradi.

### Seno, coseno, tangente

```python
math.sin(math.pi/2)   # 1.0
math.cos(0)           # 1.0
math.tan(math.pi/4)   # 1.0
```

---

# 11) Conversione gradi ↔ radianti

### Gradi → Radianti

```python
math.radians(180)  # 3.14159...
```

### Radianti → Gradi

```python
math.degrees(math.pi)  # 180.0
```

---

# 12) Arco seno/coseno/tangente (inverse)

```python
math.asin(1)     # π/2
math.acos(1)     # 0
math.atan(1)     # π/4
```

---

# 13) atan2 (angolo da coordinate)

Molto usato in geometria e grafica.

```python
math.atan2(y, x)
```

Esempio:

```python
math.atan2(1, 1)   # π/4
```

---

# 14) Iperboliche

```python
math.sinh(1)
math.cosh(1)
math.tanh(1)
```

Inverse:

```python
math.asinh(1)
math.acosh(2)
math.atanh(0.5)
```

---

# 15) Funzioni di precisione numerica

### fsum (somma precisa)

```python
math.fsum([0.1, 0.1, 0.1])
```

📌 utile per evitare errori floating point.

---

# 16) Resto divisione (modulo)

### `math.fmod()` (resto float)

```python
math.fmod(7, 2)   # 1.0
```

⚠️ diverso da `%` in alcuni casi con numeri negativi.

---

# 17) Parte frazionaria e intera (`modf`)

```python
math.modf(5.75)
```

📌 Output:

```python
(0.75, 5.0)
```

(prima parte frazionaria, poi parte intera)

---

# 18) Funzioni combinatorie

### Combinazioni (n choose k)

```python
math.comb(5, 2)   # 10
```

### Permutazioni

```python
math.perm(5, 2)   # 20
```

(Python 3.8+)

---

# 19) Distanza Euclidea (`dist`)

```python
math.dist([0, 0], [3, 4])  # 5.0
```

---

# 20) Ipotenusa (`hypot`)

```python
math.hypot(3, 4)   # 5.0
```

Con più dimensioni:

```python
math.hypot(1, 2, 2)  # 3.0
```

---

# 21) Controlli numerici (inf e nan)

```python
math.isfinite(10)         # True
math.isinf(math.inf)      # True
math.isnan(math.nan)      # True
```

---

# 22) Funzioni di confronto robusto: `isclose`

Confrontare float con `==` è rischioso.

```python
math.isclose(0.1 + 0.2, 0.3)
```

📌 spesso True anche se `0.1+0.2` produce `0.30000000000000004`.

---

# 23) Prodotti di iterabili: `prod`

```python
math.prod([2, 3, 4])   # 24
```

---

# 24) Funzioni utili aggiuntive

### Copysign (copia il segno)

```python
math.copysign(5, -1)   # -5.0
```

### Valore massimo/minimo (rispetto a float)

```python
math.fabs(-3.5)  # 3.5
```

⚠️ `fabs` restituisce float (mentre `abs()` può restituire int).

---

# 25) Esempio pratico completo: area e circonferenza cerchio

```python
import math

r = 10

area = math.pi * r**2
circ = 2 * math.pi * r

print("Area:", area)
print("Circonferenza:", circ)
```

---

# 26) Esempio pratico: teorema di Pitagora

```python
import math

a = 3
b = 4

c = math.sqrt(a*a + b*b)
print(c)
```

oppure più elegante:

```python
c = math.hypot(a, b)
```

---

# 27) Differenza tra `math` e `cmath`

* `math` → numeri reali (float, int)
* `cmath` → numeri complessi

Esempio:

```python
import math
math.sqrt(-1)  # ERRORE
```

Con complessi:

```python
import cmath
cmath.sqrt(-1)  # 1j
```

---

# 28) Tabella riepilogo funzioni principali

| Categoria      | Funzioni                        |
| -------------- | ------------------------------- |
| Costanti       | `pi`, `e`, `tau`, `inf`, `nan`  |
| Potenze        | `sqrt`, `pow`                   |
| Arrotondamento | `floor`, `ceil`, `trunc`        |
| Logaritmi      | `log`, `log10`, `log2`          |
| Esponenziali   | `exp`                           |
| Trigonometria  | `sin`, `cos`, `tan`             |
| Inverse trig   | `asin`, `acos`, `atan`, `atan2` |
| Iperboliche    | `sinh`, `cosh`, `tanh`          |
| Combinatoria   | `factorial`, `comb`, `perm`     |
| Geometria      | `hypot`, `dist`                 |
| Precisione     | `fsum`, `isclose`               |
| Controlli      | `isfinite`, `isinf`, `isnan`    |

---

# 29) Errori tipici

### ❌ `math.sqrt(-1)`

👉 errore: `ValueError`
(per complessi usare `cmath`)

### ❌ Trigonometria in gradi

👉 `math.sin(90)` NON è seno 90°
Serve:

```python
math.sin(math.radians(90))
```

---

# 30) Best Practice

✅ per potenze usare `**`
✅ per distanze usare `hypot` o `dist`
✅ per confronti float usare `math.isclose()`
✅ ricordarsi che trigonometria usa radianti

