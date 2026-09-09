# EX060 - Fatorial (minha versao com math.prod)
from math import prod

n = int(input('Numero para o fatorial: '))
fatores = range(n, 0, -1)
print(' x '.join(str(f) for f in fatores), end=' = ')
print(prod(fatores))