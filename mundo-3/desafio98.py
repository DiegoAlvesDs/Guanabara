# EX098 - Contador inteligente (minha versao)
from time import sleep


def contador(inicio, fim, passo):
    passo = abs(passo) or 1
    print(f'Contando de {inicio} ate {fim} (passo {passo}):')
    passo = passo if inicio < fim else -passo
    for i in range(inicio, fim + (1 if inicio < fim else -1), passo):
        print(i, end=' ', flush=True)
        sleep(0.3)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('Sua vez!')
contador(int(input('Inicio: ')), int(input('Fim: ')), int(input('Passo: ')))