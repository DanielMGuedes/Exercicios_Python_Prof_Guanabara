nome=str(input('Digite seu nome completo: ')).strip()
n=nome.split()
print('Muito Prazer em te conhecer \n O Seu primeiro nome é {}'.format(n[0]))
print('O Seu último nome é {}'.format(n[len(n)-1]))
