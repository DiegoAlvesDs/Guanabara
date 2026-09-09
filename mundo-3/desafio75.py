# EX075 - Analise de tupla (minha versao)
valores = tuple(int(input(f'Numero {i + 1}: ')) for i in range(4))
print(f'Voce digitou: {valores}')
print(f'O 9 apareceu {valores.count(9)} vez(es).')
print(f'O 3 saiu pela primeira vez na {valores.index(3) + 1}a posicao.' if 3 in valores else 'O 3 nao apareceu.')
pares = [v for v in valores if v % 2 == 0]
print(f'Valores pares: {pares if pares else "nenhum"}')