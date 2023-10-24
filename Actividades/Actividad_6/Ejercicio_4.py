contador = -1
num = 0
suma = 0
while num >= 0:
    suma += num
    contador += 1
    num = int(input("Introduzca un numero: "))

if contador > 0:
    media = suma / contador
    print(f"La media aritmetica de los numeros introducidos es {media}.")
else:
    print("No se introdujeron numeros validos para calcular la media.")