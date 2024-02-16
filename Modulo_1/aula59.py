# Desempacotamento em chamadas
# de métodos e funções

string = 'ABCD'
lista = ['Maria', 'Helena', 'Bianca', 'Joana', 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0         #1
    ['Maria', 'Helena'],    #0
    # 0
    ['Elaine'], #1
    #0          #1      #2
    ['Luiz', 'João', 'Eduarda'] #2
]


#p, b, *_, u = lista #*_ é resto
#print(p, u)

#for nome in lista:
#    print(nome, end=' ')    #end -> comportamento no fim de uma iteração. O padrão é quebra de linha

#print(*lista)    #Faz o mesmo que o for
#print(*string)                        
#print(*tupla)                        
print(*salas, sep='\n') #sep -> é o separador