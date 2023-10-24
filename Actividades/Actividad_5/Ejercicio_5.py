print("Escriba un numero para calcular su factorial")
numero = int(input())
if numero < 0:
    print("no es posible calcular factorial de un numero negativo.")
else:
    factorial = 1
    for i in range (1, numero +1):
        factorial *= i
print("El factorial de ", numero, " es ", factorial)