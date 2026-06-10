print("=" * 40)
print("   CONVERSOR DE MEDIDAS")
print("=" * 40)

metros = float(input("Digite um valor em metros: "))

centimetros = metros * 100
milimetros = metros * 1000

print("\nResultado:")
print(f"{metros} m equivalem a:")
print(f"{centimetros} cm")
print(f"{milimetros} mm")

print("=" * 40)