# EX105 - Boletim em dicionario (minha versao com statistics)
from statistics import mean


def boletim(*notas, situacao=False):
    resultado = {
        'total': len(notas),
        'maior': max(notas),
        'menor': min(notas),
        'media': mean(notas),
    }
    if situacao:
        resultado['situacao'] = 'BOA' if resultado['media'] >= 7 else ('RAZOAVEL' if resultado['media'] >= 5 else 'RUIM')
    return resultado


resp = boletim(8.5, 6.0, 9.5, 7.0, situacao=True)
for chave, valor in resp.items():
    print(f'{chave}: {valor}')