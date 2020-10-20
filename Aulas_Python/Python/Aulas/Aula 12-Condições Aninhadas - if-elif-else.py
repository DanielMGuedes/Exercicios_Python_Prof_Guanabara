nome=str(input('Qual é o seu nome? '))
if nome == 'Daniel':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome =='João' or nome == 'Erick':
    print('Seu nome nem é tão bonito assim!')
elif nome in 'Ana Dan Elise Pepa':
    print('Belo nome estranho')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))