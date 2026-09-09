# EX080 - Lista ordenada sem sort (minha versao com bisect)
from bisect import insort

lista = []
for i in range(5):
    n = int(input('Digite um valor: '))
    insort(lista, n)
    print(f'Adicionado na posicao {lista.index(n)}.')
print(f'Lista ordenada: {lista}')