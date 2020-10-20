num=int(input('Digite um número inteiro: '))
tot = 0
for c in range(1,num+1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[34m', end='')
    print('{}'.format(c), end='-')
print('\033[m0\nO numero {} foi divisível {} vezes '.format(num, tot))
if tot == 2:
    print('" por isso ele é Primo!')
else:
    print('E por isso ele não é Primo!')
