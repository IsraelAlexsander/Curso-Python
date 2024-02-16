"""
Fatiamento de strings
0123456789
Olá Mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd de caracteres da string
"""

variavel = 'Olá Mundo'
print(variavel[4])
print(variavel[4:8]) # Vai do indicie 4 e para no indice 7
print(variavel[0:4]) # Vai do indicie 4 e para no indice 7
print(len(variavel))
print(variavel[0:9:2]) ## Inicio, Fim e Passo
print(variavel[::-1]) ## Inverte a String
