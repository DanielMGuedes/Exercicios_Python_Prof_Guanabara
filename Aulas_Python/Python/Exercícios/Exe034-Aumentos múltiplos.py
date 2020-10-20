sal=float(input('Qual é o Salário do Funcionário R$ '))

if sal <= 1250:
    novo = sal * 1.15
else:
    novo = sal * 1.10
print('\nPara salários superiores a R$ 1250.00 o aumento é de 10% \nPara salários inferiors ou iguas, o aumento é de 15%')
print('\nO novo salario para o valor de R${} vai ser de R${}'.format(sal,novo))