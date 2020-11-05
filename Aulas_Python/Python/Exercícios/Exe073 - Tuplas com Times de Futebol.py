times = 'Flamengo', 'Palmeiras', 'Santos', 'Gremio', 'Cruzeiro',\
        'Botafogo', 'Criciuma', 'Ponte Preta'
print('-='*15)
print(f'Lista de times do brasileirão: {times}')
print('-='*15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-='*15)
print(f'Os 4 utlimos são: {times[-4]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*15)
print(f'O Flamengo está na {times.index("Flamengo")+1}ª posição ')
