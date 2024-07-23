from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from ..utils.jwt import generate_token

bp = Blueprint('auth', __name__)

users = {
    "user": {"password": "password-test"}
}
@bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username]['password'] == password:
        user = {'sub': username}
        jwt_token = generate_token(user)
        return jsonify({'token': jwt_token}), 200

    return jsonify({'message': 'Invalid credentials'}), 401