from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    from .routes import init_routes
    init_routes(app)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    #TODO: Create s3 connection

    return app