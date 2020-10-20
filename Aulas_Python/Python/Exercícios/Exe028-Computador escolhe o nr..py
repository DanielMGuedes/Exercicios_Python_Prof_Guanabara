from random import randint
from time import sleep
pc = randint(0,5) # Faz o PC escolher um nr entre 0 e 5 aleatóriamente.
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. tente Adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei?  ')) # Jogador tentando adivinhar
print('processing...')
sleep(3) # sleep faz parte do pacote time e faz uma pausa no processamento..
if jogador == pc :
    print('Muito bem! Voce acertou!')
else: print('Voce Errou. Tente outra Vez!')

