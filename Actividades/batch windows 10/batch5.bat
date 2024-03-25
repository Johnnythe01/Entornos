@echo off
title L7A7 - Hard Drive Administrative Tool

:start
cls
echo L7A7 - Hard Drive Administrative Tool
echo ------------------------------------
echo [1] Delete Internet Cookies
echo [2] Delete Temporary Internet Files
echo [3] Disk Cleanup
echo [4] Disk Defragment
echo [5] Exit

set /p choice=Enter your choice: 

if "%choice%"=="1" goto delete_cookies
if "%choice%"=="2" goto delete_temp_files
if "%choice%"=="3" goto disk_cleanup
if "%choice%"=="4" goto disk_defrag
if "%choice%"=="5" goto end

:delete_cookies
echo Deleting Internet Cookies...
del /q /s "%userprofile%\AppData\Local\Microsoft\Windows\INetCookies\*"
echo Internet Cookies deleted.
pause
goto start

:delete_temp_files
echo Deleting Temporary Internet Files...
del /q /s "%userprofile%\AppData\Local\Microsoft\Windows\INetCache\*"
echo Temporary Internet Files deleted.
pause
goto start

:disk_cleanup
echo Running Disk Cleanup...
rd /s /q "%temp%"
rd /s /q "%tmp%"
rd /s /q "c:\temp"
rd /s /q "c:\tmp"
echo Disk Cleanup completed.
pause
goto start

:disk_defrag
echo Running Disk Defragment...
defrag -c -v
echo Disk Defragment completed.
pause
goto start

:end
echo Exiting...
pause
exit