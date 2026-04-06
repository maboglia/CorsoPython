""" Funzioni in Python """

# ============================================================
# 1. Definire una funzione con def
# ============================================================
# Sintassi: def nome_funzione(parametri):
# Esempio:
# def saluta(nome):
#     print(f"Ciao, {nome}!")
# saluta("Alice")  # Output: Ciao, Alice!

# ============================================================
# 2. Restituire un valore con return
# ============================================================
# Esempio:
# def somma(a, b):
#     return a + b
# risultato = somma(5, 3)
# print(risultato)  # Output: 8

# ============================================================
# 3. Funzioni con parametri opzionali
# ============================================================
# Esempio:
# def saluta(nome, saluto="Ciao"):
#     print(f"{saluto}, {nome}!")
# saluta("Bob")  # Output: Ciao, Bob!
# saluta("Bob", "Salve")  # Output: Salve, Bob!

# ============================================================
# 4. Funzioni con un numero variabile di argomenti
# ============================================================
# Esempio:
# def somma(*numeri):
#     return sum(numeri)
# print(somma(1, 2, 3))  # Output: 6
# print(somma(4, 5))     # Output: 9

# ============================================================
# 5. Funzioni lambda (funzioni anonime)
# ============================================================
# Esempio:
# quadrato = lambda x: x ** 2
# print(quadrato(5))  # Output: 25

