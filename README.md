# CopaRenault
A website to promote the renault cup 2024

## Instalation

### Run setup.bat or follow these intructions

Clone the repository.
```bash
git clone https://github.com/ParisNicolas/CopaRenault.git
```

Create the virtual enviroment and activate it
```bash
py 3 -m venv .venv
.venv/Scripts/activate
```

Install the requirements:
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- mysql-connector-python
- dotenv-python

```bash
pip install -r requirements.txt
```

## Run the app
```bash
flask --app flaskr run --debug
```