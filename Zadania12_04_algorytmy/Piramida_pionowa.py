while True:
    try:
        h = int(input("Podaj wysokość: "))
    except ValueError:
        print("Wysokośc musi być liczbą całkowitą")
        continue
    if h <= 0:
        print("Wysokość musi być dodatnia")
        continue
    y = h-1
    while y >= 0:
        x = 1
        while x < (h*2):
            if x > y and x < (h * 2 - y):
                print("#", end="")
            else:
                print(" ", end="")
            x += 1
        print("")
        y -= 1
    print("Zakończono program")
    break