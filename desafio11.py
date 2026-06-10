largura = float(input("Digite a largura da parede (m): "))
altura = float(input("Digite a altura da parede (m): "))

area = largura * altura
tinta = area / 2

print(f"\nLargura: {largura} m")
print(f"Altura: {altura} m")
print(f"Área da parede: {area:.2f} m²")
print(f"Quantidade de tinta necessária: {tinta:.2f} litros")