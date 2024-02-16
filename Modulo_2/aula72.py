# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicar(*args):
    total = 1
    for n in args:
        total *= n
    return total

mult = multiplicar(3, 6, 10)
print(mult)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar

def par_impar(x):
    if x % 2 == 0:
        return f'{x} é par'
    return f'{x} é ímpar'
    
    
print(par_impar(4))
print(par_impar(5))

