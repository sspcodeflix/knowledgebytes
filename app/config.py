import os

base_dir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'abcde'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'mysecret')  # Change this!
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # 1 hour
    JWT_REFRESH_TOKEN_EXPIRES = 86400  # 1 day

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'test.db')

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
