# Operadores 'in' e 'not in'
# Strings são interáveis
# 0 1 2 3 4 5
# I S R A E L
#-6-5-4-3-2-1

nome = 'Israel'
# print(nome[1])
# print('I' in nome)
# print('Z' in nome)
# print('ael' not in nome)

encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else: 
    print(f'{encontrar} não está em {nome}')