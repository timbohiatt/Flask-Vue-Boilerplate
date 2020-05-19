from flask_testing import TestCase


from api import create_app, db
from api.models import db
#from api.static.config import cnf_rules as DEFAULT_CNFRules



class BaseTestCase(TestCase):
	"""A base test case."""

	def create_app(self):
		app = create_app()
		app.config.from_object('config.Config')
		#Ensure the Tests Run in SQL Lite Local DB. 
		app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
		return app

	def setUp(self):
		db.create_all()

		db.session.commit()

	def tearDown(self):
		db.session.remove()
		db.drop_all()