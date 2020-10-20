print('-='*20)
print('Analisador de Triangulos V2')
r1=float(input('Digite o tamanho do 1º segmento: '))
r2=float(input('Digite o tamanho do 2º segmento: '))
r3=float(input('Digite o tamanho do 3º segmento: '))
if r1 < (r2+r3) and r2 < r1+r3 and r3 < r1+r2:
    print('Os segmentos, {}, {} e {} podem formar um triangulo:'.format(r1,r2,r3))
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓCELES')
else:
    print('Os segmentos, {}, {} e {} NÃO PODEM formar um triangulo:'.format(r1,r2,r3))