import os
from app import create_app
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()

hostname = os.getenv("HOSTNAME")
env = os.getenv('FLASK_ENV', 'development')
app = create_app(env)
cors = CORS(app, resources={r"/api/*": {"origins": f"https://{hostname}"}})

app.config['CORS_HEADERS'] = 'Content-Type'

if __name__ == '__main__':
    app.run()
