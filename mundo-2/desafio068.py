# EX068 - Par ou Impar (minha versao)
from random import randint

vitorias = 0
print('Vamos jogar PAR ou IMPAR!')
while True:
    jogada = int(input('Seu numero (0 a 10): '))
    escolha = input('Par ou Impar? [P/I] ').strip().upper()
    pc = randint(0, 10)
    total = jogada + pc
    resultado = 'PAR' if total % 2 == 0 else 'IMPAR'
    print(f'Voce: {jogada} | Computador: {pc} | Total: {total} = {resultado}')
    ganhei = (escolha == 'P') == (total % 2 == 0)
    if ganhei:
        print('Voce ganhou! Vamos de novo...')
        vitorias += 1
    else:
        print('Voce perdeu!')
        break
print(f'Placar final: {vitorias} vitoria(s) consecutiva(s).')