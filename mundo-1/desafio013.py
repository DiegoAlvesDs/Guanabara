salario = float(input("Digite o salário do funcionário: R$ "))

aumento = salario * 0.15
novo_salario = salario + aumento

print(f"\nSalário atual : R$ {salario:.2f}")
print(f"Aumento (15%) : R$ {aumento:.2f}")
print(f"Novo salário  : R$ {novo_salario:.2f}")