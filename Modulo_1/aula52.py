"""
Tipo Tupla - Uma lista imutável
"""

nomes = ['Maria', 'Helena', 'Luiz']
nomes[1] = 'outro'

nomes = tuple(nomes)

nomes_tuple = 'Maria', 'Helena', 'Luiz'
print(nomes_tuple)