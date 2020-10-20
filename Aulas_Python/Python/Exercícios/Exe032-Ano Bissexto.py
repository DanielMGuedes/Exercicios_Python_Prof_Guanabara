from datetime import date # importando pacote date para analisar apenas o ano corrente.
Ano=int(input('Qual ano voce quer analisar? Se quiser ver sobre o ano atual coloque 0: '))
if Ano == 0:
    Ano = date.today().year
if Ano % 4 == 0 and Ano % 100 != 0 or Ano % 400 == 0 :
    print('O Ano {} é Bissexto!'.format(Ano))
else:
    print('O ano {} não é Bissexto!'.format(Ano))