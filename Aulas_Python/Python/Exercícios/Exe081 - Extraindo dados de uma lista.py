'''
Digitar valores enquanto o usario quiser e coloque numa lista.
 Depois informe Quantos numeros foram digitrados.
 A lista de calores , orednada de forma decrescente.
 Se o VAlor 5 foi digitado e está ou não na lista.
'''

valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Voê digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da Lista!')
else:
    print('O valor 5 NÃO FAA parte da lista!')
