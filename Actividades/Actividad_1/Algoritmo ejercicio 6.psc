Algoritmo Calcular_cuadrado_y_raiz_cuadrada
    Escribir "Introduzca un valor"
    Leer A
    Si A<=0 Entonces
        Escribir "Error: El numero debe ser mayor que 0."
    Sino
        cuadrado <- A * A
        Escribir "El cuadrado de ", A, " es: ", cuadrado
        Escribir "La raiz cuadrada de ", A, " es: ", RC(A)
    Fin Si
Fin Algoritmo