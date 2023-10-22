import math

A = float(input("Introduzca un valor: "))

if A <= 0:
    print("Error: El número debe ser mayor que 0.")
else:
    cuadrado = A * A
    print(f"El cuadrado de {A} es: {cuadrado}")
    raiz_cuadrada = math.sqrt(A)
    print(f"La raíz cuadrada de {A} es: {raiz_cuadrada}") 