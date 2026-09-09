# EX082 - Dividindo listas (minha versao)
valores = []
while True:
    valores.append(int(input('Digite um numero: ')))
    if input('Continuar? [S/N] ').strip().upper() in 'Nn':
        break
pares = [v for v in valores if v % 2 == 0]
impares = [v for v in valores if v % 2 != 0]
print(f'Completa: {valores}')
print(f'Pares:    {pares}')
print(f'Impares:  {impares}')