from flask import Flask, request, jsonify 
from flask_cors import CORS
import os
import bcrypt
from supabase import create_client

#url: str = os.environ.get("SUPABASE_URL")
#key: str = os.environ.get("SUPABASE_KEY")
#supabase: Client = create_client(url, key)

url = os.getenv("SUPABASE_URL")
#key = os.getenv("SUPABASE_KEY")
key = os.getenv("SUPABASE_SERVICE_KEY")
supabase = create_client(url,key)


#app = Flask(__name__,template_folder="templates")
#CORS(app)

#@app.route("/signUp", methods=['POST'])
def createAccount(username, password):
    #get username and password
    #username = request.json['user']
    #password = request.json['password']
    #password = password.encode('utf-8')

    account = supabase.table("accounts").select("*").eq("username", username).execute()

    ##check if username already exists
    if(account.data!=[]):
        #return(jsonify({'isAccountCreated' : False}))
        return False
    
    supabase.table("accounts").select("username").eq("username", username).execute()

    salt = bcrypt.gensalt()

    ##insert account to the table with a new id
    response = supabase.table("accounts").select("id").order("created_at", desc=True).limit(1).execute()
    id = response.data[0].get('id')+1
    supabase.table("accounts").insert({"id": id, "username": username, "password": bcrypt.hashpw(password,salt).decode('utf-8')}).execute()

    #return(jsonify({'isAccountCreated' : True}))
    return True

#if __name__ == '__main__':
#    app.run(debug=True, port=5000)