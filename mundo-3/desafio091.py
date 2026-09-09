# EX091 - Jogo de dados (minha versao com lambda no ranking)
from random import randint
from time import sleep

resultados = {f'jogador{i}': randint(1, 6) for i in range(1, 5)}
print('Valores sorteados:')
for nome, dado in resultados.items():
    print(f'  {nome} tirou {dado}')
    sleep(1)
print('=== RANKING ===')
for pos, (nome, dado) in enumerate(sorted(resultados.items(), key=lambda x: x[1], reverse=True), 1):
    print(f'  {pos}o lugar: {nome} ({dado})')