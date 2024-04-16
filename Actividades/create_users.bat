@echo off
setlocal

set "username=John"
set "password=Johnnyboy"

net user %username% >nul 2>nul
if %errorlevel% equ 0 (
    echo User %username% already exists.
    goto :EOF
)

net user %username% %password% /add

echo User %username% created successfully.
