''' Calcule o valor a ser pago por produto considerando preço normal e condiç~´oes especiais:
- à vista dinheiro 10% de desconto
- à vista no cartão 5% desconto
- ate 2x no cartão: preço normal
- 3x ou mais no cartão: 20% juros
'''

print('='*12,'LOJAS DANIELS', '='*12)
compra=float(input('Preço das Compras: R$ '))
print('''Escolha a FORMA DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque 10% desconto
[ 2 ] à vista cartão 5% desconto
[ 3 ] 2X no cartão: preço normal
[ 4 ] 3X ou mais no cartão 20$ de juros''')
opção=int(input('Qual é a sua opção?  '))
if opção == 1:
    total = compra - (compra * 10/100)
elif opção == 2:
    total = compra - (compra * 5/100)
elif opção == 3:
    total = compra
    parcela = total /2
    print('Sua compra será parcela em 2X de R$ {:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = compra + (compra * 20/100)
    totparc = int(input('Quantas Parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcela em {:.2f}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    print('Opção invalida! Tente novamente')
    print('Sua compra de R${:.2f} vai custar R${} no final'.format(compra,compra))

# print('Sua compra de R${} vai custar R${} no final.'.format(compra,opção))

