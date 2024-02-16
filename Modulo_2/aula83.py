# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
#print(a, b)

pessoa = {
    'nome': 'Aline', 
    'sobrenome': 'Souza',
}
#a, b = pessoa  recebe as chaves
#a, b = pessoa.items()  recebe tuplas com chaves e valores
#(a1, a2), b = pessoa.items()   
# a, b = pessoa.values()
# print(a, b)

# for chave, valor in pessoa.items():
#     print(valor)

dados_pessoas = {
    'idade': 16,
    'altura': 1.6,
}

pessoa_completa = {**pessoa, **dados_pessoas}

#print(pessoa_completa)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)
def mostrar_argumentos_nomeados(*args, **kwargs):
    #print(kwargs)
    print('Não nomeados: ', args)
    for chave, valor in kwargs.items():        
        print(chave, valor)

#mostrar_argumentos_nomeados(nome = 'Joana', qlq = 123)
mostrar_argumentos_nomeados(**pessoa_completa)