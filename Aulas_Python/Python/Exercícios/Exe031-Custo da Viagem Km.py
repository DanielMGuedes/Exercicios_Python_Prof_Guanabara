'''d=float(input('Qual é distancia da viagem?  '))
t=float(input('Qual o preço da tarifa por Km: '))
p=d*t
print('você esta preste a começar uma viagm de {}Km.'.format(d))
print('E o preço da sua viagem será de R${} '.format(p))'''

d=float(input('Qual é distancia da viagem?  '))
print('você esta preste a começar uma viagm de {}Km.'.format(d))
#if d <= 200.0:
 #   preco = d*0.50
#else:
 #   preco = d*0.45'''
preco = d*0.50 if d <=200 else d*0.45 # Outra forma de fazer **** o guanabara não ghosta assim...
print('E o preço da sua viagem será de R${:.2f} '.format(preco))