# 1ª parte do Programa. VAi pedir o nome e o preço de alguns Produtos. Até a Flag.

'''while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$ '))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' Fim do Programa '))'''

# 2ª parte do Programa. VAi pedir o nome e o preço de alguns Produtos. Até a Flag.
from time import sleep
total = totmil = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$ '))
    cont += 1
    total += preço # aqui ele fica rodando em loop e somando os preços
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('Processando...')
sleep(2)
print('{:-^40}'.format(' Fim do Programa '))
print(f'O total da compra foi de R${total:10.2f}')
print(f'Temos {totmil} produtos que custam mais de R$1.000')
print(f'O Produto mais barato foi {barato} que custa R$ {menor:.2f}')