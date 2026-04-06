import os

# Informazioni directory
print(f"Directory corrente: {os.getcwd()}")
print(f"Contenuto directory: {os.listdir('.')}")

# Manipolazione percorsi
percorso = os.path.join("cartella", "file.txt")
print(f"Percorso completo: {os.path.abspath(percorso)}")

# Variabili d'ambiente
print(f"Utente: {os.getenv('USER', 'Sconosciuto')}")