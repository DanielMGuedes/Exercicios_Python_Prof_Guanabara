num=int(input('Digite um número inteiro: '))
print('''Escolha a opção para escolher a base de conversão': 
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal''')
opção=int(input('Sua opção: ' ))


if opção == 1:
    print('{} convertido para Binário é igual a {}'.format(num,bin(num)[2:]))
elif opção == 2:
    print('{} convertido para Octal é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, tente novamente!')
