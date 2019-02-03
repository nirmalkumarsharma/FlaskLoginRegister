from flask import Flask, jsonify, json, request
from datetime import datetime
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import (create_access_token)
from flask_jwt_extended import JWTManager
from user_database_setup import LocalUser

import user_database_service

app=Flask(__name__)
app.config['JWT_SECRET_KEY']='secret'
bcrypt=Bcrypt(app)
jwt=JWTManager(app)

CORS(app)

@app.route('/user/register', methods=['POST'])
def register():
	r_first_name=request.get_json()['first_name']
	r_last_name=request.get_json()['last_name']
	r_email=request.get_json()['email']
	r_password=bcrypt.generate_password_hash(request.get_json()['password']).decode('utf-8')

	result=""

	if user_database_service.if_user_exists(r_email):
		result="user already exists"
		return jsonify({'result': result})

	new_user=LocalUser(first_name=r_first_name, last_name=r_last_name, email=r_email, password=r_password, created=datetime.utcnow())
	added=user_database_service.add_user(new_user)
	if added is True:
		result="user successfully added"
	else:
		result="unable to add"

	return jsonify({'result': result})


@app.route('/user/login', methods=['POST'])
def login():
	email=request.get_json()['email']
	password=request.get_json()['password']
	result=""

	response_user=user_database_service.get_user(email)

	if response_user:
		if bcrypt.check_password_hash(response_user.password, password):
			access_token=create_access_token(
				identity=
				{
					'first_name': response_user.first_name,
					'last_name': response_user.last_name,
					'email': response_user.email
				}
			)
			result=jsonify({'token': access_token})
		else:
			result=jsonify({'error': 'Invalid username or password'})
	return result

if __name__=='__main__':
	app.run(host="127.0.0.1", port=5000, debug=False)
