"""
Iterando strings com while
"""
nome = 'Rael'   ##Iteráveis
tamanho_nome = len(nome)

i = 0

novo_nome = ''

while i < tamanho_nome:
    novo_nome = novo_nome + f'{nome[i]}*'
    i += 1

print(novo_nome)