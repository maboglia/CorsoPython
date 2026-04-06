# 15. Modulo `logging`: Addio ai `print` selvaggi

Quando un programma diventa grande, usare `print()` per capire cosa succede non basta più. `logging` permette di scrivere messaggi di errore o di stato in modo ordinato.

* **Livelli di gravità:** DEBUG, INFO, WARNING, ERROR, CRITICAL.

---

## 💡 Esercizio: "Il Diario di Bordo"

```python
import logging

# Configura il logging per scrivere su un file
logging.basicConfig(filename='app.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def divisione_sicura():
    try:
        a = int(input("Numero A: "))
        b = int(input("Numero B: "))
        risultato = a / b
        logging.info(f"Divisione riuscita: {a}/{b} = {risultato}")
    except ZeroDivisionError:
        # TODO: Usa logging.error() per registrare l'errore
        print("Errore: non puoi dividere per zero!")

# Nota: Controlla il file 'app.log' dopo aver eseguito lo script!

```
