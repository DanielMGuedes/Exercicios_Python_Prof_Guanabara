from random import randint
from time import sleep
computador = randint(0,10) # Faz o PC escolher um nr entre 0 e 5 aleatóriamente.
print('-=-'*20)
print('Olá! Sou seu computador... \nAcabei de pensar em um número entre 0 e 10...')
sleep(1)
print('Será que você consegue advinhar qual foi? ')
print('-=-'*20)
sleep(2)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Me diga! Qual foi o número que pensei?  ')) # Jogador tentando adivinhar
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('processing...')
sleep(3) # sleep faz parte do pacote time e faz uma pausa no processamento..
print('Muito bem! Voce acertou na {}ª tentativa!'.format(palpite))
# else: print('Voce Errou. Tente outra Vez!')