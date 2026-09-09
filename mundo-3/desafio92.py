# EX092 - Cadastro de trabalhador (minha versao)
from datetime import date

t = {}
t['nome'] = input('Nome: ').strip()
ano_nasc = int(input('Ano de nascimento: '))
t['idade'] = date.today().year - ano_nasc
ctps = int(input('Carteira de trabalho (0 = nao tem): '))
if ctps != 0:
    t['ctps'] = ctps
    ano_contrat = int(input('Ano de contratacao: '))
    t['salario'] = float(input('Salario: R$'))
    t['aposenta_com'] = (ano_contrat + 35) - ano_nasc
print('-=' * 25)
for chave, valor in t.items():
    print(f'{chave}: {valor}')