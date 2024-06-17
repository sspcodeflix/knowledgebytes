import pytest
from app import create_app, db
from app.models import User

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
def access_tokens(client):
    # Create and login a user to get the access and refresh tokens
    client.post('/auth/signup', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password',
        'is_author': True
    })
    response = client.post('/auth/login', json={
        'email': 'test@example.com',
        'password': 'password'
    })
    data = response.get_json()
    return data['access_token'], data['refresh_token']

def test_signup(client):
    response = client.post('/auth/signup', json={
        'username': 'testuser2',
        'email': 'test2@example.com',
        'password': 'password',
        'is_author': True
    })
    assert response.status_code == 201

    user = User.query.filter_by(email='test2@example.com').first()
    assert user is not None
    assert user.username == 'testuser2'

def test_login(client):
    # Create a user directly in the database
    user = User(username='testuser', email='test@example.com', is_author=True)
    user.set_password('password')
    db.session.add(user)
    db.session.commit()

    response = client.post('/auth/login', json={
        'email': 'test@example.com',
        'password': 'password'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert 'access_token' in data
    assert 'refresh_token' in data

def test_refresh_token(client, access_tokens):
    _, refresh_token = access_tokens

    response = client.post('/auth/refresh', headers={
        'Authorization': f'Bearer {refresh_token}'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert 'access_token' in data

def test_logout(client, access_tokens):
    access_token, _ = access_tokens

    response = client.post('/auth/logout', headers={
        'Authorization': f'Bearer {access_token}'
    })
    assert response.status_code == 200
    assert response.get_json()['message'] == 'Logout successful'

