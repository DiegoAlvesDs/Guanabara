# EX065 - Maior e media do grupo (minha versao)
cadastros = []  # lista de (nome, idade, sexo)
while True:
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    cadastros.append((nome, idade, sexo))
    if input('Continuar? [S/N] ').strip().upper() == 'N':
        break

idades = [i for _, i, _ in cadastros]
homens = [(n, i) for n, i, s in cadastros if s == 'M']
mulheres_jovens = [n for n, i, s in cadastros if s == 'F' and i < 20]

print(f'Total cadastrado: {len(cadastros)}')
print(f'Media de idade: {sum(idades) / len(idades):.1f}')
if homens:
    velho = max(homens, key=lambda x: x[1])
    print(f'Homem mais velho: {velho[0]} ({velho[1]} anos)')
print(f'Mulheres com menos de 20: {len(mulheres_jovens)}')