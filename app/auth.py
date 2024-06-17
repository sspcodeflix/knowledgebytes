from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, db
from flask_login import login_user, logout_user, login_required, current_user

auth = Blueprint('auth', __name__)


# Initialize the JWT manager
def initialize_jwt(app):
    # app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
    JWTManager(app)


@auth.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    is_author = data.get('is_author', False)

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'message': 'User already exists'}), 400

    user = User(username=username, email=email, is_author=is_author)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'Registration successful'}), 201

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return jsonify({'message': 'Invalid credentials'}), 401

    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)

    return jsonify({
        'message': 'Login successful',
        'access_token': access_token,
        'refresh_token': refresh_token
    }), 200

@auth.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user_id = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user_id)
    return jsonify({'access_token': new_access_token}), 200

@auth.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    return jsonify({'message': 'Logout successful'}), 200

@auth.route('/me', methods=['GET'])
@jwt_required()
def get_me():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if user:
        return jsonify({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'role': user.role,
            'credits': user.credits
        }), 200
    return jsonify({'message': 'User not found'}), 404