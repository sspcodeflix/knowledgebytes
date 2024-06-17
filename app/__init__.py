from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
jwt = JWTManager()

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(f'app.config.{config_name.capitalize()}Config')

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    login_manager.init_app(app)

    from .models import User, Quiz, Question, Score

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/api')

    return app
