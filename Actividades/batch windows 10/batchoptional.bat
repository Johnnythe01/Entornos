Exercise 2. Batch

1. Copy files from one folder to another:
a. Suppose you have a folder called “Documents” with some important files.
b. We will create a folder called “Backup” and copy all the files from “Documents” to this folder for backup.
c. Use variables to define absolute paths. 
eg: set sourceFolder=C:\Ruta\Hacia\Documentos

2. File existence check:
a. Before copying the files, we will check if the “Documents” folder exists.
b. If it does not exist, we will display an error message.

3. Using if exists and xcopy commands:
a. We will use the if exist command to verify the existence of the “Documents” folder.
b. Then, we will use xcopy to copy the files from “Documents” to “Backup”.


@echo off
setlocal

REM Define source and destination folders
set "sourceFolder=C:\Path\To\Documents"
set "backupFolder=C:\Path\To\Backup"

REM Check if source folder exists
if not exist "%sourceFolder%" (
    echo Source folder does not exist.
    goto :EOF
)

REM Create backup folder if it doesn't exist
if not exist "%backupFolder%" (
    mkdir "%backupFolder%"
)

REM Copy files from source to backup
xcopy "%sourceFolder%\*" "%backupFolder%\" /E /Y

echo Files copied successfully.

:end
endlocal