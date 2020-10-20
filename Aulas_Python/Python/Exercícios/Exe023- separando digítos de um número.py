# maneira simples de fazer para entender o fatiamento por posição. O Problema á quando nã utiliza os 4 digitos(espaços)
'''
num=int(input('Digite um numero de 1 a 9999: '))
n=str(num)
print('Analisando o número {}'.format(num))
print('unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))
'''
# Forma matemática de fazer
num=int(input('Digite um numero de 1 a 9999: '))
u = num //1 %  10 # Número dividido por 1(unidade) e tiro o módulo por 10 o resultado vai ser a casa das unidades
d = num //10%  10 # Número dividido por 10(dezena) e tiro o módulo por 10 o resultado vai ser a casa das dezenas
c = num //100% 10 # Número dividido por 100(centena) e tiro o módulo por 10 o resultado vai ser a casa das centenas
m = num //1000% 10 # Número dividido por 1000(milhar) e tiro o módulo por 10 o resultado vai ser a casa do milhar
print('Analisando o número {}'.format(num))
print('unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))



