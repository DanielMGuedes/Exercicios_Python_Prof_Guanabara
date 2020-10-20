km=float(input('Qual a quantidade de km percorridos? '))
dias=int(input('Qual a quantidade de dias alugados? '))
pag= (dias*60) + (km*0.15)
print('O valor a pagar por {} dias alugado e {:.2f}km rodados é de R$ {:.2f} '.format(dias,km,pag))