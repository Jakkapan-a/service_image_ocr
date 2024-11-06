import os

class Config:
    UPLOAD_FOLDER = 'public/uploads'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024 # 16MB
    DEBUG = os.getenv("DEBUG", "false").lower()
    print("DEBUG =>",os.getenv('DEBUG'))
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    PORT = int(os.getenv("PORT", 10010))
    LOG_FILE = 'logs/app.log'




class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_ENV = 'development'

class ProductionConfig(Config):
    DEBUG = False
    FLASK_ENV = 'production'
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_secretKey')