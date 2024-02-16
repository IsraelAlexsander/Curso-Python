"""
Faça um programa que peça ao usuário para digitar um número  inteiro, informe se este número é par ou ímpar
Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""

num = input('Digite um número inteiro: ')

try:
    num_int = int(num)

    if num_int % 2 == 0:
        print('Este número é par')
    else:
        print('Este número é ímpar')

except:
    print('Não é um número inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, basenaodo-se ao horário descrito, exiba a saudação apropriada
"""

horario = input('Digite a hora: ')

try: 
    horario_int = int(horario)

    if (horario_int > 0) and (horario_int < 12):
        print('Bom Dia')
    elif horario_int < 18:
        print('Boa Tarde')
    else:
        print('Boa Noite')
        
except:
    print('Valor invalido')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos, escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande"
"""

nome = input('Digite o seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome <= 4:
    print('Seu nome é curto')
elif tamanho_nome <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é grande')