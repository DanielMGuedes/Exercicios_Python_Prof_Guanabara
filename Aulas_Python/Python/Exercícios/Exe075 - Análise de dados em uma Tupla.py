'''Programa que lê quatyro valores e guarda em uma tupla. No final, mostra:
a) Quantas veses apareceu o valor 9;
b) Em que posição foi digitado o primeiro valor 3;
c) Quais foram os números pares.
'''

núm = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o ultimo número: ')))
print(f'Voce digitou os valores {núm}')
print(f'O valor 9 apareceu {núm.count(9)} vezes')
if 3 in núm:
    print(f'O valor 3 apareceu na {núm.index(3)+1}ª posição ')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
for n in núm:
    if n %2 == 0:
        print(n, end=' ')