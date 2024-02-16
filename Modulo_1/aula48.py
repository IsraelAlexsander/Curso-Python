"""
Listas em Python
Tipo list - Mútavel
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - indices e fatiamento
Métodos úteis:
    append -> Adiciona umm item ao final 
    insert -> Adiciona um item no índice escolhido 
    pop -> Remove ao final ou do índice escolhido 
    del -> Apaga um indice 
    clear -> Limpa a Lista 
    extend -> Estende a lista 
    + -> Contatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

## Evitar mover indices da lista caso ela seja muito grande

## Aula 80
""""
lista = list()
lista = []
print(lista, type(lista))
print(bool(lista)) 
lista = [123, True, 'Rael', 1.2, []]
print(lista)
"""

## Aula 81
""""
lista = [10, 20, 30, 40]
lista[2] = 300
print(lista)
print(lista[2])
del lista[2] #deleta 
print(lista)

lista.append(50)
print(lista)

lista.pop() #remove o ultimo valor e retorna 
print(lista)
"""

# Aula 82
"""
lista = [10, 20, 30, 40]
lista.insert(0, 5) # Indice - Valor     //Caso ultrapasse o indice final, ele coloca no final da lista
"""

# Aula 84

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
print(f'Lista c = {lista_c}')

lista_d = lista_a.extend(lista_b) # Mexe diretamente na lista a, e não retorna nada
print(f'Lista a modificada: {lista_a}')
