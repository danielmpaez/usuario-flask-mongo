#importacion de librerias...
import json
from Flask import Flask, request, render_template
import os
#from pymongo import MongoClient
#from bson.objectid import ObjectId
#import bson
#import jsonify
import json
#from dateutil.parser import parse
import http.client
#import httplib2
import sys




#conexion a API Youtube
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')

YOUTUBE_ID = "LFoQqAI2LSo"

youtube_client = http.client.HTTPSConnection("https://www.googleapis.com/youtube/v3/playlists?key=[YOUTUBE_API_KEY]")
youtube_client.request("GET", "/youtube/v3/videos?part=contentDetails,id,liveStreamingDetails,snippet,statistics,status&channelId=UCZ7wN9kEDmRFhQ7MAotRIAQ&id={}&key={}".format(YOUTUBE_ID, YOUTUBE_API_KEY))
response = youtube_client.getresponse()
if response.status != 200:
  print("error: {}".format(response.read({title})))
  exit(1)

data = json.loads(response.read())
print(data)

# por cada item guardar en db.videos:
# - item['id']
# - item['snippet']['title']
# - parse(['liveStreamingDetails']['actualStartTime'])
# - item['statistics']


#conexion a Mongodb
'''client = MongoClient(os.getenv("Mongoclient"))
db = client['scpipeline']
mycol = db["youtube"]
datos =data
db.youtube.insert_many(data)'''



