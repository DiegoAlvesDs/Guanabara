# EX090 - Dicionario do aluno (minha versao)
aluno = {}
aluno['nome'] = input('Nome do aluno: ').strip()
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
aluno['situacao'] = 'Aprovado' if aluno['media'] >= 7 else ('Recuperacao' if aluno['media'] >= 5 else 'Reprovado')
for chave, valor in aluno.items():
    print(f'{chave}: {valor}')