#Manipulando chaves e valores em dicionários
pessoa = {}

##
##

pessoa['nome'] = 'Rael'

print(pessoa)
print(pessoa['nome'])

chave = 'sobrenome'
pessoa[chave] = 'Alexsander'
print(pessoa)
print(pessoa['sobrenome'])
print(pessoa[chave])

del pessoa['sobrenome']
print(pessoa)

# pessoa.get('sobrenome') retorna valor da chave, ou none caso não exista (ou parâmetro depois da chave)

if pessoa.get('sobrenome') is not None:
    print('Existe')
else:
    print('Não existe')