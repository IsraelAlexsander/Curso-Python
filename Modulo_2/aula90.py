import sys

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)   #tem __iter__ e __next__
#print(next(iterator))
lista = [n for n in range(1000000)] #fica toda na memoria
generator = (n for n in range(1000000)) #espera o valor ser chamado

#Tamanho em bytes 
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

