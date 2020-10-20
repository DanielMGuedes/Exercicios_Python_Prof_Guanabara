# PA feito com for _ in range
'''primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão: '))
décimo=primeiro +(10-1) * razão
for c in range (primeiro, décimo + razão, razão):
    print('{} '.format(c), end=' -> ')
print('ACABOU')'''

# PA feita com while

print('#-'*5, 'Gerador de PA', '#-'*5)
print('-='*10)
primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} > '.format(termo),end='')
    termo += razão
    cont += 1
print('FIM')