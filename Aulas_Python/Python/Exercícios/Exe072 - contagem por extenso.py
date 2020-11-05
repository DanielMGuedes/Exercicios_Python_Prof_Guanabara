cont = 'zero', 'um', 'dois','três', 'quatro', 'cinco', 'seis', 'sete', '...'
while True:
    núm = int(input('Digite um número entre 0 e 20: '))
    if 0<= núm <= 20:
        break
    print('tente novamente. ', end='')
print(f'Você digitou {cont[núm]}')

'''Explicação:
o cont está recebendo o valor que escrevemos por
extenso na posição, correspondente a cada um 0 = zero, etc..

'''

COMPLETAR EXERCÍCIO....

