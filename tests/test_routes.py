import pytest
import time
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
def access_tokens(client):
    # Create and login a user to get the access and refresh tokens
    signup_response = client.post('/auth/signup', json={
        'username': 'test@example.com',
        'email': 'test@example.com',
        'password': 'password',
        'is_author': True
    })
    print("Signup Response:", signup_response.data)
    login_response = client.post('/auth/login', json={
        'email': 'test@example.com',
        'password': 'password'
    })
    print("Login Response:", login_response.data)
    data = login_response.get_json()
    return data['access_token'], data['refresh_token']

@pytest.fixture
def logged_in_client(client, access_tokens):
    access_token, _ = access_tokens
    client.environ_base['HTTP_AUTHORIZATION'] = f'Bearer {access_token}'
    
    # Promote user to premium
    # promote_response = client.post('/api/promote_author', json={'user_id': 1}, headers={'Authorization': f'Bearer {access_token}'})
    # print("Promote Author Response:", promote_response.data)
    
    # Verify the user role and credits
    user = User.query.filter_by(email='test@example.com').first()
    print("User role after promotion:", user.role)
    print("User credits after promotion:", user.credits)
    
    # Re-fetch the user from the database to ensure the role and credit updates are reflected
    db.session.refresh(user)
    assert user.role == 'premium'
    assert user.credits == 100
    
    return client

def test_check_user(client):
    # Create a user
    user = User(username='test@example.com', email='test@example.com', is_author=False)
    user.set_password('password')
    db.session.add(user)
    db.session.commit()
    
    # Check if the user exists
    response = client.post('/api/check_user', json={'email': 'test@example.com'})
    assert response.status_code == 200
    assert response.get_json()['message'] == 'User exists'

    # Check if a non-existing user does not exist
    response = client.post('/api/check_user', json={'email': 'nonexistinguser@example.com'})
    assert response.status_code == 404
    assert response.get_json()['message'] == 'User does not exist'