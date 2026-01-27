# ============================================================
# 1. Che cos’è lo slicing
# ============================================================

# Mostrare che lo slicing permette di estrarre una porzione di stringa:
# stringa[inizio:fine] → dal carattere "inizio" fino a (fine-1)

# Esempio:
# word = "Strawberry"
# print(word[0:5])   # 'Straw'


# ============================================================
# 2. Slicing senza indice di inizio
# ============================================================

# Se omettiamo l’indice iniziale, Python parte automaticamente da 0

# Esempio:
# fruit = "Banana"
# print(fruit[:3])    # 'Ban'


# ============================================================
# 3. Slicing senza indice di fine
# ============================================================

# Se omettiamo l’indice finale, Python continua fino alla fine

# Esempio:
# name = "Carrot"
# print(name[2:])     # 'rrot'


# ============================================================
# 4. Slicing completo
# ============================================================

# Permette di fare una copia della stringa

# Esempio:
# text = "Python"
# print(text[:])      # 'Python'


# ============================================================
# 5. Slicing con step
# ============================================================

# Sintassi: stringa[inizio:fine:step]
# Step controlla di quanto avanza l’indice ogni volta

# Esempio:
# code = "ABCDEFG"
# print(code[0:7:2])   # 'ACEG'


# ============================================================
# 6. Step negativo per invertire una stringa
# ============================================================

# Usare step -1 per invertire la stringa rapidamente

# Esempio:
# word = "Pizza"
# print(word[::-1])   # 'azziP'


# ============================================================
# 7. Slicing con indici negativi
# ============================================================

# Gli indici negativi permettono di partire dalla fine

# Esempio:
# item = "Tomato"
# print(item[-4:-1])   # 'mat'


# ============================================================
# 8. Usare len() insieme allo slicing
# ============================================================

# Estrarre le ultime N lettere usando len()

# Esempio:
# product = "Watermelon"
# last3 = product[len(product)-3:]
# print(last3)          # 'lon'


# ============================================================
# 9. Slicing errati che NON danno errori
# ============================================================

# Slicing fuori dai limiti restituisce una stringa vuota, NON un errore

# Esempio:
# s = "Hi"
# print(s[5:10])    # ''   (stringa vuota)


# ============================================================
# 10. Concatenazione con l'operatore +
# ============================================================

# Unire due o più stringhe

# Esempio:
# first = "Hello"
# second = "World"
# print(first + " " + second)   # 'Hello World'


# ============================================================
# 11. Concatenazione con variabili
# ============================================================

# Esempio:
# name = "Anna"
# greeting = "Hi, " + name
# print(greeting)


# ============================================================
# 12. Concatenare usando f-string (metodo migliore)
# ============================================================

# Esempio:
# user = "Sam"
# print(f"Welcome, {user}!")


# ============================================================
# 13. Usare la concatenazione insieme allo slicing
# ============================================================

# Esempio:
# item = "Chocolate"
# short = item[:5] + "..."
# print(short)     # 'Choco...'


# ============================================================
# 14. Ripetizione di stringhe con l’operatore *
# ============================================================

# Non è concatenazione, ma è utile mostrarlo qui

# Esempio:
# print("na" * 3)   # 'nanana'


# ============================================================
# 15. Unire parti di più stringhe per formare parole nuove
# ============================================================

# Esempio divertente:
# a = "spaghetti"
# b = "gelato"
# new_word = a[:4] + b[-3:]
# print(new_word)   # 'spato'
