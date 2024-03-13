@echo off

set "fileName=myname.txt"
set "fullName=Your Full Name"

rem Check if the file exists
if exist "%fileName%" (
    echo %fullName% >> "%fileName%"
    echo Appended your full name to %fileName%.
) else (
    echo %fullName% > "%fileName%"
    echo Created %fileName% and wrote your full name.
)

pause