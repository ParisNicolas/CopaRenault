@echo off

echo Creating a virtual environment...
py 3 -m venv .venv

if errorlevel 1 (
    echo Failed to create a virtual environment.
    exit /b 1
)
echo Virtual environment created successfully.


echo Activating virtual environment...
call .venv\Scripts\activate
if errorlevel 1 (
    echo Failed to activate virtual environment.
    exit /b 1
)
echo Virtual environment activated successfully.


echo Installing requirements...
pip install -r requirements.txt
if errorlevel 1 (
    echo Failed to install requirements.
    exit /b 1
)
echo Requirements installed successfully.


echo Setting up enviroment variables...
set /p url= Your database url:
set /p secret= Your secret:

if not exist .env.bat (
    echo Creando archivo .env.bat ...
    if "%secret%"=="" (
        echo set SECRET_KEY=secretkey123 > .env.bat
    ) else (
        echo set SECRET_KEY=%secret% > .env.bat
    )
    echo set DEBUG=True >> .env
    echo set APP_SETTINGS=config.DevelopmentConfig >> .env.bat
    if "%url%"=="" (
        echo set DATABASE_URL=sqlite:///path-to-your-db.db >> .env.bat
    ) else (
        echo set DATABASE_URL=%url% >> .env.bat
    )
    echo set FLASK_APP=flaskr >> .env.bat
    echo set FLASK_DEBUG=1 >> .env.bat
    echo set RECAPTCHA_PUBLIC_KEY=... >> .env.bat
    echo set RECAPTCHA_PRIVATE_KEY=... >> .env.bat
)
call .env.bat

echo Configuración completada.
pause