# **Promemoria Esempi — Tipi di Dato in Python**

# ============================================================
# 1. Numeri (int, float)
# ============================================================

# int: numeri interi
# float: numeri con la virgola (floating point)
# Mostrare: operazioni aritmetiche e type()

# Esempi da mostrare:
# a = 10
# b = 3.5
# print(a, type(a))
# print(b, type(b))
# print(a + b)
# print(a // 3)   # divisione intera


# ============================================================
# 2. Booleani (bool)
# ============================================================

# Mostrare: True / False, confronti, operazioni booleane

# Esempi da mostrare:
# is_available = True
# print(5 > 3)             # True
# print(10 == 5)           # False
# print(True and False)


# ============================================================
# 3. Stringhe (str)
# ============================================================

# Mostrare: dichiarazione, concatenazione, f-string, slicing

# Esempi:
# name = "Milk"
# print(name)
# print(name[0])           # primo carattere
# print(name[1:3])         # slice
# print("Product: " + name)
# price = 2.99
# print(f"{name} costs {price} €")


# ============================================================
# 4. Liste (list)
# ============================================================

# Mostrare: liste miste, accesso agli elementi, append, remove, len()

# Esempi:
# items = ["milk", "eggs", "bread"]
# print(items)
# items.append("cheese")     
# print(items)
# print(items[1])
# items.remove("eggs")
# print(len(items))


# ============================================================
# 5. Tuple (tuple)
# ============================================================

# Mostrare: immutabilità, utilizzo per record fissi

# Esempi:
# product_info = ("Milk", "Dairy", 3.50)
# print(product_info)
# print(product_info[2])
# product_info[0] = "New Milk"   # mostrare errore se eseguito


# ============================================================
# 6. Dizionari (dict)
# ============================================================

# Mostrare: chiave → valore, accesso, aggiornamento, aggiunta

# Esempi:
# inventory = {"milk": 10, "eggs": 30}
# print(inventory["milk"])
# inventory["milk"] = 15     # aggiornamento valore
# inventory["bread"] = 20    # aggiunta nuova chiave
# print(inventory.keys())
# print(inventory.values())
# print(inventory.items())


# ============================================================
# 7. Insiemi (set)
# ============================================================

# Mostrare: unicità degli elementi, uso per rimuovere duplicati

# Esempi:
# categories = {"Dairy", "Bakery", "Dairy", "Produce"}
# print(categories)          # "Dairy" compare una sola volta
# categories.add("Meat")
# categories.remove("Bakery")


# ============================================================
# 8. Conversioni tra tipi (type casting)
# ============================================================

# Mostrare: int(), float(), str(), list(), tuple(), set()

# Esempi:
# a = "10"
# print(int(a))
# b = 3
# print(float(b))
# print(list("Milk"))        # da stringa a lista di caratteri
# print(tuple([1, 2, 3]))
# print(set([1, 1, 2, 2, 3]))


# ============================================================
# 9. NoneType
# ============================================================

# Mostrare: valore "assenza di valore"

# Esempi:
# result = None
# print(result, type(result))
# if result is None:
#     print("No value yet")
