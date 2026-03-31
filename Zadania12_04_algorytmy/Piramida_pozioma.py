h = 3
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
