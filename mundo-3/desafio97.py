# EX097 - Print especial (minha versao)
def escreva(texto):
    linha = len(texto) + 4
    print('~' * linha)
    print(f'{texto:^{linha}}')
    print('~' * linha)


escreva('Python Snake')
escreva('Diego Alves')
escreva('Meu proprio estilo de codigo')