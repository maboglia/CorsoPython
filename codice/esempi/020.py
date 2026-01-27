# **Promemoria Esempi — Variabili in Python**

# ============================================================
# 1. Cosa sono le variabili
# ============================================================

# Mostrare: una variabile è un contenitore che memorizza un valore.
# Mostrare assegnazione con "="

# Esempi:
# product = "Milk"
# price = 2.99
# stock = 120
# print(product, price, stock)


# ============================================================
# 2. Assegnazione e ri-assegnazione
# ============================================================

# Mostrare che il valore può cambiare nel tempo

# Esempi:
# quantity = 10
# print(quantity)
# quantity = 15   # nuova assegnazione
# print(quantity)


# ============================================================
# 3. Naming delle variabili
# ============================================================

# Mostrare le regole:
# - niente spazi
# - niente caratteri speciali (eccetto "_")
# - non iniziare con un numero
# - case-sensitive (“Name” ≠ “name”)

# Esempi validi:
# product_name = "Bread"
# ProductName = "Eggs"   # diverso da product_name
# _discount = 0.20

# Esempi NON validi (da spiegare, non eseguire):
# 2price = 10
# product-name = "Milk"


# ============================================================
# 4. Assegnazione multipla
# ============================================================

# Mostrare che è possibile assegnare più variabili in una sola riga

# Esempi:
# a, b, c = 1, 2, 3
# print(a, b, c)

# Assegnazione dello stesso valore:
# x = y = z = 0
# print(x, y, z)


# ============================================================
# 5. Tipi dinamici
# ============================================================

# Python è dinamico: una variabile può cambiare tipo

# Esempi:
# item = "Milk"
# print(item, type(item))
# item = 5
# print(item, type(item))


# ============================================================
# 6. Uso di type()
# ============================================================

# Mostrare come verificare il tipo di una variabile

# Esempi:
# price = 3.99
# print(type(price))


# ============================================================
# 7. Variabili e input dell’utente
# ============================================================

# Mostrare che input() restituisce sempre una stringa

# Esempi:
# name = input("Enter product name: ")
# print(name, type(name))

# Conversione esplicita:
# qty = int(input("Enter quantity: "))
# print(qty, type(qty))


# ============================================================
# 8. Variabili temporanee come contatori
# ============================================================

# Mostrare l’uso nelle iterazioni o accumulo valori

# Esempi:
# total = 0
# for price in [2, 3, 5]:
#     total += price
# print(total)


# ============================================================
# 9. Costanti (convenzione)
# ============================================================

# Python non ha costanti reali → si usano variabili tutte maiuscole

# Esempi:
# TAX_RATE = 0.22
# print(TAX_RATE)


# ============================================================
# 10. None come valore “vuoto”
# ============================================================

# Mostrare uso per inizializzare variabili senza valore

# Esempi:
# current_user = None
# print(current_user)
# current_user = "Anna"
# print(current_user)
