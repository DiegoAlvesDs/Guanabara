# EX058 - Jogo da adivinhacao v2.0 (minha versao)
from random import randint

segredo = randint(0, 10)
tentativas = 0
print('Pensei em um numero de 0 a 10. Consegue adivinhar?')
while True:
    palpite = int(input('Seu palpite: '))
    tentativas += 1
    if palpite == segredo:
        break
    print('E mais...' if palpite < segredo else 'E menos...')
print(f'Isso mesmo! Voce acertou em {tentativas} tentativa(s).')