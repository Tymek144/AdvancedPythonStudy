import math

a = input("Podaj wartość słupka a")
c = input("Podaj wartość słupka c")

if not a.isdigit() or not c.isdigit():
    print("Niepoprawnie wprowadzone wartości")
else:
    a = int(a)
    c = int(c)
    if a <= 0 or a >= 20 or c <= 0 or c >= 20:
        print("Podana wielkość nie jest z przedziału 1-30")
    elif a == c:
        print("Podane wielkości nie mogą być równe")
    else:
        b = math.ceil((a + c) / 2)
        ciag = [a, b, c]
        for k in ciag:
            przesuniecie = max(ciag) - k
            print(" " * (przesuniecie+k+1) + "|")
            print(" " * przesuniecie + "+" + "-" * k + "+")
            print(" " * przesuniecie + "|" + " " * k + "|")
            print(" " * przesuniecie + "+" + "-" * k + "+")
        print(" " * (max(ciag)+1) + "|")

