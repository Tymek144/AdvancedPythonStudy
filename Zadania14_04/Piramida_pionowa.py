h= input("Podaj wysokość: ")
if not h.isdigit():
    print("Dla wprowadzonej wartości niemożliwe jest wygenerowanie piramidy.")
else:
    h = int(h)
    y = h-1
    while y >= 0:
        x = 1
        while x < (h*2):
            if x > y and x < (h * 2 - y):
                print("#", end="")
            else:
                print(" ", end="")
            x += 1
        else:
            print("\n")
        y -= 1
    else:
        print("Zakończono program")
