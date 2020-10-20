n=int(input('Digite um número inteiro: '))
result = n % 2 # % resto da divisão
#'''print('O resultado foi {}'.format(result))''' - Teste para ver
if result == 0:
    print('O número {} seu número é par'.format(n))
else:
    print('O número {} seu número é impar'.format(n))

