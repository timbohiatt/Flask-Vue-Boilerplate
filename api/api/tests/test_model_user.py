# tests/test_basic.py

import unittest

from .base import BaseTestCase
from ..models import db, User


class FlaskTestCase(BaseTestCase):

	# Ensure that Flask was set up correctly
	def test_model_user_create(self):
		#==================================================
		# Define Test Data
		#==================================================
		tdFirstName = "Timothy"
		tdLastName = "Hiatt"
		tdEmail = "THiatt@email.com"
		#==================================================

		#Create User DB Object
		tUser = User(    
			FirstName = tdFirstName,
			LastName = tdLastName,
			Email = tdEmail
		)
		#Add User Object to DB.
		db.session.add(tUser)
		db.session.commit()

		#Run Field Checks. Ensure Fields are Being Stored against the DB Correctly.
		self.assertEqual(tUser.FirstName, tdFirstName)
		self.assertEqual(tUser.LastName, tdLastName)
		self.assertEqual(tUser.Email, tdEmail)

# Ensure that Flask was set up correctly
	def test_model_user_query_by_id(self):
		#Reuse User Create Test Function to Create User Object
		self.test_model_user_create()
		#Get User from DB Using ID
		vUser = User.get_by_id(vID=1)
		#Check Returned Object == User and User ID == 1
		self.assertEqual(type(vUser), User)
		self.assertEqual(vUser.ID, 1)
		

	def test_model_user_set_inactive_active(self):
		#Reuse User Create Test Function to Create User Object
		self.test_model_user_create()

		tUser = User.get_by_id(vID=1)

		tUser.set_inactive()
		self.assertEqual(tUser.sys_active, False, "User, Set Inactive, Not Functining Correctly")
		
		tUser.set_active()
		self.assertEqual(tUser.sys_active, True, "User, Set Active, Not Functining Correctly")


	# Ensure that Flask was set up correctly
	def test_model_user_query_active_by_id(self):
		#Reuse User Create Test Function to Create User Object
		self.test_model_user_create()

		#Get User from DB Using ID
		vUser = User.get_active_by_id(vID=1)
		#Check Returned Object == User and User ID == 1
		self.assertEqual(type(vUser), User)
		self.assertEqual(vUser.ID, 1)
	
		vUser.set_inactive()
		db.session.commit()

		#Get User from DB Using ID
		vUser = User.get_active_by_id(vID=1)
		#Check Returned Object == User and User ID == 1
		self.assertEqual(type(vUser), type(None))
		self.assertEqual(vUser, None)


if __name__ == '__main__':
	unittest.main()