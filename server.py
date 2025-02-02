from flask import Flask, request, jsonify, make_response 
from flask_cors import CORS
import jwt.exceptions
from BotCode.Bot import generate_text
from AccountAccess.signUp import create_Account
from AccountAccess.logIn import verify_account, verify_username
from AccountAccess.tokens import generate_jwt, get_access_token
import jwt
import os

refreshKey = os.getenv("REFRESH_KEY")
accessKey = os.getenv("ACCESS_KEY")

app = Flask(__name__,template_folder="templates")
CORS(app, supports_credentials=True)


@app.route("/bot", methods=['POST'])
def bot():
    question = request.json['query']
    #return(jsonify({'text' : generate_text(question)}))
    return(jsonify({'text' : 'I am the bot'}))

@app.route("/signUp", methods=['POST'])
def signUp():
    username = request.json['user']
    password = request.json['password']
    password = password.encode()

    return(jsonify({'isAccountCreated': create_Account(username, password)}))

@app.route("/logIn", methods=['POST'])
def logIn():
    username = request.json['user']
    password = request.json['password']
    password = password.encode()

    isUsernameExisting = verify_username(username)
    isPasswordVerified = False
    if(isUsernameExisting==True):
        isPasswordVerified = verify_account(username, password)

    return(jsonify({'isUsernameExisting': isUsernameExisting, 'isPasswordVerified': isPasswordVerified}))

@app.route("/logOut", methods=['DELETE'])
def logout():
    response = make_response("Logged out")
    response.set_cookie('accessToken', '', expires=0)
    response.set_cookie('refreshToken', '', expires=0)
    return response

@app.route("/initializeSession", methods=['POST'])
def initializeSession():
    username = request.json['user']
    accessToken, refreshToken = generate_jwt(username)
    response = make_response("Login Successful")
    response.set_cookie(key="refreshToken", value=refreshToken, httponly=True, secure=True, samesite="Strict", max_age=1 * 24 * 60 * 60)
    response.set_cookie(key="accessToken", value=accessToken, httponly=True, secure=True, samesite="Lax", max_age=30 * 60)
    return response

@app.route("/authenticate", methods=['POST'])
def authenticate():
    accessToken = request.cookies.get("accessToken")

    try:
        accessToken = jwt.decode(accessToken, accessKey, algorithms=["HS256"])
        username = accessToken.get("username")

        return(jsonify({"isTokenValid":True, "username": username}))
    
    except (jwt.ExpiredSignatureError, jwt.DecodeError):
        refreshToken = request.cookies.get("refreshToken")
        accessToken = get_access_token(refreshToken)

        if(accessToken==None):
            return(jsonify({"isTokenValid":False, "error": "Invalid token"}))
        
        else:
            username = jwt.decode(accessToken, accessKey, algorithms=["HS256"]).get("username")
            response = make_response(jsonify({"isTokenValid":True, "username": username}))
            response.set_cookie(key="accessToken", value=accessToken, httponly=True, secure=True, samesite="Lax", max_age=30 * 60)
            return response
    


           

if __name__ == '__main__':
    app.run(debug=True, port=5000)
