import os
from flask import Flask, jsonify
from flask_cors import CORS
from logging.handlers import TimedRotatingFileHandler
import logging
from .core.config import Config

def create_app():
    app = Flask(__name__)

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    app.config.from_object(Config)
    # logs
    if not os.path.exists('logs'):
        os.mkdir('logs')

    # Logging
    # handler = TimedRotatingFileHandler(app.config['LOG_FILE'], when="S", interval=10, backupCount=7)
    handler = TimedRotatingFileHandler(app.config['LOG_FILE'], when="midnight", interval=1, backupCount=7)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

    app.logger.info('Starting server...')

    @app.get('/')
    def index():
        return jsonify({"message": "Server is running"}), 200

    # Register blueprints
    from  .routes import ocr_route
    app.register_blueprint(ocr_route, url_prefix='/api/ocr')

    # return app
    return app