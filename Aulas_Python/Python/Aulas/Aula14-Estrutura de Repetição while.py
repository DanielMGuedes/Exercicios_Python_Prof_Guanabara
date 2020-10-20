'''LAÇOS DE REPETIÇÃO - Estrutura de repetição while no Python. Por exemplo:
c=1 while c !=10:
print(c)
c+=1
print(‘Acabou’) '''
'''for c in range(1,10): # fORMA DE FAZER USANDO O FOR
    print(c, end='-')
print('Fim')'''
'''c = 1     # 2ª Forma de fazer usando o while
while c< 10:
    print(c, end=' ')
    c += 1
print('Fim')'''
# Ambas as formas podem ser utilizadas quando se sabe o limite.
# Quando não se sabe o limte usamos o WHILE
#Exemplo 1:
'''r = 'S'
while r == 'S': # Flag (Indica ao programa o ponto para parar a iteração
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')'''
#Exemplo 2:
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 ==0:
            par += 1
        else:
            impar += 1
print('Vc digitou {} numeros PAres e {} numeros impares!'.format(par,impar))