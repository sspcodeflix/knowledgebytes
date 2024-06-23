# import os
# from app import create_app
# from flask_cors import CORS
# from flask_migrate import upgrade

# def apply_migrations(app):
#     with app.app_context():
#         upgrade()

# if __name__ == '__main__':
#     os.system('source .env')
#     env = os.getenv('FLASK_ENV', 'development')
#     app = create_app(env)
#     cors = CORS(app, resources={r"/api/*": {"origins": "https://superstarbot.online"}})

#     app.config['CORS_HEADERS'] = 'Content-Type'
    
#     apply_migrations(app)

#     app.run()

import os
from app import create_app
from flask_cors import CORS

env = os.getenv('FLASK_ENV', 'development')
app = create_app(env)
cors = CORS(app, resources={r"/api/*": {"origins": "https://superstarbot.online"}})

app.config['CORS_HEADERS'] = 'Content-Type'

if __name__ == '__main__':
    app.run()
