# EX096 - Area do terreno (minha versao)
def area(largura, comprimento):
    """Calcula e mostra a area de um terreno retangular."""
    return largura * comprimento


print('-' * 22)
print(' CONTROLE DE TERRENOS')
print('-' * 22)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
print(f'A area de {l}x{c} e de {area(l, c)}m2.')