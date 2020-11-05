#Comandos ensinados durante a Aula:
# fatiamento: frase[1:15] / [:2] / [:] - pega os caracteres desse espaço da memória.
#len(frase) - quantos espaços de memória ocupa a strg
#frase.count('o') - contar o objeto
#frase.find('deo') - Procurar
# 'Curso' in frase - Pergunta se tem a Strg na variavél
# frase.replace('Python', Android') - Substitui uma palavra pela outra
# frase.upper() - Coloca as letras em MAIUSCULOS
# frase.lower() - Coloca as letras em minusculas
# frase.capitalize() - Deixa apenas a primeira letra da frase em MAIUSCULO
# frase.title() - Deixa as primeiras letras de cada palavra em MAIUSCULO
# frase.strip() - remove os espaços em branco no início e no fim da frase(espaços inúteis)
# frase.rstrip() - remove os espaços em branco no lado direito(right) da frase(espaços inúteis)
# frase.lstrip() - remove os espaços em branco no lado esquerdo(lefth) da frase(espaços inúteis)
'''DIVISÃO'''
#frase.split() - trasnforma a frase(strg) em varias listas conforme os espaços
# após o SPLIT() é possível utilizar o '-'.join(frase) para acrescentar o '-' entre cada lista criada.
# print(frase.upper().count('O')) - Junção de dois comandos de manipulação - Deixar tudo maiuscula e procurar
# print(len(frase.strip())) - outro exemplo de junção de funções
frase ='   Curso em Video Python   '
x = frase.replace('Python', 'Android')

print(x)





