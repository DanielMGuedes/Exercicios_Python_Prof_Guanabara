# Essa versão da Tabuada vai utilizar laços com while e break
#  tabuada de vários números, um de cada vez. Sera interrompido quando
#o numero digitado for negativo

while True:
    n = int(input('Quer ver a tabuada de qual valor Daniel? '))
    print('-'*30)
    if n <0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('-'*30)
print('PROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE!')