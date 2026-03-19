import string

tekst = input("Napisz coś tekstowego: ")
print(tekst.split())

suma_liter = 0
suma_znakow = 0
for znak in tekst:
    if znak.isalpha():
        suma_liter += 1
    elif znak in string.punctuation:
        suma_znakow += 1

suma_spacji = tekst.count(" ")
sum_wyraz = len(tekst.split())
print(f"Twoj tekst składa się z {suma_liter} liter i {suma_znakow} znaków. \
Tekst zawiera {suma_spacji} spacje i {sum_wyraz} wyrazów.")
maly_tekst = tekst.lower()
czestosc = set(maly_tekst)
print(czestosc)
for litera in czestosc:
    if litera.isalpha():
        print(f"W tekście użyto {litera} : {maly_tekst.count(litera)}")