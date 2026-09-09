# EX066 - Varios numeros com flag (minha versao)
valores = []
while True:
    n = int(input('Digite um numero [999 para parar]: '))
    if n == 999:
        break
    valores.append(n)
print(f'Voce digitou {len(valores)} numero(s) e a soma foi {sum(valores)}.')