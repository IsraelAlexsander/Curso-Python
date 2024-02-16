"""
Faça um jogo para o usuário advinhar qual a palavra secreta.
-Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
    - Se a letra estiver na palavra, exiba a letra
    - Se a litra não estiver na palavra, exiba *
- Faça uma contagem de tentativas
"""

palavra_secreta = 'variavel'
letras_acertadas = ''

while True:
    letra_digitada = input('Digite uma letra: ')

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra...')
        continue    

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''    
    for letra_Secreta in palavra_secreta:
        if letra_Secreta in letras_acertadas:
            palavra_formada += letra_Secreta
        else:
            palavra_formada += '*'

    print(palavra_formada)