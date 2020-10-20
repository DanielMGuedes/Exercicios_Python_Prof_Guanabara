# Criar um programa que peça para o usuario digitar numeros e para sometne quando for digitado a flag '999'
# NO Final o programa deve somar todos os numeros menos a flag.
num = cont = soma = 0
num = int(input('Digite um numero 999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um numero 999 para parar]: '))
print('Voce digitou {} números e a soma entre eles foi {}.'.format(cont,soma))