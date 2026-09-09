# EX064 - Soma com flag (minha versao com operador morsa :=)
soma = cont = 0
while (num := int(input('Digite um valor (999 para parar): '))) != 999:
    soma += num
    cont += 1
print(f'Foram {cont} valores, somando {soma}.')