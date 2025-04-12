@echo on
REM Check if a module name is provided
if [%1]==[] (
    echo Please provide a pip module to install.
    exit /b 1
)

REM Upgrade pip
python -m pip install --upgrade pip

REM Install the specified module
pip install %1

REM Freeze the installed packages into requirements.txt
pip freeze > requirements.txt