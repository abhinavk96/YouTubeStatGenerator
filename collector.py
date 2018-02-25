import requests
import json
import pprint

data = requests.get('https://www.googleapis.com/youtube/v3/videos?id=7lCDEYXw3mM&key=AIzaSyABl0yMpz7he4CdOIrvgdNayyMpIu5AXe4&part=snippet,contentDetails,statistics,status')
jsonData=data.json()
requiredStats=jsonData['items'][0]['statistics']
commentCount, viewCount = int(requiredStats['commentCount']), int(requiredStats['viewCount'])
print(commentCount, viewCount)
#for key in jsonData:
#	print (key)
#pprint(dataDict)

