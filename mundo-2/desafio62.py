# EX062 - Super PA v3.0 (minha versao)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
mostrados = 10
print(list(range(primeiro, primeiro + mostrados * razao, razao)))
while True:
    extra = int(input('Quantos termos a mais? (0 para parar) '))
    if extra == 0:
        break
    inicio = primeiro + mostrados * razao
    print(list(range(inicio, inicio + extra * razao, razao)))
    mostrados += extra
print(f'PA finalizada com {mostrados} termos.')