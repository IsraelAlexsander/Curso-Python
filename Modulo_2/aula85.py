lista = []
for x in range(3):
    for y in range(3):
        lista.append((x,y))
#print(lista)

lista_c = [
    (x,y) 
    for x in range(3)
    for y in range(3)
]
print(lista_c)

lista_c2 = [
    [x for y in range(3)]
    for x in range(3)    
]

print(lista_c2)