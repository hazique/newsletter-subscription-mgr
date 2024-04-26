from flask import Flask
from flask_restful import Api
from app.resources import initialize_routes, subscription
from app.config import DevelopmentConfig, TestConfig

import os

app = Flask(__name__)

# Load configuration based on environment
env = os.environ.get('FLASK_ENV', 'development')
if env == 'development':
    app.config.from_object(DevelopmentConfig)
elif env == 'test':
    app.config.from_object(TestConfig)

api = Api(app)

initialize_routes(api)

if __name__ == '__main__':
    app.run(debug=True)