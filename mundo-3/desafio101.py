# EX101 - Situacao do voto (minha versao)
from datetime import date


def voto(ano_nascimento):
    idade = date.today().year - ano_nascimento
    if idade < 16:
        return f'Com {idade} anos: nao pode votar.'
    if idade < 18 or idade > 70:
        return f'Com {idade} anos: voto opcional.'
    return f'Com {idade} anos: voto obrigatorio.'


print(voto(int(input('Ano de nascimento: '))))