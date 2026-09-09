# EX071 - Caixa eletronico (minha versao com divmod)
print('=== BANCO DA COBRINHA ===')
valor = int(input('Valor do saque: R$'))
for cedula in (50, 20, 10, 1):
    qtd, valor = divmod(valor, cedula)
    if qtd:
        print(f'{qtd} cedula(s) de R${cedula}')
print('Volte sempre!')