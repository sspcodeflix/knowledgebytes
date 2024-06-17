from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
import time
from . import db

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=True)
    is_author = db.Column(db.Boolean, default=False)
    role = db.Column(db.String(50), default='regular')
    credits = db.Column(db.Integer, default=5)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

def generate_id():
    return int(datetime.now().strftime("%Y%m%d%H%M%S"))

class Quiz(db.Model):
    __tablename__ = "quizzes"
    id = db.Column(db.Integer, primary_key=True, default=generate_id, unique=True, nullable=False)
    title = db.Column(db.String(150), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id', name='fk_quiz_author_id'), nullable=False)
    is_published = db.Column(db.Boolean, default=False)
    is_closed = db.Column(db.Boolean, default=False)

    author = db.relationship('User', backref=db.backref('quizzes', lazy=True))

class Question(db.Model):
    __tablename__ = "questions"
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id', name='fk_question_quiz_id'), nullable=False)
    text = db.Column(db.String(500), nullable=False)
    options = db.Column(db.String(500), nullable=False)
    answer = db.Column(db.String(100), nullable=False)

    quiz = db.relationship('Quiz', backref=db.backref('questions', lazy=True))

class Score(db.Model):
    __tablename__ = "scores"
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id', name='fk_score_quiz_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', name='fk_score_user_id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)

    user = db.relationship('User', backref=db.backref('scores', lazy=True))
    quiz = db.relationship('Quiz', backref=db.backref('scores', lazy=True))
