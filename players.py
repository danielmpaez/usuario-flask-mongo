from flask import Flask,jsonify, render_template,request,redirect,url_for # For flask implementation    
from pymongo import MongoClient    
import os  
import json  
from bson import json_util, ObjectId 
    
app = Flask(__name__)       
 
Mongoclient = 'mongodb://ababab:xzxzxz@3.tcp.ngrok.io:23370/scpipeline?authSource=admin'  #host
#MONGO_PORT = 23370  #port
#MONGO_DB = 'scpipeline' #select database'
#MONGO_USER = 'ababab'  #username
#MONGO_PASS = 'xzxzxz'    #password


#conection
client = MongoClient(os.getenv("MONGO_URI"))
db = client['users']


print(db)   
#collection
players = db.new_replays #Select the collection name     
print(players)


cursor = client.list_databases()
for db in cursor:
    print(db)

#route   
@app.route("/list")    
def get_replays():
   
    response = jsonify(players)
    return Response(response)

    print(response)







    
  

  

  
if __name__ == "__main__":    
    
    app.run(debug=True)  
