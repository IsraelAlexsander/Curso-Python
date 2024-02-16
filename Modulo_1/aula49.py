"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável )
"""

lista_a = ['Luis', 'Maria']
lista_b = lista_a           # Aponta para o local de memoria da lista_a

lista_a[0] = 'Mudei o valor'
print(lista_b)

lista_c = ['Rael', 'Alex']
lista_d = lista_c.copy()

lista_c[0] = 'Mudei o valor'
print(lista_d)