# comentario
Write-Output "hola mundo"

ls

Get-ChildItem

$variable = "mi contenido"

Write-Output $variable

# condicionales
$num = 10
if ($num -eq 10){
    Write-Output "El número es 10"
}elseif ($num -gt 44) {
    Write-Output "El número es mayor que 44"
}else{
    Write-Output "No lo se"
}
# bucles for
# for each
$lista = "rojo", "amarillo", "verde"
foreach ($color in $lista) {
    WriteOutput "El color es $color"
}
# for (estilo C) -- for normal
for ($i = 0; $i -lt 8; $i++){
    Write-Output $i
}
# bucles while
$contador = 0
while ($contador -le 12){
    # hacemos algo
    $contador ++
}
# leer por teclado (scanner en java)
$num = Read-Host "¿Cuantos años tienes?"
Write-Output "Tienes $num años"
Get-Command
Read-Host "¿Quieres salir?"