from app import db
from flask import jsonify, request
from flask import current_app as app
from flask.views import View, MethodView
from api.models import User
from api.schemas import UserSchema
from api.v1_api.errors import bad_request, error_404, error_405, error_500 
from api.v1_api.created import created_request
from api.v1_api.success import success_request
from api.v1_users import bp



class UserAPI(MethodView):
    #Response Nesting Title
    self.schemaTitle = 'users'

    def get(self):
        vUsers = User.query.all()
        return success_request(message="Found {} commentds for Row ID {}.".format(len(vUsers), ROW_ID), data=UserSchema().dump(vUsers, many=True), title=self.schemaTitle)
        

    def post(self):
        user = User.from_form_data(request.form)
        

bp.add_url_rule('/', view_func=UserAPI.as_view('users'))