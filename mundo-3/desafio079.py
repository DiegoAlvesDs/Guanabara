# EX079 - Valores unicos (minha versao com set)
numeros = set()
while True:
    n = int(input('Digite um valor: '))
    if n in numeros:
        print('Repetido! Nao vou adicionar.')
    else:
        numeros.add(n)
        print('Adicionado com sucesso!')
    if input('Continuar? [S/N] ').strip().upper() == 'N':
        break
print(f'Valores finais (ordenados): {sorted(numeros)}')