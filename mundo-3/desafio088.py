# EX088 - Mega Sena (minha versao com random.sample)
from random import sample
from time import sleep

quant = int(input('Quantos jogos da Mega Sena? '))
print(f'==== SORTEANDO {quant} JOGO(S) ====')
for i in range(quant):
    jogo = sorted(sample(range(1, 61), 6))
    print(f'Jogo {i + 1}: {jogo}')
    sleep(1)
print('==== BOA SORTE! ====')