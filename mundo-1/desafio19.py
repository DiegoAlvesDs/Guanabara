from math import radians, sin, cos, tan

angulo = float(input("Digite um ângulo: "))

radianos = radians(angulo)

seno = sin(radianos)
cosseno = cos(radianos)
tangente = tan(radianos)

print(f"\nÂngulo informado: {angulo}°")
print(f"Seno     : {seno:.2f}")
print(f"Cosseno  : {cosseno:.2f}")
print(f"Tangente : {tangente:.2f}")