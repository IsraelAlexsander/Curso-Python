"""
Flag (bandeira) - Marcar um local
None = não valor
'is' e 'is not' = é ou não é (tipo, valor, identidade)
id = identidade
"""
condição = True
passou_no_if = None

if condição:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

if passou_no_if is None:
    print('Não passou no if')

if passou_no_if is not None:
    print('Passou no if')


# v1 = 'a'
# v2 = 'a'
# print(id(v1))
# print(id(v2))
# Vão possuir o mesmo id, por conta do valor ser o mesmo

# v2 = 'b'

# print(id(v1))
# print(id(v2))