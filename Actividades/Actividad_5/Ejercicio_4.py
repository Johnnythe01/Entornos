intentos = 3
acertado = False

while intentos > 0 and not acertado:
    pwd = input("Introduzca la contraseña ")
    if pwd == "eureka":
        acertado = True
    intentos -= 1

if not acertado:
    print("Has agotado los 3 intentos.")
else:
    print("Contraseña correcta, bienvenido.")