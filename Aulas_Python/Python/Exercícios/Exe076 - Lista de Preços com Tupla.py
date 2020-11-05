'''
Criar Programa que Leia a lista de Comrpras e seus valores (Tuplas)
'''

Lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.9,
         'Estojo', 25,
         'Trafer', 4.20,
         'Comprasso', 9.99,
         'canetas', 22.30,
         'Livro', 34.90)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range (0, len(Lista)):
    if pos %2 == 0:
        print(f'{Lista[pos]:.<30}', end=' ')
    else: print(f'R${Lista[pos]:.>8.2f}')
