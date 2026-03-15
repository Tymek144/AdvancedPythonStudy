import string

tekst = input("Podaj tekst: ")
print(tekst.split())

suma_liter = 0
suma_znakow = 0
for znak in tekst:
    if znak.isalpha():
        suma_liter += 1
    elif znak in string.punctuation:
        suma_znakow += 1

suma_spacji = tekst.count(" ")
suma_wyrazow = len(tekst.split())

print(f"Twoj tekst składa się z {suma_liter} liter i {suma_znakow} znaków interpunkcyjnych. \
Tekst zawiera {suma_spacji} spacje/i oraz {suma_wyrazow} wyrazy/ów.")

maly_tekst = tekst.lower()
czestotliwosc = set(maly_tekst)
print(czestotliwosc)
for litera in czestotliwosc:
    if litera.isalpha():
        print(f"W tekście użyto {litera} : {maly_tekst.count(litera)}")