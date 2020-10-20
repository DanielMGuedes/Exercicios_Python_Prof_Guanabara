'''A Confederaçãoprecisa de prgrama praa ler o ano de nascimetno e informar a categoria
doa atleta de acordo com sua idade: categorias:
Até 9 anos: Mirim       Até 19 anos: Junior
Até 14 anos: Infantil   Até 25 anos: Sênior     Acima de 25anos: MASTER
'''
from datetime import date
ano = int(input('Qual o Ano de nascimento do atleta: '))
atual= date.today().year
idade= atual - ano
print('No ano de {} o atleta terá {} anos '.format(atual,idade))
if idade <= 9:
    print('Categoria MIRIM')
elif idade <= 14:
    print('Categoria INFANTIL')
elif idade <= 19:
    print('Categoria JUNIOR')
elif idade <= 25:
    print('Categoria SENIOR')
elif idade > 25:
    print('Categoria MASTER')


