p=float(input('Qual o preço do Produto? R$ '))
desc=float(input('Qual o desconto do produto? R$ '))
novo=p - (p * desc/100)
print('O produto com desconto de {:.2f} fica no valor de {:.2f}'.format(desc,novo))