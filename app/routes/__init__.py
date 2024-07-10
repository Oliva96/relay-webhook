def init_routes(app):
    from . import handler
    app.register_blueprint(handler.bp)