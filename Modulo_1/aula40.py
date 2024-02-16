"""Calculadora com while"""

while True:

    try:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
    except:
        print('Um ou ambos os valores estão incorretos')
        continue
    
    operador = input('Digite o operador\n[+] Adição\n[-] Subtração\n[*] Multiplicação\n[/] Divisão\nOpção: ')

    if (operador not in '+-*/') or (len(operador) > 1):
        print('Operador inadequado')
        continue

    if operador == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operador == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    elif operador == '*':
        print(f'{num1} * {num2} = {num1 * num2}')
    else: 
        print(f'{num1} / {num2} = {num1 / num2}')

    sair = input('Deseja sair? [S] Sim: ').upper().startswith('S')
    if sair:
        break