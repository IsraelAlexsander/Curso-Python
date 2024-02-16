"""
Faça uma lista de comprar com listas
O usuário dever ter a possibilidade de inserir, apagar e listar valores da sua lista
Não permita que o pregrama quebre com erros de índices inexistentes na lista.
"""

import os

lista = []

while True:    
    os.system('cls')        
    opcao = input('Selecione uma opção\n[I] Inserir\t[A] Apagar\t[L] Listar: ').lower()

    if opcao == 'i':      
        os.system('cls')        
        lista.append(input('Digite o nome do item: '))

    elif opcao == 'a':
        os.system('cls')        
        indice_str = input('Digite o índice que deseja apagar: ')   
        try:
            indice_int = int(indice_str)
            del lista[indice_int]            
        except ValueError:
            print('Por favor digite número int.')
            continue
        except IndexError:
            print('Valor fora do índice')
            continue

    elif opcao == 'l':
        os.system('cls')        
        if len(lista) == False:
            print('A Lista está vazia')
        else:
            for item in enumerate(lista):
                indice, nome = item
                print(indice, nome)

    else:
        os.system('cls')
        print('Opção invalida...')
        continue
