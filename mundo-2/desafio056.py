# EX056 - Analisador completo (minha versao com lista de dicionarios)
pessoas = []
for i in range(4):
    print(f'--- {i + 1}a pessoa ---')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    pessoas.append({'nome': nome, 'idade': idade, 'sexo': sexo})

media = sum(p['idade'] for p in pessoas) / len(pessoas)
homem_velho = max((p for p in pessoas if p['sexo'] == 'M'), key=lambda p: p['idade'], default=None)
mulheres_jovens = [p['nome'] for p in pessoas if p['sexo'] == 'F' and p['idade'] < 20]

print(f'\nMedia de idade do grupo: {media:.1f} anos')
if homem_velho:
    print(f"Homem mais velho: {homem_velho['nome']} ({homem_velho['idade']} anos)")
else:
    print('Nenhum homem foi cadastrado.')
print(f"Mulheres com menos de 20 anos: {len(mulheres_jovens)}")