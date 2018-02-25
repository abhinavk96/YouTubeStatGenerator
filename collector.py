import requests
import json
import pprint
import csv

with open('Law.csv', 'r') as f_in, open('output.csv', 'w') as f_out:
	cols = ['id', 'views', 'comments']
	writer = csv.DictWriter(f_out, fieldnames=cols)
	writer.writeheader()
	reader = csv.DictReader(f_in)
	for row in reader:
		newRow = {}
		newRow['id'] = row['id']
		data = requests.get('https://www.googleapis.com/youtube/v3/videos?id={}&key=AIzaSyABl0yMpz7he4CdOIrvgdNayyMpIu5AXe4&part=snippet,contentDetails,statistics,status'.format(row['id']))
		jsonData=data.json()
		try:
			requiredStats=jsonData['items'][0]['statistics']
			commentCount, viewCount = int(requiredStats['commentCount']), int(requiredStats['viewCount'])
			print(commentCount, viewCount)
			newRow['views'], newRow['comments'] = commentCount, viewCount
			writer.writerow(newRow)
		except:
			print("An unexpected error has occured. API Quota may be over")

#for key in jsonData:
#	print (key)
#pprint(dataDict)

