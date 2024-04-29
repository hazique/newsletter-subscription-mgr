
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import DevelopmentConfig, TestConfig

from app.models.user import UserModel
from app.models.subscription import SubscriptionModel

import os

from app.models import db


def create_app():
    app = Flask(__name__)

    # Load configuration based on environment
    env = os.environ.get('FLASK_ENV', 'development')
    if env == 'development':
        app.config.from_object(DevelopmentConfig)
    elif env == 'test':
        app.config.from_object(TestConfig)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app