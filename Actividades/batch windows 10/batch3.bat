@echo off

:menu
cls
echo Menu:
echo 1. Show computer name
echo 2. Show current user
echo 3. Show current date and time
echo 4. Exit

set /p choice=Enter your choice: 

if "%choice%"=="1" goto showComputerName
if "%choice%"=="2" goto showCurrentUser
if "%choice%"=="3" goto showDateTime
if "%choice%"=="4" goto :eof

echo Invalid choice. Please try again.
pause
goto menu

:showComputerName
echo Computer Name: %computername%
pause
goto menu

:showCurrentUser
echo Current User: %username%
pause
goto menu

:showDateTime
echo Current Date and Time: %date% %time%
pause
goto menu