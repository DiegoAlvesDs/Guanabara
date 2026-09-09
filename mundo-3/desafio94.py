# EX094 - Grupo de pessoas (minha versao)
galera = []
while True:
    p = {}
    p['nome'] = input('Nome: ').strip()
    while (sexo := input('Sexo [M/F]: ').strip().upper()) not in 'MF':
        print('Digite apenas M ou F!')
    p['sexo'] = sexo
    p['idade'] = int(input('Idade: '))
    galera.append(p)
    if input('Continuar? [S/N] ').strip().upper() == 'N':
        break

media = sum(p['idade'] for p in galera) / len(galera)
print(f'A) Total: {len(galera)} pessoa(s)')
print(f'B) Media de idade: {media:.1f} anos')
print(f'C) Mulheres: {", ".join(p["nome"] for p in galera if p["sexo"] == "F")}')
print('D) Acima da media:')
for p in galera:
    if p['idade'] > media:
        print(f'   {p["nome"]} ({p["idade"]} anos)')