from random import choice

aluno1 = input("Nome do 1º aluno: ")
aluno2 = input("Nome do 2º aluno: ")
aluno3 = input("Nome do 3º aluno: ")
aluno4 = input("Nome do 4º aluno: ")

alunos = [aluno1, aluno2, aluno3, aluno4]

escolhido = choice(alunos)

print(f"\nO aluno escolhido para apagar o quadro foi: {escolhido}")