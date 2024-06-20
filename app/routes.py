from flask import Blueprint, request, jsonify
from flask_restx import Api
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import db
from .models import Quiz, Question, User, Score
from sqlalchemy.sql import func

main = Blueprint('main', __name__)
api = Api(main)

@main.route('/')
def index():
    return "Welcome to the Quiz App"

@main.route('/check_user', methods=['POST'])
def check_user():
    data = request.get_json()
    email = data.get('email')
    
    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({'message': 'User exists'}), 200
    return jsonify({'message': 'User does not exist'}), 404

