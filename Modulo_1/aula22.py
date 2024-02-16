# Operadores lógicos
# and, or e not
# Or - Qualquer condição verdadeira avalia toda a expressão como verdadeira
# Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0

entrada = input('[E] Entrar [S] Sair: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avaliação de curto circuito
print(True or False or True)
