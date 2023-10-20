A = float(input("Introduzca un valor para A: "))
B = float(input("Introduzca un valor para B: "))
C = float(input("Introduzca un valor para C: "))

if A > B and A > C:
    print("El primer valor es mayor")
elif B > A and B > C:
    print("El segundo valor es mayor")
else:
    print("El tercer valor es mayor")