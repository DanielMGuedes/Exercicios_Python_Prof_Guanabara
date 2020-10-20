l=float(input('Qual a largura da sua parede: '))
a=float(input('Qual a altura da sua parede: '))
ar=l*a
t=ar/2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m2'.format(l,a,ar))
print('para pintar essa parede, você precisará de {}l de tinta'.format(t))