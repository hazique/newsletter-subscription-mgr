
from flask import Flask
from app.config import DevelopmentConfig, TestConfig

from flask_restful import Api
from app.resources import initialize_routes

from app.models.user import UserModel
from app.models.subscription import SubscriptionModel
from app.data_loader import load_data

import os


def create_app():
    app = Flask(__name__)

    # Load configuration based on environment
    env = os.environ.get('FLASK_ENV', 'development')
    if env == 'development':
        app.config.from_object(DevelopmentConfig)
        load_data(app)
        
    elif env == 'test':
        app.config.from_object(TestConfig)

    api = Api(app)

    initialize_routes(api)

    return app