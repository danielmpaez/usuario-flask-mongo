from flask import Flask, request, render_template
import os
from pymongo import MongoClient
from bson.objectid import ObjectId
import bson
import jsonify
import json


client = MongoClient(os.getenv("Mongoclient"))
db = client['scpipeline']


app = Flask(__name__)

@app.route('/list', methods=['GET'])
def cast_index():
  ret = list(db.new_replays.find({}))
  json_data = json.dumps(ret)
  return json_data
  print(ret)

  for x in ret.find():
    print(x)

ret = list(db.new_replays.find({}))
print(ret)
# aca me devuelve bien el primer documento
@app.route('/list2', methods=['GET'])
def cast_index2():
  ret = list(db.new_replays.find_one())
  json_data = json.dumps(ret)
  return json_data
#aca intente desde uno de las claves /valor me devuelva un documento, no lo consegui, la idea era me devuelva el segundo
@app.route('/list3', methods=['GET'])
def cast_index3():
    
  ret = list(db.new_replays.find({'report_name':'9b68c7d66c1d5c3c52204856031d945e'}))
  json_data = json.dumps(ret)
  return json_data
  print(ret)


@app.route('/uno')
def html1():
   return  render_template('index.html')



if __name__ == "__main__":    
    
    app.run(debug=True)  
