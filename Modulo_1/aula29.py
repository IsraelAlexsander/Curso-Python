"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input('O número que digitar será dobrado: ')

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)    
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2}')
except:
    print('Isso não é um número')

# Fail Fast
