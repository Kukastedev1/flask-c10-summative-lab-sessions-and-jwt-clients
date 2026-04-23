from flask import Blueprint, request
from models import User
from extensions import db
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

auth_bp = Blueprint('auth_bp', __name__)


# SIGNUP (auto-login behavior)
@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    if not data or not data.get('username') or not data.get('password'):
        return {"errors": ["Username and password required"]}, 400

    if User.query.filter_by(username=data['username']).first():
        return {"errors": ["Username already exists"]}, 400

    user = User(username=data['username'])
    user.set_password(data['password'])

    db.session.add(user)
    db.session.commit()

    token = create_access_token(identity=str(user.id))

    return {
        "access_token": token,
        "user": {
            "id": user.id,
            "username": user.username
        }
    }, 201


# LOGIN ( frontend-compatible)
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data:
        return {"errors": ["No input data"]}, 400

    user = User.query.filter_by(username=data['username']).first()

    if user and user.check_password(data['password']):
        token = create_access_token(identity=str(user.id))

        return {
            "access_token": token,
            "user": {
                "id": user.id,
                "username": user.username
            }
        }, 200

    return {"errors": ["Invalid credentials"]}, 401

# ME 
@auth_bp.route('/me', methods=['GET'])
@jwt_required()
def me():
    user_id = int(get_jwt_identity())
    user = User.query.get(user_id)

    if not user:
        return {"errors": ["User not found"]}, 404

    return {
        "id": user.id,
        "username": user.username
    }, 200