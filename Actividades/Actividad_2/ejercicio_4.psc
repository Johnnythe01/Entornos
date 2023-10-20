Algoritmo ejercicio_4
	intentos <- 3
	acertado <- Falso
	Mientras intentos > 0 Y acertado = Falso
		Escribir "Introduzca contraseña"
		Leer pwd
		si pwd = "eureka"
			acertado <- Verdadero
		FinSi
		intentos <- intentos - 1
	FinMientras
	si acertado = Falso
		Escribir "Has agotado los 3 intentos."
	SiNo
		Escribir "Contraseña correcta, bienvenido."
	FinSi
FinAlgoritmo