from flask import Flask, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secure random key

# OAuth setup for your new Cognito pool
oauth = OAuth(app)
oauth.register(
    name='cognito',
    client_id='356afchlgkf9gtrfuqus99bmg6',  # New App Client ID
    client_secret='1rm40pphtrj2k9hv943kq19qiol83ho81csndujdm10r69df038i',  # New App Client Secret
    server_metadata_url='https://cognito-idp.us-east-1.amazonaws.com/us-east-1_fdl86GhVS/.well-known/openid-configuration',  # New domain
    client_kwargs={'scope': 'openid profile email'}
)

@app.route('/')
def index():
    user = session.get('user')
    if user:
        return f'Hello, {user.get("email", "User")}. <a href="/logout">Logout</a>'
    return 'Welcome! Please <a href="/login">Login</a>.'

@app.route('/login')
def login():
    redirect_uri = url_for('authorize', _external=True)
    return oauth.cognito.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
    token = oauth.cognito.authorize_access_token()
    user = token['userinfo']
    session['user'] = user
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
