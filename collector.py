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

with open('Arts.csv', 'r') as f_in, open('output.csv', 'w') as f_out:
	cols = ['id', 'views', 'comments']
	writer = csv.DictWriter(f_out, fieldnames=cols)
	writer.writeheader()
	reader = csv.DictReader(f_in)
	lines = len(open('Law.csv').readlines())
	counter = 0
	queryCounter = 0
	rows=[]
	for row in reader:
		newRow = {}
		newRow['id'] = row['id']
		rows.append(row['id'])
		counter+=1
		queryCounter+=1
		if (queryCounter == 50 or (queryCounter < 50 and counter == lines)):
			try:
				# Takes 50 videos at a time.
				data = requests.get('https://www.googleapis.com/youtube/v3/videos?id={}&key={}&part=statistics'.format(','.join(rows), API_KEY))
			except:
				print("A network error has occured")
			jsonData=data.json()
			# print (jsonData)
			for index, row in enumerate(rows):
				try:
					requiredStats=jsonData['items'][index]['statistics']
					newRow['id'], commentCount, viewCount = row, int(requiredStats['commentCount']), int(requiredStats['viewCount'])
					print(commentCount, viewCount)
					newRow['views'], newRow['comments'] = commentCount, viewCount
					writer.writerow(newRow)
				except:
					continue
			rows = []
			queryCounter = 0
			print('#############\nCurrent Count: {}'.format(counter))






