# EX073 - Times de futebol (minha versao)
times = ('Flamengo', 'Palmeiras', 'Corinthians', 'Sao Paulo', 'Gremio',
         'Internacional', 'Fluminense', 'Botafogo', 'Vasco', 'Bahia',
         'Sport', 'Fortaleza', 'Cruzeiro', 'Atletico-MG', 'Ceara',
         'Athletico-PR', 'Santos', 'Goias', 'Chapecoense', 'Avai')
print(f'Brasileirao: {times}')
print(f'G-5: {times[:5]}')
print(f'Z-4: {times[-4:]}')
print(f'Alfabetica: {sorted(times)[:5]} ...')
pos = times.index('Chapecoense') + 1
print(f'A Chapecoense esta na {pos}a posicao.')