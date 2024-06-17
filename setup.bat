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

if not exist .env (
    echo Creando archivo .env...
    echo SECRET_KEY=your-secret-key > .env
    echo >> .env
    echo DB_TYPE=mysql >> .env
    echo SQLITE_URL=sqlite:///path-to-your-db.db >> .env
    echo >> .env
    echo MYSQL_USER=your_db_user >> .env
    echo MYSQL_PASSWORD=your_db_pdw >> .env
    echo MYSQL_HOST=db_host >> .env
    echo MYSQL_DB=db_name >> .env
)

echo Configuración completada.