import json

#from dateutil.parser import parse
import  requests
import http.client
import os

YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')

YOUTUBE_ID = "LFoQqAI2LSo"

youtube_client = http.client.HTTPSConnection("www.googleapis.com")

#youtube_client.request("GET", "/youtube/v3/search?part=myRating,pageToken,statistics,status&channelId=UCZ7wN9kEDmRFhQ7MAotRIAQ&id={}&key={}".format(YOUTUBE_ID, YOUTUBE_API_KEY))
youtube_client.request("GET","/youtube/v3/search?part=id,snippet&channelId=UCZ7wN9kEDmRFhQ7MAotRIAQ&order=date&maxResults=10&key={}".format(YOUTUBE_API_KEY))


response = youtube_client.getresponse()
if response.status != 200:
  print("error: {}".format(response.read()))
  exit(1)


data = json.loads(response.read())
print(data)

r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&channelId=UCZ7wN9kEDmRFhQ7MAotRIAQ&order=date&key={}".format(YOUTUBE_API_KEY))
json_data = r.json()                                                                                                
nextPageToken = json_data.get("CAoQAA")
print(json_data)
# Devuelve el resto de las paginas en un bucle
while nextPageToken:
    r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&channelId=UCZ7wN9kEDmRFhQ7MAotRIAQ&order=date&key={}&pageToken=CAoQAA".format(YOUTUBE_API_KEY))
    json_data = r.json()
    nextPageToken = json_data.get("CAoQAA")
print(json_data)


# por cada item guardar en db.videos:
# - item['id']
# - item['snippet']['title']
# - parse(['liveStreamingDetails']['actualStartTime'])
# - item['statistics']
#https://www.googleapis.com/youtube/v3/search?part=$args&channelId=UCZ7wN9kEDmRFhQ7MAotRIAQ&key=$api_key&order=date&maxResults=10
