h = 3
y = 2*h - 1
while y > 0:
    while y >= h:
        x=1
        while x <= h:
            if x <= 2*h-y:
                print("#", end="")
            else:
                print(".", end="")
            x += 1
        print("")
        y -= 1
    while y <= h and y >0:
        x = 1
        while x <= h:
            if x <= y:
                print("#", end="")
            else:
                print(".", end="")
            x += 1
        print("")
        y -= 1
