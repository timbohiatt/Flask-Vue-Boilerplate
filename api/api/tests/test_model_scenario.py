# tests/test_basic.py

import unittest

from .base import BaseTestCase
from ..models import db, Scenario


class FlaskTestCase(BaseTestCase):

	# Ensure that Flask was set up correctly
	def test_model_scenario_create(self):
		#==================================================
		# Define Test Data
		#==================================================
		tdScenarioName = "This is A Scenario"
		tdScenarioDescription = "I would like to write a long description."
		#==================================================

		#Create User DB Object
		tScen = Scenario(    
			Name = tdScenarioName,
			Description = tdScenarioDescription
		)
		#Add User Object to DB.
		db.session.add(tScen)
		db.session.commit()

		#Run Field Checks. Ensure Fields are Being Stored against the DB Correctly.
		self.assertEqual(tScen.Name, tdScenarioName)
		self.assertEqual(tScen.Description, tdScenarioDescription)


        #Get Scenario from DB Using ID
		vScen = Scenario.get_active_by_id(vID=1)
		#Check Returned Object == Scenario and Scenario ID == 1
		self.assertEqual(type(vScen), Scenario)
		self.assertEqual(vScen.ID, 1)
	
		vScen.set_inactive()
		db.session.commit()

		#Get Scenario from DB Using ID
		vScen = Scenario.get_active_by_id(vID=1)
		#Check Returned Object == Scenario and Scenario ID == 1
		self.assertEqual(type(vScen), type(None))
		self.assertEqual(vScen, None)