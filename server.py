from flask import Flask, request, jsonify 
from flask_cors import CORS
from BotCode.Bot import generate_text
from AccountAccess.signUp import createAccount

app = Flask(__name__,template_folder="templates")
CORS(app)


@app.route("/bot", methods=['POST'])
def bot():
    question = request.json['query']
    #return(jsonify({'text' : generate_text(question)}))
    return(jsonify({'text' : 'I am the bot'}))

@app.route("/signUp", methods=['POST'])
def signUp():
    username = request.json['user']
    password = request.json['password']
    password = password.encode('utf-8')

    return(jsonify({'isAccountCreated': createAccount(username, password)}))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
