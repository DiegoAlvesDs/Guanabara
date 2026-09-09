# EX072 - Numero por extenso (minha versao)
extenso = 'zero um dois tres quatro cinco seis sete oito nove dez onze doze treze quatorze quinze dezesseis dezessete dezoito dezenove vinte'.split()
while not (0 <= (n := int(input('Numero entre 0 e 20: '))) <= 20):
    print('Invalido! Tente de novo.')
print(f'Voce digitou: {extenso[n]}')