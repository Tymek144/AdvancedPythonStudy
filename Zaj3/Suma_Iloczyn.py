lista = [8,2,7,1]
liczba = int(input("Podaj liczbę "))
para_suma = []
pary_iloczyn = []
for i in range(len(lista)):
    for j in range(i+1, len(lista)):
        if lista[i] + lista[j] == liczba:
            para_suma.append((lista[i], lista[j]))
        elif lista[i] * lista[j] == liczba:
            pary_iloczyn.append((lista[i], lista[j]))

if para_suma:
    print(f"Twoja liczba to suma liczb {para_suma}")
if pary_iloczyn:
    print(f"Twoja liczba to iloczyn liczb {pary_iloczyn}")
if not para_suma and not pary_iloczyn:
    print("Twoja liczba nie jest wynikiem sumy lub iloczynu liczb")