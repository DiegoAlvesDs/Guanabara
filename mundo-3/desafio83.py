# EX083 - Validando expressoes (minha versao com contador de profundidade)
expr = input('Digite a expressao: ')
nivel = 0
for letra in expr:
    if letra == '(':
        nivel += 1
    elif letra == ')':
        nivel -= 1
    if nivel < 0:  # fechou sem abrir
        break
print('Expressao valida!' if nivel == 0 else 'Expressao invalida!')