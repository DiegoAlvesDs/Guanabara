from math import sqrt

print("=" * 50)
print("      DOBRO, TRIPLO E RAIZ QUADRADA")
print("=" * 50)

numero = float(input("Digite um número: "))

dobro = numero * 2
triplo = numero * 3
raiz_quadrada = sqrt(numero)

print("\nRESULTADOS")
print("-" * 50)
print(f"Número informado : {numero}")
print(f"Dobro            : {dobro}")
print(f"Triplo           : {triplo}")
print(f"Raiz quadrada    : {raiz_quadrada:.2f}")
print("-" * 50)

print("\nPrograma finalizado com sucesso!")