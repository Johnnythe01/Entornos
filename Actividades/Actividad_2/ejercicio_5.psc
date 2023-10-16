Algoritmo ejercicio_5
	Escribir "Escriba un numero para calcular su factorial"
	Leer numero
	Si numero <0
		Escribir "no es posible calcular factorial de un número negativo."
	SiNo
		factorial <- 1
		Para i <- 1 Hasta numero
			factorial <- factorial * i
		FinPara
		Escribir "El factorial de ", numero, " es ", factorial
	FinSi
FinAlgoritmo