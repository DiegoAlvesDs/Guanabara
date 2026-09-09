# EX076 - Lista de precos (minha versao com zip)
produtos = ('Lapis', 'Borracha', 'Caderno', 'Estojo', 'Transferidor',
            'Compasso', 'Mochila', 'Canetas', 'Livro')
precos = (1.75, 2.00, 15.90, 25.00, 4.20, 9.99, 120.32, 22.30, 34.90)
print('=' * 35)
print(f'{"LISTAGEM DE PRECOS":^35}')
print('=' * 35)
for nome, preco in zip(produtos, precos):
    print(f'{nome:<25} R$ {preco:>7.2f}')
print('=' * 35)