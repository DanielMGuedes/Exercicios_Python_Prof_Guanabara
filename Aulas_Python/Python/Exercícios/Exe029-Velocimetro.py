v=float(input('Qual foi a velocidade atual do carro: '))
if v <= 80.00 :
    print('muito bem. Continue assim!')
else:
    print('Vc Ultrapassou a velocidade permitida. Vc foi multado!')
    multa = 100 + ((v-80) * 7)
    print('o valor da multa é {}!'.format(multa))
