'''nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo'
    print('Que nome lindo você tem!')
print('Bom dia {}!'.format(nome))'''

n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))
m = (n1+n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Parabéns você foi aprovado')
else: # pode tirar o else sem problema****
    print('Sorry. Vai ter que estudar mais!')