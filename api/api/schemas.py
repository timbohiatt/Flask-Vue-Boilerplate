from api import db, ma
from api.models import User


class UserSchema(ma.SQLAlchemySchema):
	class Meta:
		model = User
	#Exposed Columns
	ID = ma.auto_field()
	Username = ma.auto_field()
	FirstName = ma.auto_field()
	LastName = ma.auto_field()
