@echo off

echo Possible colors:
echo 0 = Black
echo 1 = Blue
echo 2 = Green
echo 3 = Aqua
echo 4 = Red
echo 5 = Purple
echo 6 = Yellow
echo 7 = White
echo 8 = Gray
echo 9 = Light Blue
echo A = Light Green
echo B = Light Aqua
echo C = Light Red
echo D = Light Purple
echo E = Light Yellow
echo F = Bright White

set /p bgColor=Enter background color (0-F): 

set /p fontColor=Enter font color (0-F): 

color %bgColor%%fontColor%