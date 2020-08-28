from flask import Flask, render_template,request,redirect,url_for # For flask implementation    
from bson import ObjectId # For ObjectId to work    
from pymongo import MongoClient    
import os    
    
app = Flask(__name__)       
 
MONGO_Host = 'mongodb://3.tcp.ngrok.io/'  #host
MONGO_PORT = 23370  #port
MONGO_DB = 'scpipeline' #select database'
MONGO_USER = 'starcraft'  #username
MONGO_PASS = 'testing'    #password


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
def lists ():    
   players= db.new_players.find() 
   return render_template(players)    
  

  

  
if __name__ == "__main__":    
    
    app.run(debug=True)  