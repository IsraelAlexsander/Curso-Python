# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]
# lista = [3, 5,54,664,6,543,42,43]
# lista.sort()

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

def ordena(item):   
    return item['nome']

def exibir(lista):
    for item in lista:
        print(item)

#lista.sort(key=ordena)
lista.sort(key=lambda item: item['nome'])
l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(lista)
print()
exibir(l1)
print()
exibir(l2)