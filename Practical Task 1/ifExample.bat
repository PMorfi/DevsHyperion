@echo off
set "folderToCheck=new_folder"

if exist "%folderToCheck%" (
    mkdir if_folder
    echo New folder 'if_folder' created.
) else (
    echo Folder '%folderToCheck%' does not exist.
)

pause
