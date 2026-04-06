# Python Slot Machine Game

import random

def spin_row():
    symbols = ['🍒', '🍋', '🍊', '🍉', '⭐']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("\n-----------------")
    print(' | '.join(row))
    print("-----------------")
    
def check_win(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return 2 * bet
        elif row[0] == '🍋':
            return 3 * bet
        elif row[0] == '🍊':
            return 5 * bet 
        elif row[0] == '🍉':
            return 10 * bet
        elif row[0] == '⭐':
            return 20 * bet

    return 0

def main():

    balance = 100

    print("Python Slot Machine!")
    print(f"Il tuo saldo iniziale è: {balance}")
    print("".join(['🍒', '🍋', '🍊', '🍉', '⭐']))
    # input("Press Enter to spin...")
    

    
    
    while balance > 0:
        bet = input("Quanto vuoi puntare?: ")
        if not bet.isdigit():
            print("Inserisci un numero valido.")
            continue
        
        bet = int(bet)
        
        if int(bet) <= 0:
            print("La puntata deve essere un numero positivo.")
            continue
        
        if bet > balance:
            print("Non hai abbastanza soldi per quella puntata.")
            continue
        
        balance -= bet
        
        row = spin_row()
        print("\nSpinning...")
        print_row(row)
        payout = check_win(row, bet)
        
        balance += payout
        
        if payout > 0:
            print(f"Hai vinto {payout}!")
        else:
            print("Non hai vinto questa volta.")
            
        print(f"Il tuo saldo attuale è: {balance}")

        print("\nVuoi uscire? (s/n)")
        play_again = input().lower()
        if play_again == 's':
            break
        
print("Grazie per aver giocato!")

if __name__ == "__main__":
    main()