A = float(input("Introduzca el primer valor"))
B = float(input("Introduzca el segundo valor"))
mayor = max(A,B)
menor = min(A,B)

if menor == 0:
    print ("No se puede dividir por 0.")
else:
    resultado = mayor / menor
    print(f"La division de {mayor} entre {menor} es igual a {resultado}")