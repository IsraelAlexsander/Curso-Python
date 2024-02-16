# List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis
import pprint

#print(list(range(10)))
def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

lista = []
for numero in range(10):
    lista.append(numero)

#print(lista)

lista = [numero * 2 for numero in range(10)]
#print(lista)

# Pameamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 10,},
    {'nome': 'p3', 'preco': 30,},
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}   #Map sempre antes do for
    for produto in produtos
    if produto['preco'] >= 20 and produto['preco'] * 1.05 > 10    #Filtro sempre depois do for
]

#print(*novos_produtos, sep='\n')
#p(novos_produtos)

#Filtros

#lista = [n for n in range(10) if n % 2 == 0]
p(novos_produtos)
