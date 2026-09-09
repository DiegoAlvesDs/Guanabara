# EX061 - Progressao Aritmetica v2.0 (minha versao com range)
print('== Gerador de PA ==')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
for termo in range(primeiro, primeiro + 10 * razao, razao):
    print(termo, end=' -> ')
print('FIM')