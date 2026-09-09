# EX089 - Boletim (minha versao com dicionarios)
boletim = []
while True:
    nome = input('Nome: ').strip()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    boletim.append({'nome': nome, 'notas': [n1, n2], 'media': (n1 + n2) / 2})
    if input('Continuar? [S/N] ').strip().upper() == 'N':
        break

print(f'{"No.":<4}{"NOME":<12}{"MEDIA":>8}')
print('-' * 26)
for i, aluno in enumerate(boletim):
    print(f'{i:<4}{aluno["nome"]:<12}{aluno["media"]:>8.1f}')
while True:
    opc = int(input('Notas de qual aluno? (999 sai) '))
    if opc == 999:
        break
    if 0 <= opc < len(boletim):
        print(f'Notas de {boletim[opc]["nome"]}: {boletim[opc]["notas"]}')
print('Volte sempre!')