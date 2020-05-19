import os, logging
from pathlib import Path	
from dotenv import load_dotenv
import binascii



basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    #APPLICATION CONSTANTS


    #APPLICATION VARIABLES
    APP_NAME =  os.environ.get('APP_NAME') or "LOCALHOST"
    APP_ENV = os.environ.get('APP_ENV') or "LCL"
    APP_PORT = os.environ.get('APP_PORT') or 5000

    #FLASK VARIABLES
    #FLASK_ENV = APP_ENV
    SERVER_NAME = os.environ.get('APP_SERVER_NAME') or 'LOCALHOST'+":"+APP_PORT
    SECRET_KEY = os.environ.get('SECRET_KEY') or binascii.hexlify(os.urandom(16))

    #CELERY VARIABLES
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL') or 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND') or 'redis://localhost:6379/0'

    
    #DEBUG VARIABLES
    LOGLEVEL = logging.DEBUG



    #DATABASE VARIABLES
    DB_INIT_DIR = "./db"
    DB_NAME = os.environ.get('DB_NAME') or (APP_NAME+"_"+APP_ENV)
    DB_USER = os.environ.get('DB_USER') or 'admin'
    DB_PASS = os.environ.get('DB_PASS') or 'password'
    DB_HOST = os.environ.get('DB_HOST') or 'localhost'
    DB_URI='mysql+pymysql://'+DB_USER+':'+DB_PASS+'@'+DB_HOST+'/'+DB_NAME

    #SQLALCHEMY VARIABLES
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = DB_URI or 'sqlite:///' + os.path.join(basedir, 'app.db')

   

    #Mail Server Setup:
    MAIL_SERVER=os.environ.get('MAIL_SERVER') or None
    MAIL_PORT=os.environ.get('MAIL_PORT') or 25
    #MAIL_USE_TLS=os.environ.get('MAIL_USE_TLS') or False
    MAIL_USE_SSL=os.environ.get('MAIL_USE_SSL') or False
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME') or None
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD') or None
    MAIL_SENDER=os.environ.get('MAIL_SENDER') or 'webmaster@'+APP_NAME+'.co.uk'
