# EX070 - Estatisticas de produtos (minha versao)
carrinho = []  # lista de (nome, preco)
while True:
    nome = input('Nome do produto: ').strip()
    preco = float(input('Preco: R$'))
    carrinho.append((nome, preco))
    if input('Continuar? [S/N] ').strip().upper() == 'N':
        break

total = sum(p for _, p in carrinho)
caros = [n for n, p in carrinho if p > 1000]
barato = min(carrinho, key=lambda x: x[1])

print(f'Total da compra: R${total:.2f}')
print(f'Produtos acima de R$1000: {len(caros)}')
print(f'Mais barato: {barato[0]} (R${barato[1]:.2f})')