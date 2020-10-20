# Criar: Ler um nome completo e ver se dentro desse texto tem a palavra ''Silva'' no nome

nome = str(input('Digite seu nome completo: ')).strip() # variavel nome com .strp para retirar eventuais espeaços
print('Seu nome tem Silva? {}'.format('silva' in nome.lower())) # operador 'in' para ver ser a 'string' tem na variável.

