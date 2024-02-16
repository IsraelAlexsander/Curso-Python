"""
split e join com list e str
split - divide uma string
loin - une um string
"""

frase = '   Olha só que,   coisa interessante   '
lista_palavras_cruas = frase.split(',')   #Caractere de divisão

lista_palavras = []
for i, frase in enumerate(lista_palavras_cruas):
    lista_palavras.append(lista_palavras_cruas[i].strip())    #Apaga o espaço no inicio e no fim da string 

print(lista_palavras_cruas)
print(lista_palavras)

frases_unidas = ', '.join(lista_palavras)
print(frases_unidas)
