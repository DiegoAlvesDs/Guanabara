# EX099 - Maior valor (minha versao)
def maior(*numeros):
    print('-=' * 25)
    if not numeros:
        print('Nenhum valor informado.')
        return
    print(f'Valores: {numeros} ({len(numeros)} no total)')
    print(f'O maior e {max(numeros)}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()