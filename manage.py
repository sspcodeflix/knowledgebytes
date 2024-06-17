# from flask import Flask
# from app import create_app
# import os
# print(os.getenv('FLASK_ENV'))
# app = create_app(os.getenv('FLASK_ENV') or 'development')

# if __name__ == '__main__':
#     app.run()

from flask import Flask
from flask_migrate import Migrate
from app import create_app, db
import os

app = create_app(os.getenv('FLASK_ENV') or 'development')
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()
