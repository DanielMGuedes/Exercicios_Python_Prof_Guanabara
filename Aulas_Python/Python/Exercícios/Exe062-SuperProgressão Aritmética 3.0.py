print('#-'*5, 'Gerador de PA', '#-'*5)
print('-='*10)
primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} > '.format(termo),end='')
        termo += razão
        cont += 1
    print('FIM')
    mais = int(input('Quantos Termos você quer colocar a mais? '))
print('Progressão finalizado com {} termos mostrados'.format(total))
