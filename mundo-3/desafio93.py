# EX093 - Jogador de futebol (minha versao)
jogador = {}
gols = []
jogador['nome'] = input('Nome do jogador: ').strip()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for p in range(partidas):
    gols.append(int(input(f'Gols na partida {p + 1}: ')))
jogador['gols'] = gols
jogador['total'] = sum(gols)
print('-=' * 25)
print(jogador)
print(f'{jogador["nome"]} fez {jogador["total"]} gol(s) em {partidas} partida(s):')
for i, g in enumerate(gols, 1):
    print(f'  Partida {i}: {g} gol(s)')