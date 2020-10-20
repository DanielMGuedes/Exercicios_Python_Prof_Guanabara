peso=float(input('Digite seu peso: '))
altura=float(input('Digite sua altura: '))
IMC= peso / (altura * altura)
print('O seu IMC é de {:.1f}.'.format(IMC))
if IMC < 18.5:
    print('Abaixo do Peso')
elif 18.5 <= IMC < 25:
    print('PESO IDEAL')
elif 25 <= IMC < 30:
    print('PESO SOBREPESO')
elif 30 <= IMC < 40:
    print('PESO OBESIDADE')
else:
    print('Obesidade Mórbida')

