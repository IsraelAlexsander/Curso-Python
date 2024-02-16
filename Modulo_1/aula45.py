"""
iterável -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# texto = iter('Rael') # __iter__()

# print(next(texto)) # __next__()
# print(next(texto)) 
# print(next(texto)) 
# print(next(texto)) 

# For letra in texto
texto = 'Rael' # Iteravel
iterador = iter(texto) # Iterador

while True:
    try:
        print(next(iterador))
    except StopIteration: # Erro quando termina a interação por falta de novos indices 
        break