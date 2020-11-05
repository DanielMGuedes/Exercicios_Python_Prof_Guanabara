'''
\033[0;33;44m > Sintaxe para utilizar cores no terminal (Padrão ANSI)
\033 - Inicial obrigatório
[0; - 1ª de 3 códigos = Style: 0 - Normal/ 1 - Negrito / 4 - Sublinhado / 7 - Negative(troca o fundo)
;33 - 2ª código = Cor Text: 30 / 31 / 32 / 33/ 34/ 35/ 36/ 37
;44 - 3ª código = Cor Fundo: 40 / 41 / 42 / 43/ 44/ 45/ 46/ 47

Códigos de

print('\033[0;30;41mteste fundo VERM\033[m')
print('\033[4;33;44mteste fundo AZU\033[m')
print('\033[1;35;43mteste fundo AMA\033[m')
print('\033[30;42mteste fundo VED\033[m')
print('\033[mteste fundo PRET\033[m')
print('\033[7;30mteste fundo BRC\033[m')
'''
n='Jose'
i=25
print('vc é {} e tem {}'.format(n,i))