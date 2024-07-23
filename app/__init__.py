from flask import Flask
from .utils.s3 import s3
from .routes import init_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    from .utils.oauth import configure_oauth
    with app.app_context():
        configure_oauth(app)

    init_routes(app)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    s3.connect()

    return app