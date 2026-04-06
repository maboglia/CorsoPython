# 14. Modulo `time`: Cronometri e Pause

Essenziale per misurare quanto tempo impiega un codice a girare o per far "aspettare" il programma.

* **Metodi principali:**
* `time.sleep(secondi)`: Blocca l'esecuzione per un tot di tempo.
* `time.time()`: Restituisce il "Timestamp Unix" (secondi passati dal 1° gennaio 1970).

### 💡 Esercizio: "Il Timer di Studio"

```python
import time

def timer_studio(minuti):
    secondi = minuti * 60
    print(f"Timer avviato per {minuti} minuti. Buon lavoro!")
    
    # 1. Aspetta il tempo indicato
    # TODO: Usa time.sleep()
    
    print("⏰ Tempo scaduto! Fai una pausa.")

def misura_performance():
    # 2. Prendi il tempo iniziale
    inizio = time.time()
    
    # Esegui un'operazione (es. un ciclo lungo)
    sum(range(1000000))
    
    # 3. Prendi il tempo finale e calcola la differenza
    fine = time.time()
    print(f"L'operazione ha richiesto {fine - inizio:.4f} secondi.")

# Sfida: Crea un countdown che stampi ogni secondo rimanente (es. 5... 4... 3...)

```
