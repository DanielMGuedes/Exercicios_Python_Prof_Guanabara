n1=float(input('Digite a Nota 1: '))
n2=float(input('Digite a Nota 2: '))
m= (n1+n2)/2
print('Tirando {:.2f} e {:.2f}, a média do aluno é {:.2f}'.format(n1,n2,m))
if 7 > m >=5:
    print('O Aluno está de RECUPERAÇÃO')
elif m < 5:
    print('REPROVADO')
elif m >= 7:
    print('APROVADO')