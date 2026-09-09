# EX100 - Sortear e somar (minha versao)
from random import sample


def sorteia():
    return sample(range(1, 11), 5)


def soma_pares(valores):
    return sum(v for v in valores if v % 2 == 0)


numeros = sorteia()
print(f'Sorteados: {numeros}')
print(f'Soma dos pares: {soma_pares(numeros)}')