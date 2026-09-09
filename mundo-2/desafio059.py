# EX059 - Menu de operacoes (minha versao com match-case; exige Python 3.10+)
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
while True:
    print('[1] somar [2] multiplicar [3] maior [4] novos numeros [5] sair')
    op = input('Sua opcao: ').strip()
    match op:
        case '1':
            print(f'{n1} + {n2} = {n1 + n2}')
        case '2':
            print(f'{n1} x {n2} = {n1 * n2}')
        case '3':
            print(f'Maior valor: {max(n1, n2)}')
        case '4':
            n1 = float(input('Primeiro valor: '))
            n2 = float(input('Segundo valor: '))
        case '5':
            print('Ate mais!')
            break
        case _:
            print('Opcao invalida!')