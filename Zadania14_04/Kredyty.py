a = True
while a == True:
    K = input("Podaj kwotę kredytu")
    if not K.isdigit():
        print("Kwota musi być liczbą całkowitą")
    else:
        K = int(K)
        liczba_lat = input("Podaj liczbę lat")
        if not liczba_lat.isdigit():
            print("Liczba lat musi być liczbą całkowitą")
        else:
            liczba_lat = int(liczba_lat)
            n = liczba_lat * 12
            i = input("Podaj roczne oprocentowanie: ").replace(",", ".")
            try:
                i = float(i)
            except ValueError:
                print("Niepoprawne oprocentowanie, podaj liczbę dziesiętną")
            else:
                i = float(i)
                r = i/12
                typ_raty = input("Podaj typ raty: s/m")
                if typ_raty != "s" and typ_raty != "m":
                    print("Niepoprawny typ raty")
                else:
                    a = False

if typ_raty == "s":
    rata = K * r * (1 + r)**n / ((1 + r)**n - 1)
    pozostaly_kapital = K
    print(f"Kredyt na {K} zł na {liczba_lat} lat(a) z rocznym oprocentowaniem {i*100}% z {typ_raty}tałymi ratami \n"
          f"Łącznie do spłaty: {rata*n:.2f} \n"
          f"Koszt kredytu: {rata*n-K:.2f}")
    for k in range(1, n + 1):
        odsetki = pozostaly_kapital *r
        kapital = rata - odsetki
        pozostaly_kapital -= kapital
        print(f"Rata za {k} miesiąc: {rata:.2f} zł w tym "
              f"część kapitałowa: {kapital:.2f} i odsetki: {odsetki:.2f}; "
              f"zostało do spłaty: {pozostaly_kapital:.2f}")
elif typ_raty == "m":
    kwota_kredytu = 0
    pozostaly_kapital = K
    print(f"Kredyt na {K} zł na {liczba_lat} lat(a) z rocznym oprocentowaniem {i * 100}% z {typ_raty}alejącymi ratami")
    for k in range(1, n+1):
        rata_k = K/n * (1 + r*(n+1-k))
        odsetki = pozostaly_kapital * r
        kapital = rata_k - odsetki
        pozostaly_kapital -= kapital
        kwota_kredytu += rata_k
        print(f"Rata za {k} miesiąc: {rata_k:.2f} zł w tym "
              f"część kapitałowa: {kapital:.2f} i odsetki: {odsetki:.2f}; "
              f"zostało do spłaty: {pozostaly_kapital:.2f}")
    print(f"Łącznie do spłaty: {kwota_kredytu:.2f} \n"
          f"Koszt kredytu: {kwota_kredytu - K:.2f}")
else:
    print(f"Niepoprawny typ raty")