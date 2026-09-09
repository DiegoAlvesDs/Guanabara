# EX085 - Pares e impares separados (minha versao)
valores = [[], []]  # [pares, impares]
for i in range(7):
    n = int(input(f'{i + 1}o. valor: '))
    valores[n % 2].append(n)
valores[0].sort()
valores[1].sort()
print(f'Pares:   {valores[0]}')
print(f'Impares: {valores[1]}')