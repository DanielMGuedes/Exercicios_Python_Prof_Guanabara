'''
Criar Programa onde o usuário digite uma expressão metamtica. e o Program vai validar
se a quantidade de parenteses (Abre e FEcha) estão validos.
'''

expre = str(input('Digite sua expressão matemática: '))
pilha = []
for símb in expre:
    if símb =='(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
