#iniciamos IMPORT MATH mas só precisamos de uma função do pacote. Por isso colocamos (FROM MATH IMPORT TRUNC)
# trunc - parte inteira de um número
from math import trunc
x=float(input('Digite um valor: ' ))
print('A porção inteira do valor digitado {} é o numero {}'.format(x, trunc(x)))