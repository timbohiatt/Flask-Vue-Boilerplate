import os, click, unittest
from config import Config
from api.models import db



def register(app):

	@app.cli.command("db-destroy")
	#@click.argument("name")
	def run_tests(): 
		"""Destroys the MySQL Database for compelte rebuild"""
		import pymysql.cursors
		connection = pymysql.connect(host=app.config['DB_HOST'],
                             user=app.config['DB_USER'],
                             password=app.config['DB_PASS'],
                             db=app.config['DB_NAME'],
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
		try:
			with connection.cursor() as cursor:
				# Create a new record
				sql = "SET FOREIGN_KEY_CHECKS=0;"
				cursor.execute(sql)
				sql = "DROP DATABASE IF EXISTS {}".format(app.config['DB_NAME'])
				cursor.execute(sql)
				sql = "CREATE DATABASE  {}".format(app.config['DB_NAME'])
				cursor.execute(sql)
				sql = "SET FOREIGN_KEY_CHECKS=1;"
				cursor.execute(sql)
			connection.commit()
		finally:
			connection.close()
		return

	@app.cli.command("run-unit-tests")
	#@click.argument("name")
	def run_tests(): 
		"""Runs the unit tests without coverage."""
		tests = unittest.TestLoader().discover("api.tests")
		unittest.TextTestRunner(verbosity=2).run(tests)
		return



	@app.cli.command("load-init-data")
	#@click.argument("name")
	def load_init_data():  
		return
		