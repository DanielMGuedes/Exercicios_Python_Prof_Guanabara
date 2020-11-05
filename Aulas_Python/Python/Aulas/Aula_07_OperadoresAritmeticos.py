#nome=input('Qual é o seu nome? ')
# print('Prazer em te conhecer {:=^20}!'.format(nome))
n1=int(input('Digite um valor: '))
n2=int(input("Digite outro valor: "))
s=n1+n2 # Soma
m=n1*n2 # multiplicação
d=n1/n2 # divisão
di=n1//n2 # PArte "inteira" da Divisão
e=n1**n2 # Potencia
dr=n1%n2 # PArte "Resto" da Divisão
print('A soma é {}, \n o produto é {} e a \n divisão é {:.3f}'.format(s,m,d), end=' >>> ')
print('\nDivisão Inteira: {}\n e Potência {}\n e DivisãoResto: {}'.format(di,e,dr))

