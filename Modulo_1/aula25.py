"""
Interpolação básica de strings
s - strings
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Israel'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f %s' % (nome, preco)
print(variavel)