Algoritmo ejercicio_4
	intentos <- 3
	acertado <- Falso
	Mientras intentos > 0 Y acertado = Falso
<<<<<<< HEAD
		Escribir "Introduzca contraseña"
		Leer pwd
		si pwd = "eureka"
			acertado <- Verdadero
=======
		Leer pwd
		si pwd = "eureka"
			acertado = Verdadero
>>>>>>> fa108ad5b6c07f8926a2a1687f4490e6fcd07fe8
		FinSi
		intentos <- intentos - 1
	FinMientras
	si acertado = Falso
<<<<<<< HEAD
		Escribir "Has agotado los 3 intentos."
=======
		Escribir "Has agotado tus intentos."
>>>>>>> fa108ad5b6c07f8926a2a1687f4490e6fcd07fe8
	SiNo
		Escribir "Contraseña correcta, bienvenido."
	FinSi
FinAlgoritmo