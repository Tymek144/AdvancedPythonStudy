from asyncio.windows_events import NULL

lista = [8, 3, 5, 6]

liczba = int(input("Podaj liczbę "))
pary_sum = []
pary_iloczyn = []

for i in range(len(lista)):
    for j in range(i+1, len(lista)):
        if lista[i] + lista[j] == liczba:
            pary_sum.append((lista[i], lista[j]))
        elif lista[i] * lista[j] == liczba:
            pary_iloczyn.append((lista[i], lista[j]))

if pary_sum: print(f"Twoja liczba to suma dwóch liczb {pary_sum}")
if pary_iloczyn: print(f"Twoja liczba to iloczyn dwóch liczb {pary_iloczyn}")
if not pary_sum and not pary_iloczyn: print("Twoja liczba nie jest wynikiem ani sumy, ani iloczynu żadnej par liczb")