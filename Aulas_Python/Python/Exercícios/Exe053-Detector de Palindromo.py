# Palindromo = Palavras que possuem a mesma grafia na ordem direta ou inversa
frase=str(input('Digite uma Frase: ')).strip().upper() #Strip()--->tira os espaços e upper() coloca tudo em maius
palavras = frase.split() # Split() divide as palavras
junto = ''.join(palavras) # .join --->junta as palavras com '' oq ue estiver entre aspas. serve para tirar os espaços

'''for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]''' # primeira forma qe fazer


inverso = junto[::-1] # segunda forma: Fatiametno de String e mostra ao contrário (-1)


print('O inverso de {} é \n{}'.format(junto,inverso))
if inverso==junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palindromo!')
#print(junto, inverso)


