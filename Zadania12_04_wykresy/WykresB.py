a = input("Podaj a: ")
b = input("Podaj b: ")

if not a.isdigit() or not b.isdigit():
    print("Niepoprawnie wprowadzone wartości")
else:
    a = int(a)
    b = int(b)
    if a < 0 or a >= 9 or b < 0 or b >= 9:
        print("Podana wielkość nie jest z przedziału 0-8")
    elif a == b:
        print("Podane wielkości nie mogą być równe")
    else:
        c = abs(a - b)
        ciag = [a, b, c]
        maks = max(ciag)
        print("--+-+--+-+--+-+--")
        for poziom in range(1, maks + 1):
            for k in ciag:
                if poziom < k:
                    print(" | | ", end="")
                elif poziom == k and k != 0:
                    print(" +-+ ", end="")
                else:
                    print("     ", end="")
            print()