# while/else

string = 'valor qualquer'

i = 0

while i < len(string):
    print(string[i])
    i += 1
else:
    print('Fim do while')
    
# Caso use um break, o else não será executado