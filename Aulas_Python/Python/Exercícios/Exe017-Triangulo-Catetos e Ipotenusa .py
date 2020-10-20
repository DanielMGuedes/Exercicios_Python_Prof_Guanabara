# 1ª Forma de Fazer - Conceitos matemáticos
''' co=float(input('Digite o Valor do comprimento do Cateto oposto: '))
ca=float(input('Digite o Valor do Cateto adjacente: '))
hi= (co**2 + ca**2) ** (1/2)
print('O Valor da Hipotenuza vai medir {:.2f} '.format(hi)) '''

# 2ª Forma de fazer - Importanto função do pacote math

from math import hypot
co=float(input('Digite o Valor do comprimento do Cateto oposto: '))
ca=float(input('Digite o Valor do Cateto adjacente: '))
hi = hypot(co,ca)
print('o valro da hipotenuza é {:.2f}'.format(hi))
