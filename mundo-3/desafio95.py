# EX095 - Time de jogadores (minha versao)
time = []
while True:
    j = {'nome': input('Nome do jogador: ').strip()}
    partidas = int(input(f'Quantas partidas {j["nome"]} jogou? '))
    j['gols'] = [int(input(f'  Gols na partida {p + 1}: ')) for p in range(partidas)]
    j['total'] = sum(j['gols'])
    time.append(j)
    if input('Continuar? [S/N] ').strip().upper() == 'N':
        break

print(f'{"cod":<4}{"nome":<15}{"gols":<20}{"total":<6}')
print('-' * 45)
for i, j in enumerate(time):
    print(f'{i:<4}{j["nome"]:<15}{str(j["gols"]):<20}{j["total"]:<6}')
while True:
    opc = int(input('Dados de qual jogador? (999 sai) '))
    if opc == 999:
        break
    if 0 <= opc < len(time):
        print(f'Levantamento de {time[opc]["nome"]}:')
        for i, g in enumerate(time[opc]['gols'], 1):
            print(f'  Jogo {i}: {g} gol(s)')
    else:
        print('Codigo invalido!')
print('Volte sempre!')