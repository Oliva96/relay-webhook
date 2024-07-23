from authlib.integrations.flask_client import OAuth
from flask import current_app

oauth = OAuth()

def configure_oauth(app):
    oauth.init_app(app)
    oauth.register(
        name='provider',
        client_id=current_app.config['OAUTH_CLIENT_ID'],
        client_secret=current_app.config['OAUTH_CLIENT_SECRET'],
        authorize_url='https://example.com/oauth/authorize',
        authorize_params=None,
        access_token_url='https://example.com/oauth/token',
        access_token_params=None,
        refresh_token_url=None,
        redirect_uri=None,
        client_kwargs={'scope': 'openid profile email'}
    )