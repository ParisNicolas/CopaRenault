import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class SQLiteConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLITE_URL') or 'sqlite:///app.db'

class MySQLConfig(Config):
    MYSQL_USER = os.environ.get('MYSQL_USER')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
    MYSQL_HOST = os.environ.get('MYSQL_HOST')
    MYSQL_DB = os.environ.get('MYSQL_DB')

    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}'

def get_config():
    db_type = os.environ.get('DB_TYPE', 'mysql').lower()
    if db_type == 'mysql':
        return MySQLConfig
    else:
        return SQLiteConfig
