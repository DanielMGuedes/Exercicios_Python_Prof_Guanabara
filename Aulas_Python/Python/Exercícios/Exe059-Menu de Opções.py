from time import sleep
opção = 0
result = 0
print('-=-'*20)
print('Você vai Digitar 2 numeros e depois escolher o que fazer com eles')
print('-=-'*20)
num1=float(input('Digite o Primeiro Número: '))
num2=float(input('\nDigite o Segundo Número: '))
print('-*-'*20)
sleep(1)
while opção != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    print('-*-'*20)
    sleep(1)
    opção = int(input('>>>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = num1 + num2
        print('A soma entre {} + {} é {}'.format(num1,num2,soma))
    elif opção == 2:
        produto = num1 * num2
        print('O Produto entre {} X {} é {}'.format(num1, num2, produto))
    elif opção == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('Entre {} e {} o maior valor é {}'.format(num1, num2, maior))
    elif opção == 4:
        print('Informe os números novamente:')
        num1 = int(input('Digite o Primeiro Número: '))
        num2 = int(input('Digite o Segundo Número: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção invalida! tente novamente')
    print('-*-' * 10)
    sleep(2)
print('Fim do Programa! Volte Sempre')

