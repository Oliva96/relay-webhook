from flask import Flask
from .utils.s3 import s3

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    from .routes import init_routes
    init_routes(app)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    s3.connect()

    return app