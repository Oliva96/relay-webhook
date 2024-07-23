from functools import wraps
from flask import request, jsonify
from .jwt import decode_token

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization', None)
        if not auth_header:
            return jsonify({"message": "Missing Authorization Header"}), 401

        parts = auth_header.split()
        if parts[0].lower() != 'bearer' or len(parts) != 2:
            return jsonify({"message": "Invalid Authorization Header"}), 401

        user = decode_token(parts[1])
        if user is None:
            return jsonify({'message': 'Token is invalid or expired!'}), 401

        return f(*args, **kwargs)
    return decorated_function