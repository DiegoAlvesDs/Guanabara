# EX087 - Analise da matriz (minha versao)
matriz = [[int(input(f'Valor para [{l}, {c}]: ')) for c in range(3)] for l in range(3)]
for linha in matriz:
    print(' '.join(f'[{v:^5}]' for v in linha))
soma_pares = sum(v for linha in matriz for v in linha if v % 2 == 0)
soma_col3 = sum(linha[2] for linha in matriz)
maior_l2 = max(matriz[1])
print(f'Soma dos pares: {soma_pares}')
print(f'Soma da 3a coluna: {soma_col3}')
print(f'Maior da 2a linha: {maior_l2}')