NIU = "88335"
lista = []
for znak in NIU:
    if int(znak) not in lista:
        lista.append(int(znak))
print(lista)

def bubble_ascending(lista):
    for j in range(len(lista)-1):
        for i in range(len(lista)-1-j):
            if lista[i] < lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    return lista

def bubble_descending(lista):
    for j in range(len(lista)-1):
        for i in range (len(lista)-1-j):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    return lista

print(bubble_ascending(lista))
print(bubble_descending(lista))