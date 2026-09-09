# EX104 - Leitura validada (minha versao com try/except, aceita negativos)
def leia_int(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print('ERRO! Digite um numero inteiro valido.')


numero = leia_int('Digite um numero: ')
print(f'Voce digitou {numero}.')