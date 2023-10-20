A = float(input("Introduzca un valor para A: "))
B = float(input("Introduzca un valor para B: "))
C = float(input("Introduzca un valor para C: "))

if A < 0:
    resultado = A * B * C
else:
    resultado = A + B + C

print("El resultado es:", resultado)