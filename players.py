from flask import Flask,jsonify, render_template,request,redirect,url_for # For flask implementation    
from bson import ObjectId   
from pymongo import MongoClient    
import os    
    
app = Flask(__name__)       
 
MONGO_Host = 'mongodb://3.tcp.ngrok.io/'  #host
MONGO_PORT = 23370  #port
MONGO_DB = 'scpipeline' #select database'
MONGO_USER = 'carlitos'  #username
MONGO_PASS = 'bala'    #password


#conection
con = MongoClient(MONGO_Host, MONGO_PORT)
db = con[MONGO_DB]
db.authenticate(MONGO_USER, MONGO_PASS)

print(db)   
#collection
new_replays = db.new_replays #Select the collection name     
print(new_replays)


#route   
@app.route("/list")    
    
#players= db.new_players
def players():
    return  jsonify(new_players) 
  

  

  
if __name__ == "__main__":    
    
    app.run(debug=True)  
