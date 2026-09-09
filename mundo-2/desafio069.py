# EX069 - Analise de grupo (minha versao)
pessoas = []
while True:
    idade = int(input('Idade: '))
    while (sexo := input('Sexo [M/F]: ').strip().upper()) not in ('M', 'F'):
        print('Digite apenas M ou F!')
    pessoas.append((idade, sexo))
    if input('Continuar? [S/N] ').strip().upper() == 'N':
        break

print(f'Maiores de 18 anos: {sum(1 for i, _ in pessoas if i >= 18)}')
print(f'Homens cadastrados: {sum(1 for _, s in pessoas if s == "M")}')
print(f'Mulheres com menos de 20: {sum(1 for i, s in pessoas if s == "F" and i < 20)}')