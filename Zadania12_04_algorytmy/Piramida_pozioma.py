def generate_pyramid(h):
    y = 2 * h - 1
    while y > 0:
        x = 1
        if y >= h:
            while x <= h:
                if x <= 2 * h - y:
                    print("#", end="")
                x += 1
        else:
            while x <= h:
                if x <= y:
                    print("#", end="")
                x += 1
        print("")
        y -= 1

while True:
    try:
        h = int(input("Podaj wysokość: "))
    except ValueError:
        print("Wysokośc musi być liczbą całkowitą")
        continue
    if h <= 0:
        print("Wysokość musi być dodatnia")
        continue
    generate_pyramid(h)
    break