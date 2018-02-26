import requests
import json
import pprint
import csv
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')

load_dotenv(dotenv_path, verbose=True)

API_KEY = os.environ.get('API_KEY')

with open('Law.csv', 'r') as f_in, open('output.csv', 'w') as f_out:
	cols = ['id', 'views', 'comments']
	writer = csv.DictWriter(f_out, fieldnames=cols)
	writer.writeheader()
	reader = csv.DictReader(f_in)
	for row in reader:
		newRow = {}
		newRow['id'] = row['id']
		try:
			data = requests.get('https://www.googleapis.com/youtube/v3/videos?id={}&key={}&part=statistics'.format(row['id'], API_KEY))
		except:
			print("A network error has occured")
		jsonData=data.json()
		try:
			requiredStats=jsonData['items'][0]['statistics']
			commentCount, viewCount = int(requiredStats['commentCount']), int(requiredStats['viewCount'])
			print(commentCount, viewCount)
			newRow['views'], newRow['comments'] = commentCount, viewCount
			writer.writerow(newRow)
		except:
			print("An unexpected error has occured. API Quota may be over")

for key in jsonData:
	print (key)
pprint(dataDict)

