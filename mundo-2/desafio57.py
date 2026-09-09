# EX057 - Validacao de sexo (minha versao)
while True:
    sexo = input('Informe seu sexo: [M/F] ').strip().upper()
    if sexo in ('M', 'F'):
        break
    print('Valor invalido! Tente de novo.')
print(f'Sexo {sexo} registrado com sucesso!')