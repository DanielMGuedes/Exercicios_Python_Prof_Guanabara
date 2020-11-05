'''
Criar Programa que peça ao usuario digitar varios VALORES
NUMERICOS e cadastre-os em uma lista. caso o número já tenha sido digitado
ele não aceitaram. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''

núm = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in núm:
        núm.append(n)
        print('Valor adicionado com suicesso...')
    else:
        print('Valor duplicado! Não vou adicionar a lista...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-='*30)
núm.sort()
print(f'Você digitou os valores {núm}')