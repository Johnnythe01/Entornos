Algoritmo ejercicio_2
	Escribir "Introduzca primer n�mero"
	Leer A
	Escribir "Introduzca segundo n�mero"
	Leer B
	Si A > B Entonces
		mayor <- A
		menor <- B
	SiNo
		mayor <- B
		menor <- A
	FinSi
	resultado <- mayor / menor
	Escribir "La divisi�n del mayor entre el menor es: " resultado
FinAlgoritmo