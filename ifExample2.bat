@echo off

rem Step 1: Check if the folder 'new_folder' exists
if exist "new_folder" (
    rem Step 2: If 'new_folder' exists, create 'if_folder'
    mkdir if_folder
    echo New folder 'if_folder' created.
) else (
    rem Step 3: If 'new_folder' doesn't exist, create 'hyperionDev'
    mkdir hyperionDev
    echo New folder 'hyperionDev' created.
)

rem Step 4: Check if 'if_folder' exists
if exist "if_folder" (
    rem Step 5: If 'if_folder' exists, create 'hyperionDev'
    mkdir hyperionDev
    echo New folder 'hyperionDev' created.
) else (
    rem Step 6: If 'if_folder' doesn't exist, create 'new-projects'
    mkdir new-projects
    echo New folder 'new-projects' created.
)

pause
