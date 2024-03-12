@echo off
set /p num1=Enter the first number: 
set /p num2=Enter the second number: 

set /a result=num1+num2

echo The result of adding %num1% and %num2% is: %result%
pausen 