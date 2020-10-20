nome=str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiúsculas é {}'.format(nome.upper())) # TUDO EM MAIÚSCULA
print('Seu nome em maiúsculas é {}'.format(nome.lower())) # TUDO EM MINÚSCULA
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))) # Contagem do nome (menos) a contagem de espaços' '
# print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) # fatiou até o primeiro espaço e separou o primeiro nome

separa = nome.split() # O Split criou as listas pelos separadores e depois utilizamos a lista [0] isolada para mostra e contar
print(' O seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0]))) #

