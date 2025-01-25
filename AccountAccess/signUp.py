from flask import Flask, request, jsonify 
from flask_cors import CORS
import os
import bcrypt
from supabase import create_client, Client

#url: str = os.environ.get("SUPABASE_URL")
#key: str = os.environ.get("SUPABASE_KEY")
#supabase: Client = create_client(url, key)

url = os.getenv("SUPABASE_URL")
#key = os.getenv("SUPABASE_KEY")
key = os.getenv("SUPABASE_SERVICE_KEY")
supabase = create_client(url,key)
import httpx

try:
    response = httpx.get(url)
    print(response.status_code)
except httpx.ConnectError as e:
    print(f"Connections failed: {e}")



app = Flask(__name__,template_folder="templates")
CORS(app)

@app.route("/signUp", methods=['POST'])
def createAccount():
    username = request.json['user']
    password = request.json['password']
    password = password.encode('utf-8')

    salt = bcrypt.gensalt()

    #index.upset({"username": username, "password": bcrypt.hashpw(password, salt), "history": []})

    supabase.table("accounts").insert({"id": 2, "username": username, "password": bcrypt.hashpw(password,salt).decode('utf-8')}).execute()

    return

if __name__ == '__main__':
    app.run(debug=True, port=5000)