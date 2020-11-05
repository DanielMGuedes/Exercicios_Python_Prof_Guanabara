'''
Criar um programa onde o usuario possa digitar cinco valores e cadastre em uma lista.
Já na posição correta sem utilizar o sort(). No final mosttre a lista ordenadad na tela.
'''
lista = []
for c in range (0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n>lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                print(f'Adicionado na posição {pos} lista')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')
