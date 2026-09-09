print("=" * 40)
print("        TABUADA")
print("=" * 40)

numero = int(input("Digite um número inteiro: "))

print(f"\nTabuada do {numero}:")
print("-" * 40)

for i in range(1, 11):
    print(f"{numero} x {i:2} = {numero * i}")

print("=" * 40)