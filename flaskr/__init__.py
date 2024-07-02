import os

import click
from decouple import config
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_caching import Cache

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

# SimpleCache para pruebas, tal vez RedisCache u otros en producción
cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    
    
    """Config manualy or using the get_config to get it from env variables"""
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object(config("APP_SETTINGS"))
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    #Basic test route
    @app.route("/hello")
    def hello():
        return 'HEllo'
    

    """Initialize"""
    login_manager.init_app(app)
    bcrypt.init_app(app)
    db.init_app(app)
    migrate = Migrate(app, db)
    cache.init_app(app)
    #from . import models #ES NECESARIO ESTA LINEA PARA QUE MIGRATE TOME LOS MODELOS???

    """Blueprints"""
    from flaskr.main.routes import main_bp
    from flaskr.admin.routes import admin as admin_blueprint
    app.register_blueprint(main_bp)
    app.register_blueprint(admin_blueprint)
    

    """Obtener usuario actual para cada solicitud"""
    from flaskr.models import Usuario
    login_manager.login_view = "admin.login"
    login_manager.login_message_category = "danger"
    @login_manager.user_loader
    @cache.cached(timeout=500, key_prefix='user_')
    def load_user(user_id):
        return Usuario.query.get(int(user_id)) #.filter(Usuario.id == int(user_id)).first()
    
    """Comandos"""
    @app.cli.command("register-user")
    @click.argument("email")
    @click.argument("password")
    def create_user(email, password):
        """Create a new user with USERNAME, EMAIL, and PASSWORD."""
        new_user = Usuario(email, password)
        db.session.add(new_user)
        db.session.commit()
        click.echo(f"User {email} created successfully!")

    @app.cli.command("remove-user")
    @click.argument("email")
    def remove_user(email):
        user = Usuario.query.filter_by(email=email).first()
        db.session.delete(user)
        db.session.commit()
        click.echo(f"User {email} removed successfully!")

    return app