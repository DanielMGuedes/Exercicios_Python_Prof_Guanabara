# Programa que vai escolher aleatoriamente um numero e comapra entra PAR ou IMPAR
#Vai jogar par ou impar com o computador. e o jogo vai mostrar o resultado
# O jogo será interrompido somente quando o JOGADOR perder. e vai mostrar
# a qtd de vitorias do jogador
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. A Soma é {total}. ', end='')
    print('\n ESSE NÚMERO É PAR' if total % 2 == 0 else 'ESSE NÚMERO É IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU JOGADOR!')
            v += 1
        else:
            print('Voce PERDEU"')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Voce PERDEU"')
            break
    print('Eu perdi, vamos jogar novamente...')
print(f'GAME OVER! VOCE PERDEU DESSA VEZ. MAS VOCE VENCEU {v} vezes.')




