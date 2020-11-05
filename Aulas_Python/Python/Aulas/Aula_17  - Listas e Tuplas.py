#Listas parte 1
'''num = [2,5,9,11,4,4,14,44]
num[2] = 3
num.append(7)
num.sort(reverse=True) # sort(ordenar / reverse(ao contrário)
num.insert(2,2)
if 5 in  num:
    num.remove(5)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa Lista tem {len(num)} elementos.')'''

#Desafio: Incluir input e Flag...e solictação de continuar ou não
'''
valores = []
valores.append(5)
valores.append(9)
valores.append(4)'''

'''valores = list()
for cont in range (0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores): # enumerateTrouxe a posição e o valor
    print(f'na posição {c} encontrei o valor {v} !')
print('Cheguei ao final da Lista.')'''

#Dica: Se criar uma variavel a partir da cópia de outra . Não pode ussar simples =
# Se utilizar b = a - vai criar uma ligação. e as alterações vão refletir em ambas.
'''a = [2,3,4,7]
b = a
b[2] = 8
print(f'Lista A: {a} ')
print(f'Lista B: {b} ')'''
# PAra fazer a cópia tem que usar: b = a[:]
a = [2,3,4,7]
b = a[:]
b[2] = 8
print(f'Lista A: {a} ')
print(f'Lista B: {b} ')