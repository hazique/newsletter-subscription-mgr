from flask import Flask
from flask_restful import Api
from app.resources import initialize_routes
from app.config import DevelopmentConfig, TestConfig
from app.models import db
from app.models.user import UserModel
from app.models.subscription import SubscriptionModel

import os

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


api = Api(app)

initialize_routes(api)

if __name__ == '__main__':
    app.run(debug=True)