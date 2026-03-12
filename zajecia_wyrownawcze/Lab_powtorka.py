tekst = "kot   "
print(tekst.rstrip()) #usuwa białe znaki na końcu
x,y,z = 1,2,3

przedmioty = ['programowanie', 'makro', 'stata']
print(przedmioty[1].upper())

przedmioty.insert(1,'ekonomia')
print(przedmioty)

del przedmioty[1]
przedmioty.remove('stata')
przedmioty.pop(0)
