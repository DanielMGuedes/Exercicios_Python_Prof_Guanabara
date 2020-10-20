# Se usar o While sem o BReak - é preciso fazer uma gambiara
# exemplo c/ gambiara

'''num = soma = 0
while num != 999:
    num = int(input('Digite um valor (999 para parar): '))
    soma += num # se escrever o codigo até aqui.. ele vai somar o numero 999 junto
soma -= 999 # para resover isso vem a gambiara*
print(f'A soma dos valores foi {soma}!')'''

# O certo é usar o While True - Ele vai ler para sempre até o break
soma = cont = 0 # Vamos inserir um contador para dizer qtos nrs foram digitados
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num # se escrever o codigo até aqui .. agora ele NÃO soma o 999
print(f'A soma dos {cont} números foi {soma}!')