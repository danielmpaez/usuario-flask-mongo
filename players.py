  from flask import Flask, request, render_template
import os
from pymongo import MongoClient
from bson.objectid import ObjectId
import bson
import jsonify
import json

Mongoclient= 'mongodb://starcraft:testing@3.tcp.ngrok.io:23370/scpipeline?authSource=admin'  #host
client = MongoClient(os.getenv("MONGO_URI"))
db = client['scpipeline']


app = Flask(__name__)

@app.route('/list', methods=['GET'])
def cast_index():
  ret = list(db.new_replays.find({}))
  json_data = json.dumps(ret)
  return json_data

  for x in ret.find():
    print(x)

@app.route('/uno')
def html1():
   return  render_template('index.html')



if __name__ == "__main__":    
    
    app.run(debug=True)  
