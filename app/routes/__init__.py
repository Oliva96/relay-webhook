from . import handler, auth
def init_routes(app):
    app.register_blueprint(handler.bp)
    app.register_blueprint(auth.bp)