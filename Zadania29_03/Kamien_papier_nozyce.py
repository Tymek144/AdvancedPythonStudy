import random

while True:
    ruch_uzytkownika = input("Wykonaj ruch: P/K/N/stop")
    if ruch_uzytkownika == "stop":
        print("Zakończyłeś grę")
        break
    else:
        if ruch_uzytkownika == "P":
            ruch_uzytkownika = 1
            print("Ruch uzytkownika: Papier")
        elif ruch_uzytkownika == "K":
            ruch_uzytkownika = 2
            print("Ruch uzytkownika: Kamień")
        elif ruch_uzytkownika == "N":
            ruch_uzytkownika = 3
            print("Ruch uzytkownika: Nożyce")

        ruch_komputera = random.randint(1,3)
        if ruch_komputera == 1: print("Ruch komputera: Papier")
        elif ruch_komputera == 2: print("Ruch komputera: Kamień")
        elif ruch_komputera == 3: print("Ruch komputera: Nożyce")
        wyniki = []

        if ruch_uzytkownika == ruch_komputera:
            print("Remis")
        elif ruch_uzytkownika == 1 and ruch_komputera == 2: print("Wygrał uzytkownik")
        elif ruch_uzytkownika == 2 and ruch_komputera == 3: print("Wygrał komputer")
        elif ruch_uzytkownika == 3 and ruch_komputera == 1: print("Wygrał uzytkownik")
        elif ruch_uzytkownika == 1 and ruch_komputera == 3: print("Wygrał komputer")
        elif ruch_uzytkownika == 2 and ruch_komputera == 1: print("Wygrał komputer")
        elif ruch_uzytkownika == 3 and ruch_komputera == 2: print("Wygrał uzytkownik")