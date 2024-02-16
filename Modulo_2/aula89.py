# dir, hasattr, e getattr em Python

string = 'Luiz'
metodo = 'upper'

if hasattr(string, 'upper'):
    print('Existe upper')
    print(string.upper())

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())