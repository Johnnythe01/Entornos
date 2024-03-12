@echo off
cls
echo Welcome to the Addition Program
echo.

REM Prompting the user to enter the first number
set /p num1=Enter the first number: 

REM Prompting the user to enter the second number
set /p num2=Enter the second number: 

REM Performing addition
set /a result=num1+num2

REM Printing the result
echo.
echo The result of %num1% + %num2% is %result%.
echo.
pause