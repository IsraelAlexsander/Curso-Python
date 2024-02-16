# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

import copy # Modulo para copias

pessoa = {
    'nome': 'Rael',
    'sobrenome': 'Alexsander'
}

#print(pessoa.__len__())
# print(len(pessoa))
# print(pessoa.keys())
# print(pessoa.values())
# print(pessoa.items())
# print(pessoa.get('nome'))   #Pode passar valor padrão, caso não exista
# nome = pessoa.pop('nome')
# print(nome)
# print(pessoa)
# ultima_chave = pessoa.popitem()    #apaga a ultima chave e retorna
# print(ultima_chave)
# print(pessoa)
pessoa.update({
    'nome': 'Israel'
})
print(pessoa)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa.setdefault('idade', 0)
print(pessoa['idade'])

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2]
}

# d2 = d1.copy()  #Copia os valores imutaveis, mas os mutaveis continuam por referência
d2 = copy.deepcopy(d1)

d2['c1'] = 1000
d2['l1'][1] = 999999

print(d1)
print(d2)