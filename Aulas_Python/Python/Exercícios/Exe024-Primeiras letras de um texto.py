# Criar: Ler o nome de uma cidade e diga se ela começa ou não com o nome "ANTO"
cid=str(input('Em que cidade você nasceu? ')).strip() #.strip() para retirra espeçaos indesejados
print(cid[:5].upper() == 'Santo') #.upper() para sempre colocar tudo em amiuscula antes de analisar
