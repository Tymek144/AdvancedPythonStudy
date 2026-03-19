lista = [8,3,5]

max = lista[0]
min = lista[0]

for i in lista:
    if i > max:
        max = i
print(f"Największa: {max}")

for i in lista:
    if i < min:
        min = i
print(f"Najmniejsza: {min}")
