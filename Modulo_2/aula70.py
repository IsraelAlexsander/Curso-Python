"""
Retorno de valores das funções (return)
"""
def soma(x, y):
    if x > 10:
        return 10,20
    return x + y

soma_1 = soma(1,2)
soma_2 = soma(3,4)
soma_3 = soma(11, 0)

print(soma_1 + soma_2)
print(soma_3)