"""
args - Argumentos não nomeados
* - *arges (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento

# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

# def soma(x,y):
#     return x + y

def soma(*args):
    total = 0
    for numero in args:
        total += numero        
    return total

soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)
print(soma_4_5_6)

outra_soma_1 = soma(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(outra_soma_1)

numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9
#outra_soma_2 = soma(numeros)   Não funciona, pois esta empacotada
outra_soma_2 = soma(*numeros)   #Desempacota
print(outra_soma_2) 

#print(sum(1, 2, 3, 4, 5, 6, 7, 8, 9)) Não funciona porque não esta empacotado
print(sum(numeros)) #Funciona por estar empacotado