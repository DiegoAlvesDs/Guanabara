# EX086 - Matriz 3x3 (minha versao)
matriz = [[int(input(f'Valor para [{l}, {c}]: ')) for c in range(3)] for l in range(3)]
print('-=' * 20)
for linha in matriz:
    print(' '.join(f'[{v:^5}]' for v in linha))