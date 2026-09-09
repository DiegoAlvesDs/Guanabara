# EX102 - Fatorial recursivo (minha versao)
def fatorial(n, mostrar=False):
    """Calcula o fatorial de n. Se mostrar=True, exibe a conta."""
    if n <= 1:
        return 1
    if mostrar:
        print(f'{n} x ', end='')
    return n * fatorial(n - 1, mostrar)


n = int(input('Fatorial de: '))
ver = input('Mostrar a conta? [S/N] ').strip().upper() == 'S'
if ver:
    print('1 = ', end='')
print(fatorial(n, mostrar=ver))