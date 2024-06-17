import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import get_config

db = SQLAlchemy()

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    
    
    """Config manualy or using the get_config to get it from env variables"""
    app.config.from_mapping(
        SECRET_KEY='dev'
    )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object(get_config())
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
    
    #Initialize the database, migration and models
    db.init_app(app)
    migrate = Migrate(app, db)
    from . import models

    """Blueprints"""
    from flaskr.main.routes import main_bp
    from flaskr.auth.routes import auth as auth_blueprint
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_blueprint)
    

    return app