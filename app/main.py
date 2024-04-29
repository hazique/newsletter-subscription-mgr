
from flask_restful import Api
from app.resources import initialize_routes


from app import create_app

app = create_app()


api = Api(app)

initialize_routes(api)

if __name__ == '__main__':
    app.run(debug=True)