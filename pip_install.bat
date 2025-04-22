@echo on
if [%1]==[] (
    echo Please provide a pip module to install.
    exit /b 1
)

python -m pip install --upgrade pip

pip install %1

pip freeze > requirements.txt