import pytest
from app import create_app, db
from app.models import User, Quiz, Question, Score

@pytest.fixture
def app():
    app = create_app('testing')
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def logged_in_client(client):
    user = User(username='testuser', email='test@example.com', is_author=True)
    user.set_password('password')
    db.session.add(user)
    db.session.commit()
    client.post('/auth/login', data={'email': 'test@example.com', 'password': 'password'}, follow_redirects=True)
    yield client
    client.get('/auth/logout')
