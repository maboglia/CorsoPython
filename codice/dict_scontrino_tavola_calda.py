""" scontrino tavola calda """

menu = {
    "pasta al pomodoro": 5.0,
    "pasta al pesto": 6.0,
    "pasta alla carbonara": 7.0,
    "birra": 3.0,
    "acqua": 1.0,
    "coca-cola": 2.5,
    "caffè": 1.5
}


scontrino = []
totale = 0.0


print("Benvenuto alla tavola calda!")
print("Ecco il nostro menu:")
for key, value in menu.items():
    print(f"{key:20}: {value:.2f} €")

while True:
    scelta = input(f"Cosa vuoi ordinare? (q per terminare) ")
    if scelta.lower() == "q":
        break
    else:
        if scelta in menu:
            prezzo = menu[scelta]
            scontrino.append((scelta, prezzo))
            totale += prezzo
            print(f"Hai ordinato {scelta} per {prezzo:.2f} €")
        else:
            print("Mi dispiace, non abbiamo questo prodotto.")
print("\nIl tuo scontrino:")
for item, price in scontrino:
    print(f"{item:20}: {price:.2f} €")
print(f"Totale: {totale:.2f} €")
