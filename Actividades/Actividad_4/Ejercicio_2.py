A = float(input("Introduzca un valor para A: "))
B = float(input("Introduzca un valor para B: "))

Resultado = A + B
print("El resultado de la suma es:", Resultado)

Resultado = A - B
print("El resultado de la resta es:", Resultado)

Resultado = A * B
print("El resultado de la multiplicación es:", Resultado)

if B != 0:
    Resultado = A / B
    print("El resultado de la división es:", Resultado)
else:
    print("No se puede dividir por cero.") 