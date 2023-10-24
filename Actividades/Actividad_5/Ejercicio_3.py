dia = int(input("Introduzca el dia"))
mes = int(input("Introduzca el mes"))
if (mes > 1 and mes < 12):
    if (dia >= 1 and dia <= 31):
        print("La fecha es valida.")
    else:
        print("El dia ingresado no es valido.")
