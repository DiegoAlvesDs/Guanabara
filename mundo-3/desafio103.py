# EX103 - Ficha do jogador (minha versao)
def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


nome = input('Nome do jogador: ').strip()
gols_txt = input('Numero de gols: ').strip()
gols = int(gols_txt) if gols_txt.isdigit() else 0
ficha(nome if nome else '<desconhecido>', gols)