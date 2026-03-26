NIU = [8,2,7,1]

def sort_bubble_ascending(lista):
    for n in range(len(lista)-1):
        for x in range(len(lista)-1-n):
            if lista[x] > lista[x+1]:
                lista[x], lista[x+1] = lista[x+1], lista[x]
    return lista

def sort_bubble_descending(lista):
    for n in range(len(lista)-1):
        for x in range(len(lista)-1-n):
            if lista[x+1] > lista[x]:
                lista[x+1], lista[x] = lista[x], lista[x+1]
    return lista


print(sort_bubble_ascending(NIU))
print(sort_bubble_descending(NIU))
