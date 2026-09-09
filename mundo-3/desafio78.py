# EX078 - Maior e menor na lista (minha versao)
valores = [int(input(f'Valor na posicao {i}: ')) for i in range(5)]
maior, menor = max(valores), min(valores)
print(f'Lista: {valores}')
print(f'Maior: {maior} nas posicoes {[i for i, v in enumerate(valores) if v == maior]}')
print(f'Menor: {menor} nas posicoes {[i for i, v in enumerate(valores) if v == menor]}')