from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES


def created_response(status_code=None, message=None, data=None, title='data'):
	payload = {'status': HTTP_STATUS_CODES.get(status_code, 'Unknown Error')}
	if message:
		payload['message'] = message
	if data:
		payload[title]= data
	response = jsonify(payload)
	response.status_code = status_code
	return response


def created_request(message, data=None, title='data'):
	return created_response(201, message=message, data=data, title=title)