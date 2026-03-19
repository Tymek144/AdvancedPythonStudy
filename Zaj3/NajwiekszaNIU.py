lista = [8,2,7,1]

max = lista[0]
min = lista[0]

for i in lista:
    if i > max:
        max = i
print(max)

for i in lista:
    if i < min:
        min = i
print(min)