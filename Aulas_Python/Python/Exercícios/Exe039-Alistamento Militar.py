from datetime import date
anoatual= date.today().year
anonasc=int(input('Ano de nascimento: '))
idade = anoatual - anonasc
print('Quem nasceu em {} tem {} anos em {}.'.format(anonasc, idade, anoatual))
if idade == 18:
    print('Você tem que alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda tem menos de 18 anos em {}. Ainda faltam {} anos para o seu alistamento.'.format(anoatual,saldo))
    ano = anoatual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = anoatual - saldo
    print('Já passou a hora de você se alistar! Você deveria ter se alsitado há {} anos.'.format(saldo))
    print('Seu alistamento foi em {}'.format(ano))

