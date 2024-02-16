# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

respostas_certas = 0

for pergunta in perguntas:
    print(f'{pergunta["Pergunta"]}\n')       

    opcoes = pergunta['Opções']
    for i, op in enumerate(opcoes):
        print(f'{i}) {op}')
    print()

    resposta = input('Escolha uma opção: ')

    acertou = False
    resposta_int = None
    qtd_opcoes = len(opcoes)

    if resposta.isdigit():
        resposta_int = int(resposta)

    if resposta_int is not None:
        if resposta_int >= 0 and resposta_int < qtd_opcoes:
            if opcoes[resposta_int] == pergunta['Resposta']:
                acertou = True

    if acertou:
        print('Certa resposta\n')
        respostas_certas += 1
    else:
        print('Errooou\n')

print(f'Você acertou {respostas_certas}\nde {len(perguntas)} perguntas')    
