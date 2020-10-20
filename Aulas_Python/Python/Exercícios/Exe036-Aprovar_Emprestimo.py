casa=float(input('Qual o valor da Casa: R$'))
sal=float(input('Qual o salário do comprador: R$'))
ano=int(input('Quantos anos você quer pagar? '))
res=casa/(ano*12)
min=sal*30/100
print('A Prestação será de R${} e o salário mínimo é R${}'.format(res,min))
if res <= min:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa,ano,res))
    print('O valor está dentro do limite e seu Emprestimo foi aprovado. Parabêns')
else:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, ano, res))
    print('O valor está acima do limite de 30% do seu salário. Seu Emprestimo NÃO FOI APROVADO!')


