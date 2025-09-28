# You're Not Invited - Flask Cognito Login Demo

This project demonstrates how to integrate **Amazon Cognito** with a **Flask web app** for secure user authentication.

## Features
- AWS Cognito User Pool integration
- Secure login & logout
- OAuth2 flow with hosted Cognito UI
- Flask backend

## Configuration
Before running the app, update your `app.py` with your Cognito details:

```python
COGNITO_USER_POOL_ID = 'us-east-1_fdl86GhVS'
COGNITO_CLIENT_ID = '356afchlgkf9gtrfuqus99bmg6'
COGNITO_CLIENT_SECRET = '1rm40pphtrj2k9hv943kq19qiol83ho81csndujdm10r69df038i'
COGNITO_DOMAIN = 'https://us-east-1fdl86ghvs.auth.us-east-1.amazoncognito.com'
REDIRECT_URI = 'http://127.0.0.1:5000/authorize'

## How to Run

1. Clone this repository:

git clone https://github.com/richpgitdemo/cognito-flask-login.git
cd cognito-flask-login

2. Install dependencies: 

pip install flask authlib requests

3. Start the Flask app:

python app.py

4. Open your browser and go to:

http://127.0.0.1:5000/login

## Skills Shown

-AWS Cognito configuration

-Flask web development

-OAuth2 authentication

-Git/GitHub project setup

## Notes

-Make sure your Cognito app client has Authorization code grant enabled.

-Allowed callback URL: http://127.0.0.1:5000/authorize

-Allowed logout URL: http://127.0.0.1:5000/




