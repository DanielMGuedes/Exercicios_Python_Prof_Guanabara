#sl=float(input('Qual o salário: '))
#au=float(input('Qual o percentual de aumento do salário: '))
#nsl= sl + (sl*au)
#print('O novo salário com aumento de {} é igual a {}'.format(au, nsl))

sal=float(input('Qual o seu salário? R$ '))
aum=float(input('Qual o precentual de aumento do salário? % '))
novosal= sal + (sal * aum/100)
print('O novo salário com aumento de {:.0f}% fica no valor de R${:.2f}'.format(aum,novosal))