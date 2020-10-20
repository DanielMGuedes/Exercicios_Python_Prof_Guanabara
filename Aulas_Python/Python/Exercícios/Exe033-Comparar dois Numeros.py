a = int(input('primeiro valor: '))
b = int(input('primeiro valor: '))
c = int(input('primeiro valor: '))
#verificando qual valor  é o menor
if a<b and a<c:
    menor = a
if b<c and b<a:
    menor = b
if c<a and c<b:
    menor = c
print('o menor VALOR  é {}'.format(menor))
#verificando qual valor  é o MAIOR
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('o maior valor É {}'.format(maior))
