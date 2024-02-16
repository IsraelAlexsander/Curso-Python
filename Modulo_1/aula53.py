"""
enumerate - enumera iteráveis (indices)
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# Assim so funciona uma vez
lista_enumerado = enumerate(lista)

for item in lista_enumerado:    
    print(item)

for item in lista_enumerado:    
    print(item)

# Modo mais efetivo
lista2 = ['Alex', 'Bia', 'Claudio']
lista2.append('Daniele')

for indice, valor in enumerate(lista2):    # Nesse caso, ocorre 2 for  
    print(indice, valor)

for item in enumerate(lista2):
    indice, valor = item
    print(indice, valor)

lista_enumerado = enumerate(lista)
lista_enumerado2 = list(enumerate(lista))
print(lista_enumerado)
print(lista_enumerado2)