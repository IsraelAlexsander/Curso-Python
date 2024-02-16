"""
Exercícios
Crie funções que duplicam, triplicam e quadriplicam
o número recebido como parâmetro.
"""

def criar_multiplicador(multiplicador):
    def multiplicar(multiplicando):
        return multiplicando * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(5))
print(triplicar(5))
print(quadruplicar(5))