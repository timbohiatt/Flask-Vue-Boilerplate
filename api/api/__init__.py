
import logging
#from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from celery import Celery
#from flask_bootstrap import Bootstrap
#from flask_moment import Moment
#from flask_babel import Babel, lazy_gettext as _l
#from elasticsearch import Elasticsearch
#from redis import Redis
#import rq
from config import Config



db = SQLAlchemy()
mail = Mail()

ma = Marshmallow()
migrate = Migrate()

login = LoginManager()
login.login_view = 'auth.login'
#login.login_message = _l('Please log in to access this page.')
login.login_message = ('Please log in to access this page.')
celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)



#bootstrap = Bootstrap()
#moment = Moment()
#babel = Babel()


def create_app(config_class=Config):
	app = Flask(__name__)

	
	
	CORS(app)
	
	app.config.from_object(config_class)
	db.init_app(app)
	mail.init_app(app)

	ma = Marshmallow(app)

	celery.conf.update(app.config)

	migrate.init_app(app, db)
	login.init_app(app)

	logging.basicConfig(level=app.config['LOGLEVEL'])

	#Import and Register Core Settings API Elements into the Application
	from api.v1_api import bp as v1_api
	app.register_blueprint(v1_api, url_prefix='/v1/')

	from api.v1_users import bp as v1_users
	app.register_blueprint(v1_users, url_prefix='/v1/users')

	@app.route('/v1/healthcheck', methods=['GET'])
	def v1_healthcheck():
		return {"message": "All Good!, Welcome Home!"}



	@app.after_request
	def after_request(response):
		response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
		response.headers["Expires"] = 0
		response.headers["Pragma"] = "no-cache"
		return response


	# temporary route
	@app.route('/')
	def router_health_check():
		return 'Health Check!'

	return app

#Return All Model Files
from api import models
