from flask import Flask, redirect, session
from authlib.integrations.flask_client import OAuth

# --- Flask Setup ---
app = Flask(__name__)
app.secret_key = 'super-secret-key-for-testing'  # Persistent key for session

# --- Cognito OAuth Setup ---
oauth = OAuth(app)
oauth.register(
    name='cognito',
    client_id='356afchlgkf9gtrfuqus99bmg6',  # Your App Client ID
    client_secret='1rm40pphtrj2k9hv943kq19qiol83ho81csndujdm10r69df038i',  # App Client Secret
    server_metadata_url='https://cognito-idp.us-east-1.amazonaws.com/us-east-1_fdl86GhVS/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid email profile'}
)

# --- Routes ---
@app.route('/')
def index():
    user = session.get('user')
    if user:
        return f'Hello, {user.get("email", "User")}. <a href="/logout">Logout</a>'
    return 'Welcome! Please <a href="/login">Login</a>.'

@app.route('/login')
def login():
    # Must exactly match your Cognito app's callback URL
    redirect_uri = 'http://localhost:5000/authorize'
    return oauth.cognito.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
    token = oauth.cognito.authorize_access_token()
    user = token['userinfo']
    session['user'] = user
    return redirect('/')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

# --- Main ---
if __name__ == '__main__':
    app.run(debug=True, port=5000)
