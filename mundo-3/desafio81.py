# EX081 - Extraindo dados de lista (minha versao)
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    if input('Continuar? [S/N] ').strip().upper() in 'Nn':
        break
valores.sort(reverse=True)
print(f'Total de elementos: {len(valores)}')
print(f'Ordem decrescente: {valores}')
print('O 5 esta na lista!' if 5 in valores else 'O 5 nao esta na lista.')