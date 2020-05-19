
from flask import Blueprint

bp = Blueprint('v1_users', __name__)

from api.v1_users import users