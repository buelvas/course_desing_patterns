from flask import Blueprint, request
from flask_restful import Resource, Api

auth_bp = Blueprint('auth', __name__)
api = Api(auth_bp)

class AuthenticationResource(Resource):
    def post(self):
        username = request.json.get('username')
        password = request.json.get('password')

        if username == 'student' and password == 'desingp':
            token = 'abcd12345'
            return {'token': token}, 200
        else:
            return {'message': 'unauthorized'}, 401

api.add_resource(AuthenticationResource, '/auth')




