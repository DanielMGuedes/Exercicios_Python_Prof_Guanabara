# Programa que vai ler: IDADE e SEXO de varias pessoas(Até o user pedir para parar)
# depois vai analisar(incluir sleep) e mostrar..a)Qts pessoas com mais de 18 anos
# B) Qts homens?
# c) Qts mulheres com menos de 20 anos
# 1ª parte do Programa: Lê a idade e o sexo, em loop, até o break
'''
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('Acabou') '''

# 2ª parte do eXERCICIO: Inclusão das variavéis para responder as perguntas da analise
'''
tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Total de Homens cadastrados é {totH}')
print(f'Total de Mulheres com menos de 20 aos é {totM20}')'''

# 3ª parte Incrementrando o código: incluir Sleep e contagem do total de pessoas

from time import sleep

totp = tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if sexo == 'M' or 'F':
        totp += 1
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('ANALISANDO...')
sleep(2)
print('*-'*30)
print(f'Total de pessoas cadastradas foi de: \n{totp} PESSOA(s) ')
print(f'A Quantidade Total de Pessoas com mais de 18 anos é \n{tot18} PESSOA(s)')
print(f'Total de Homens cadastrados é \n{totH} HOMEN(s)')
print(f'Total de Mulheres com menos de 20 aos é \n{totM20} MULHERE(s)')
print('*-'*30)