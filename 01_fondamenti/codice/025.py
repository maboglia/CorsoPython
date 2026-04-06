# ============================================================
# 1. Cosa significa indicizzare una stringa
# ============================================================

# Mostrare che le stringhe sono sequenze di caratteri e ogni carattere
# ha una posizione (indice), a partire da 0.

# Esempio:
# word = "Banana"
# print(word[0])   # primo carattere
# print(word[1])   # secondo carattere


# ============================================================
# 2. Indici positivi
# ============================================================

# Spiegare che gli indici positivi partono da sinistra → 0, 1, 2...

# Esempio:
# fruit = "Apple"
# print(fruit[3])  # 'l'


# ============================================================
# 3. Indici negativi
# ============================================================

# Mostrare che gli indici negativi partono dalla fine → -1, -2...

# Esempio:
# fruit = "Orange"
# print(fruit[-1])   # ultimo carattere
# print(fruit[-2])   # penultimo carattere


# ============================================================
# 4. Accesso a caratteri tramite variabile indice
# ============================================================

# Mostrare che l'indice può essere una variabile

# Esempio:
# text = "Python"
# i = 2
# print(text[i])   # stampa 't'


# ============================================================
# 5. Range di indicizzazione non valido
# ============================================================

# Mostrare IndexError quando l’indice è fuori range

# Da mostrare, non da eseguire live:
# word = "Hi"
# print(word[5])   # IndexError


# ============================================================
# 6. Slicing di stringhe (cenno introduttivo)
# ============================================================

# Introduzione al concetto:
# stringa[inizio:fine] → estrae una porzione

# Esempio:
# name = "Carrot"
# print(name[1:4])   # 'arr'


# ============================================================
# 7. Utilizzo della funzione len()
# ============================================================

# Mostrare che len() restituisce il numero di caratteri della stringa

# Esempio:
# greeting = "Hello"
# print(len(greeting))    # 5


# ============================================================
# 8. Usare len() insieme all’indicizzazione
# ============================================================

# Trovare l’ultimo carattere con len() - 1

# Esempio:
# city = "Rome"
# last_index = len(city) - 1
# print(city[last_index])


# ============================================================
# 9. Scorrere una stringa con un ciclo for e indicizzazione
# ============================================================

# Mostrare come accedere ogni carattere con l’indice

# Esempio:
# word = "Bread"
# for i in range(len(word)):
#     print(i, word[i])


# ============================================================
# 10. Differenza tra len() e ultimo indice
# ============================================================

# Ricordare che:
# len(stringa) → numero elementi
# ultimo indice → len(stringa) - 1

# Esempio dimostrativo:
# s = "Milk"
# print(len(s))     # 4
# print(s[3])       # 'k'
