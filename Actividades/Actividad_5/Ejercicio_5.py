print("Escriba un numero para calcular su factorial")
numero = int(input())
if numero < 0:
    print("no es posible calcular factorial de un numero negativo.")
else:
    factorial = 1
    for i in range (1, numero +1):
        factorial *= i
print("El factorial de ", numero, " es ", factorial)

# uf que codigo mas raro, no has pensado en usa ruby?¿ mira un ej : 
# class Mamifero 
#  def respira
#    puts "inhala y exhala"
#  end
# end
# class Gato<Mamifero
#  def habla
#    puts "Meow"
#  end
# end
# misifus = Gato.new
# misifus.respira
# misifus.habla