import os
import logging
from app import create_app
from flask_cors import CORS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    env = os.getenv('FLASK_ENV', 'development') # Fetch the environment from .env if not found use default 'development'
    logger.info(f"Starting application in {env.upper()} environment")

    app = create_app(env)
    cors = CORS(app, resources={r"/api/*": {"origins": "https://superstarbot.online"}})

    app.config['CORS_HEADERS'] = 'Content-Type'

    logger.info("CORS configuration completed")
    logger.info("Application is running")

    app.run()
