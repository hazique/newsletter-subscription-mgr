
from flask import Flask
from app.config import DevelopmentConfig, TestConfig
from logging.handlers import RotatingFileHandler
import logging
from flask.logging import default_handler

from flask_restful import Api

import os

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    configure_logging(app)

    # Load configuration based on environment
    env = os.environ.get('FLASK_ENV', 'development')
    if env == 'development':
        app.config.from_object(DevelopmentConfig)
        
    elif env == 'test':
        app.config.from_object(TestConfig)

    db.init_app(app)
    with app.app_context():           
        if not is_db_present(app):
            
            from app.models.user import UserModel
            from app.models.subscription import SubscriptionModel

            db.create_all()


    api = Api()
    register_routes(api)
    api.init_app(app)


    return app

def register_routes(api):
    from app.resources.subscription import SubscriptionResource
    api.add_resource(SubscriptionResource, '/subscription')

def is_db_present(app):
    db_path = os.path.join(app.instance_path, 'app.db')
    return os.path.isfile(db_path)

def configure_logging(app):
    # Logging Configuration
    file_handler = RotatingFileHandler('instance/flask-user-management.log',
                                        maxBytes=16384,
                                        backupCount=20)
    file_formatter = logging.Formatter('%(asctime)s %(levelname)s %(threadName)s-%(thread)d: %(message)s [in %(filename)s:%(lineno)d]')
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    # Remove the default logger configured by Flask
    app.logger.removeHandler(default_handler)

    app.logger.info('Starting the Flask User Management App...')


