# Introdução às Generator functions 
# generator = (n for n in range(1000000))

# def generator(n=0):
#     yield 1     # Pausar 
#     print('Continuando...')
#     yield 2     # Pausar
#     print('Mais uma...')
#     yield 3
#     print('Vou terminar') 
#     return 'Acabou'

def generator(n=0, maximun=10):
    while True:
        yield n
        n += 1

        if n > maximun:
            return            

gen = generator(n=5, maximun=8)
# print(next(gen))
# print(next(gen)) 
# print(next(gen))

for n in gen:
    print(n)
