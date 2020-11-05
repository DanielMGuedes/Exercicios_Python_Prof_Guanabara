'''
Criar Lista de Palavras e fazer a contagem das vogais das palavras.
*DESAFIO.....Solicitar ao usuário se quer continuar ou não
'''

palavras = ('aprender', 'programar', 'linguagem',
            'python', 'bigData', 'programador')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as seguintes vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')