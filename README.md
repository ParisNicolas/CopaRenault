# CopaRenault
Un sitio web para promocionar y administrar la copa renault 2025
 
## Instalacion
#### Ejecuta setup.bat o sigue las siguientes instrucciones:

Clona el repositorio.
```bash
git clone https://github.com/ParisNicolas/CopaRenault.git
cd CopaRenault
```

Crea el entorno virtual y activalo.
```bash
python -m venv .venv
.venv/Scripts/activate
```
Instala las dependencias:
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Bcrypt
- Flask-Login
- Flask-WTF
- Flask-Caching
- email_validator
- mysql-connector-python
- python-decouple
```bash
pip install -r requirements.txt
```

Configura las variables de entorno (se guardan en la sesion de la terminal).
```bash
set SECRET_KEY=your-secret-key
set DATABASE_URL=your-db-url
set APP_SETTINGS=config.DevelopmentConfig
set FLASK_APP=flaskr
set FLASK_DEBUG=1
set RECAPTCHA_PUBLIC_KEY=...
set RECAPTCHA_PRIVATE_KEY=...
```
- **SECRET_KEY:** Clave secreta que se usara para cifrar las sessiones y tokens
- **DATABASE_URL:** Url completa de la base de datos (CleverCloud u otra)
- **APP_SETTINGS:** Preset de configuracion 
   - *config.DevelopmentConfig*
   - *config.TestingConfig*
   - *config.ProductionConfig*
- **FLASK_APP:** Nombre del modulo de la aplicacion **(NO TOCAR)**
- **FLASK_DEBUG:** Activar o desactivar debug_mode (1 o 0), sobrescribe *APP_SETTINGS*
- **RECAPTCHA_PUBLIC_KEY:** Clave publica de ReCaptcha
- **RECAPTCHA_PRIVATE_KEY:** Clave privada de ReCaptcha

Corre el codigo.
```bash
flask run
```

## WorkFlow (cada vez que desarrollas)

 1. Activa el entorno virtual
```bash
.venv/Scripts/activate
```
 2. Configura las variables de entorno
```bash
call .env.bat
```
 3. Corre la aplicacion con: `flask run`
 4. Haz los cambios necesarios al codigo
 5. En caso de que quieras crear o eliminar usuarios:
```bash
flask create_user <email> <password>
flask remove_user <email>
```
 6. En caso de que modifiques los modelos:
```bash
flask db migrate -m "Campo edad añadido"
flask db upgrade
```
 7. Guarda los cambios:
```bash
git add *
git commit -m "Nuevo apartado, lista de tareas"
git push
```

## Funcionalidades
Esta aplicacion fue desarrollada de la manera mas estructurada y modular posible para que se de un buen comienzo y evitar cambios a la estructura de todo el codigo. Para ello se hizo una investigacion exaustiva de las mejores practicas en la creacion de proyectos con flask. Eso no quiere decir que sea la mejor manera para todo, de hecho se podria agilizar el proceso de la configuracion de las variables de entorno con dotenv, pero preferi intentarlo con configuracion directa y jugar con scripts batch.

Contiene varias funcionalidades y extensiones de flask que "facilitan" el codigo en diversos aspectos, entre ellos el cacheo de memoria (Flask-Caching), la generacion de formularios (Flask-WTF), la autorizacion de usuarios (Flask-Login), la encriptacion de contraseñas (Flask-Bcrypt), las consultas a la BD (Flask-SQLAlchemy), el manejo de versiones de la BD (Flask-Migrate), entre otros modulos integrados como *click* para comandos de consola personalizados.

La aplicacion tiene 4 rutas principales (actualmente solo hay 3 activas):
- **/ (home)**: Presentacion de la copa, informacion relevante, links a los formularios de inscripcion, sponsors, contacto.
- **/inscripcion**: Formulario de inscripcion
- **/info**: Informacion importante, como el menu, el mapa del colegio, normativas, etc.
- **/partidos**: Tabla de horarios de partidos, junto con los equipos participantes y posteriormente su resultado
- **/admin**: Panel de administracion protegido con permisos (actualmente solo login)


# Datos del Proyecto
**Nombre del Proyecto:** CopaRenault
**Alumno:** París Nicolas
**Fecha de Inicio del Proyecto:** 14/6/22
**Fecha de Finalización del Proyecto:** *****


## Descripcion general:
La **Copa Renault** es un evento polideportivo que se lleva a cabo todos los años dentro del predio del Instituto Tecnico Renaul, donde compiten colegios de toda cordoba en distintas categorias separadas por edad, ya sea para jugar *futbol, basket o voley*.
Se requiere proporcionar un mecanismo eficaz para el registro de participantes, asi como tambien gestionar los marcadores. Por esto se a decido que es de gran conveniencia contar con una interfaz web que proporcione al personal una manera de lidiar con la gestion de los partidos, que ademas proporcione un solido registro para que los participantes puedan estar al tanto del estado de sus rivales o compañeros.
Ademas con esta aplicacion se busca promocionar el evento con una UI vistosa, brindando informacion clave como sponsors, menu de comida, instrucciones, mapa del colegio y durante el evento, proporcionar una tabla de horarios de los partidos (junto con el marcador en vivo si es posible, estado --> jugando/en espera), con filtrado por colegios, horario o equipos.
Se espera que la aplicacion cuente con un formulario de inscripcion, para que el encargado de cada colegio pueda anotar a los equipos correspondientes. El registro de formularios falsos puede ser un problema, asi como tambien la administracion de los pagos.
Queda fuera del alcance de este proyecto la gestion de personal para la copa renault, esto debe ser administrado manualmente por el encargado.

## Requisitos del Proyecto:

 - Inscripcion de los participantes
- Informe a los encargados de su equipo (horarios, pagado, reglas) por mail o numero
 - Visualizacion de horarios y marcadores de cada equipo
 - Gestion de usuarios para acceso al panel de administracion (logueo por pwd o OAuth2)
 - Añadir manualmente usuarios (sin apartado de registro)
 - Anotacion de puntaje
 - Estructuracion automatica y manual de canchas/horarios para cada equipo
 - Solucion de posibles imprevistos (malas anotaciones, cancelaciones, avisos, retraso de tiempo, etc)
 - Registro de logs

## Diseño del Sistema:

### Frontend
El frontend es la parte de la aplicación con la que interactúan los usuarios. En esta estructura, el frontend está compuesto por las plantillas HTML y los archivos estáticos.

1. **Plantillas HTML**: Las plantillas HTML se encuentran en las siguientes carpetas:
   - `flaskr/admin/templates/admin/`
     - `base.html`
     - `login.html`
     - `navigation.html`
   - `flaskr/main/templates/main/`
     - `base.html`
     - `home.html`
     - `info.html`
     - `inscribirse.html`
     - `navigation.html`
   Estas plantillas definen la estructura de las páginas web y utilizan la sintaxis de Jinja2 para incluir datos dinámicos.

2. **Archivos estáticos**:
   - `flaskr/static/`: Aquí es donde se guardarían archivos estáticos como CSS, JavaScript e imágenes que son necesarios para el diseño y comportamiento del frontend.

### Backend
El backend se encarga de la lógica de la aplicación, la gestión de la base de datos y la manipulación de datos. Está compuesto por los siguientes archivos y carpetas:

1. **Módulos de Flask**:
   - `flaskr/admin/`:
     - `__init__.py`: Inicializa el módulo admin.
     - `forms.py`: Contiene los formularios utilizados en el módulo admin.
     - `routes.py`: Define las rutas y vistas para las páginas admin.
   - `flaskr/main/`:
     - `__init__.py`: Inicializa el módulo main.
     - `routes.py`: Define las rutas y vistas para las páginas principales de la aplicación.

2. **Modelos**:
   - `flaskr/models.py`: Define los modelos de datos que se utilizan para interactuar con la base de datos.

3. **Configuración**:
   - `config.py`: Contiene la configuración de la aplicación, como configuraciones de la base de datos y otras variables de configuración.

4. **Archivos de inicialización**:
   - `flaskr/__init__.py`: Inicializa la aplicación Flask principal y registra los blueprints para los módulos admin y main.

### Servidor
El servidor es responsable de servir la aplicación a los usuarios. En este caso, el servidor está configurado para ejecutar una aplicación Flask. Los archivos relevantes incluyen:

1. **Entorno virtual**:
   - `.venv/`: El entorno virtual donde se instalan las dependencias de la aplicación para asegurar que se utilizan las versiones correctas de los paquetes necesarios.

2. **Archivos de inicio**:
   - `setup.bat`: Un script para configurar el entorno y ejecutar la aplicación.
   - `.env.bat`: Un archivo que contiene variables de entorno necesarias para la configuración de la aplicación.

3. **Requisitos**:
   - `requirements.txt`: Lista de paquetes y dependencias que deben instalarse en el entorno virtual para que la aplicación funcione correctamente.

### Base de Datos
La base de datos almacena toda la información persistente de la aplicación. La configuración y las migraciones de la base de datos están gestionadas por los siguientes archivos y carpetas:

1. **Migraciones**:
   - `migrations/`: Contiene archivos de migración que gestionan los cambios en la estructura de la base de datos a lo largo del tiempo, generalmente utilizando una herramienta como Flask-Migrate.

2. **Instancia**:
   - `instance/`: Esta carpeta puede contener el archivo de la base de datos SQLite u otros archivos específicos de la instancia de la aplicación.

## Bocetos
![boceto1](https://drive.google.com/file/d/1pco3pPpwroybuFsIGzMYlj5-PyDCqP3V/view?usp=drive_link)
![boceto2](https://drive.google.com/file/d/1pgOaFuFCPDLDODIuOkyxRpCTXCUiIF9Q/view?usp=drive_link)
![adminpanel](https://drive.google.com/file/d/1pgjhN4kTdPPro97aCudPea894cC2feli/view?usp=drive_link)
![home](https://drive.google.com/file/d/1pmEyeF6lpes7ai7S8oQmfOWS8stZiuBK/view?usp=drive_link)
![Base de datos](https://drive.google.com/file/d/1prql-lMsqHB1PIAR3E44ptAshUGjpQCw/view?usp=drive_link)