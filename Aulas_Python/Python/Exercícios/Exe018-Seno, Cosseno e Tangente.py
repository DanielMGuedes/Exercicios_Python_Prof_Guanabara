# Importando todo o pacote MATh (Ajuda para localizar a função). Mas não precisa
'''import math
ângulo=float(input('Digite o Valor do Angulo: '))
seno = math.sin(math.radians(ângulo))
print('o ângulo {} tem o seno de {:.2f}'.format(ângulo,seno))
cosseno = math.cos(math.radians(ângulo))
print('o ângulo {} tem o cosseno de {:.2f}'.format(ângulo,cosseno))
tangente = math.tan(math.radians(ângulo))
print('o ângulo {} tem a tangente de {:.2f}'.format(ângulo,tangente))'''

# Importando somente as funções necessárias do pacote

from math import radians, sin, cos, tan
ângulo=float(input('Digite o Valor do Angulo: '))
seno = sin(radians(ângulo))
print('o ângulo {} tem o seno de {:.2f}'.format(ângulo,seno))
cosseno = cos(radians(ângulo))
print('o ângulo {} tem o cosseno de {:.2f}'.format(ângulo,cosseno))
tangente = tan(radians(ângulo))
print('o ângulo {} tem a tangente de {:.2f}'.format(ângulo,tangente))