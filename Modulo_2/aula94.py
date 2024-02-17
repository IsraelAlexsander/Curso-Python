# try, except, else e finally

try:
    print('Abrir Arquivo')
    #8/0
except ZeroDivisionError:
    print('Dividiu zero')
else:       #Quando não der erro
    print('Não deu erro')
finally:    #Sempre sera executado
    print('Fechar Arquivo')