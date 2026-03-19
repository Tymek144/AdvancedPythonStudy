import random

wynik_uzytkownika = 0
wynik_komputera = 0
while True:
    ruch_uzytkownika = input("Wykonaj ruch: P/K/N/stop")
    if ruch_uzytkownika == "stop":
        print("Zakończyłeś grę")
        print(f"Wyniki końcowe: Ty {wynik_uzytkownika}   |   Komputer: {wynik_komputera}")
        break
    else:
        ruchy = {
            "P": "Papier",
            "K": "Kamień",
            "N": "Nożyce"
        }

        ruch_komputera = random.choice(["K", "P", "N"])
        print(f"Ty: {ruchy[ruch_uzytkownika]}   |    Komputer: {ruchy[ruch_komputera]}")

        if ruch_uzytkownika == ruch_komputera:
            print("Remis")
        elif ruch_uzytkownika == "P" and ruch_komputera == "K" : wynik_uzytkownika += 1
        elif ruch_uzytkownika == "K" and ruch_komputera == "N" : wynik_uzytkownika += 1
        elif ruch_uzytkownika == "N" and ruch_komputera == "P": wynik_uzytkownika += 1
        else: wynik_komputera += 1

        print(f"Aktualne wyniki: Ty {wynik_uzytkownika}   |   Komputer: {wynik_komputera}")