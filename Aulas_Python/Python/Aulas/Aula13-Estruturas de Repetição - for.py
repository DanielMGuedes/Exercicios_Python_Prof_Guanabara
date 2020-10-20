#Exemplo 1
'''#for c in range(0, 7, 2):  >>>>Estrutura de repetição
#   print(c) print c
#print('FIM')'''

#Exemplo 2
'''
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim') '''

#Exemplo3
s = 0
for c in range(0,4):
    n = int(input('Digite um valor: '))
    s += n
print('O Somatório de todos os valores é {}.'.format(s))
