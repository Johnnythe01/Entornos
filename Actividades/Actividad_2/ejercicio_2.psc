Algoritmo ejercicio_2
	Escribir "Introduzca primer número"
	Leer A
	Escribir "Introduzca segundo número"
	Leer B
	Si A > B Entonces
		mayor <- A
		menor <- B
	SiNo
		mayor <- B
		menor <- A
	FinSi
	resultado <- mayor / menor
	Escribir "La división del mayor entre el menor es: " resultado
FinAlgoritmo