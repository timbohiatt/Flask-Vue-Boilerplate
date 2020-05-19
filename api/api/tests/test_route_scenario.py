# tests/test_basic.py

import unittest

from .base import BaseTestCase
from ..models import db, Scenario


class FlaskTestCase(BaseTestCase):

	#  1# Ensure that Flask Route Scenario was Created correctly.
	#  2# Ensure you cann't submit duplicate Scenario Names to the DB
	def test_route_scenario_post_201(self):
		#==================================================
		# Define Test Data
		#==================================================
		tdPayload = {
			"scenario":{
				"name": "Test Name #22",
				"description": "Test Descriptions #1"
			}
		}
		#==================================================
		
		#Test to Ensure you can submit a Scenario
		response = self.client.post('/v1/scenario/', json=tdPayload)
		self.assertEqual(response.status_code, 201, response.data)

		#Test to Ensure you get error when Submitting a Scenario with the Same Name
		response = self.client.post('/v1/scenario/', json=tdPayload)
		self.assertEqual(response.status_code, 400, response.data)

		#When Error Response. Ensure Error Response Contains Error and Message
		data = response.get_json() or {}

		#Check Payload Contains Error Data.
		self.assertNotEqual(data, None)
		#Check Payload Contains Scenario Name
		self.assertNotEqual(data.get('error'), None)
		self.assertNotEqual(data.get('message'), None)
	
	# Ensure that Flask Route Scenario was set up correctly
	def test_route_scenario_get_200(self):
		#Run Scenario Creation 
		self.test_route_scenario_post_201()
		#Call Get Function on Scenario ID == 1
		response = self.client.get('/v1/scenario/1')
		#Test for Succcessful Response
		self.assertEqual(response.status_code, 200)
		response.data
	

	# Ensure that Scenario Get Route Contains the Correct Return Data
	def test_route_scenario_get_payload_format(self):
		#Run Scenario Creation 
		self.test_route_scenario_post_201()
		#Call Get Function on Scenario ID == 1
		response = self.client.get('/v1/scenario/1')
		
		#Test for Succcessful Response with Scenario Payload
		data = response.get_json() or {}
		data = data['scenario']

		#Check Payload Contains Scenario Object
		self.assertNotEqual(data, None)
		#Check Payload Contains Scenario Name
		self.assertNotEqual(data.get('Name'), None)
		#Check Payload Contains Scenario Description
		self.assertNotEqual(data.get('Description'), None)
		#Check Payload Contains Scenario ID
		self.assertNotEqual(data.get('ID'), None)
		#Check Payload Sys Active == True on Creation
		self.assertTrue(data.get('sys_active'))

