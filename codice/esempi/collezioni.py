""" Gestire le collezioni di dati in Python: stringhe, liste, tuple, set e dizionari """

# Liste
# Le liste sono collezioni ordinate e mutabili di elementi
# Esempio:
# fruits = ["apple", "banana", "cherry"]
# print(fruits[0])          # 'apple'
# fruits.append("orange")   # aggiunge un elemento alla fine
# print(fruits)            # ['apple', 'banana', 'cherry', 'orange']

# Tuple
# Le tuple sono collezioni ordinate e immutabili di elementi
# Esempio:
# coordinates = (10.0, 20.0)
# print(coordinates[0])    # 10.0
# coordinates[0] = 15.0   # questo causerà un errore perché le tuple sono immutabili

# Set
# I set sono collezioni non ordinate di elementi unici
# Esempio:
# unique_numbers = {1, 2, 3, 4}
# print(unique_numbers)    # {1, 2, 3, 4}
# unique_numbers.add(2)   # non aggiunge perché 2 è già presente
# print(unique_numbers)    # {1, 2, 3, 4}
# unique_numbers.add(5)   # aggiunge 5 al set
# print(unique_numbers)    # {1, 2, 3, 4, 5}

# Dizionari
# I dizionari sono collezioni di coppie chiave-valore
# Esempio:
# student = {"name": "Alice", "age": 20, "major": "Computer Science"}
# print(student["name"])   # 'Alice'
# student["age"] = 21     # aggiorna il valore associato alla chiave "age"
# print(student)          # {'name': 'Alice', 'age': 21, 'major': 'Computer Science'}
