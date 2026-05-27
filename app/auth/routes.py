from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash

auth_bp = Blueprint('auth', __name__)

users = []

@auth_bp.route('/register', methods=['POST'])
def register():

    data = request.json

    user = {
        "username": data['username'],
        "password": generate_password_hash(data['password'])
    }

    users.append(user)

    return jsonify({
        "message": "User Registered"
    })

@auth_bp.route('/login', methods=['POST'])
def login():

    data = request.json

    access_token = create_access_token(
        identity=data['username']
    )

    return jsonify({
        "token": access_token
    })