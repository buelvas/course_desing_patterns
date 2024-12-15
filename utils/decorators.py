from functools import wraps
from flask import request

def validate_token(f):
    def is_valid_token(token):
        return token == "abcd1234" 

    @wraps(f)
    def wrapped(*args, **kwargs):
        token = request.headers.get('Authorization')
        
        if not token:
            return { 'message': 'Unauthorized access token not found'}, 401
        
        if not is_valid_token(token):
            return { 'message': 'Unauthorized invalid token'}, 401
        
        return f(*args, **kwargs)

    return wrapped
