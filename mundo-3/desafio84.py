# EX084 - Lista composta (minha versao)
galera = []
while True:
    nome = input('Nome: ').strip()
    peso = float(input('Peso: '))
    galera.append([nome, peso])
    if input('Continuar? [S/N] ').strip().upper() == 'N':
        break

pesos = [p for _, p in galera]
mais_pesados = [n for n, p in galera if p == max(pesos)]
mais_leves = [n for n, p in galera if p == min(pesos)]

print(f'Cadastradas: {len(galera)} pessoa(s)')
print(f'Maior peso: {max(pesos)}Kg -> {mais_pesados}')
print(f'Menor peso: {min(pesos)}Kg -> {mais_leves}')