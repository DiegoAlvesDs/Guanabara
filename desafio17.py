from math import hypot

cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print(f"\nCateto oposto   : {cateto_oposto}")
print(f"Cateto adjacente: {cateto_adjacente}")
print(f"Hipotenusa      : {hipotenusa:.2f}")