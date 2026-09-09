# EX074 - Sorteio em tupla (minha versao com random.sample)
from random import sample

numeros = tuple(sample(range(1, 11), 5))
print(f'Sorteados: {numeros}')
print(f'Maior: {max(numeros)} | Menor: {min(numeros)}')