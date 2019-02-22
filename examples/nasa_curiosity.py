import json
import urllib.request
import pprint
import webbrowser


key = open('KEY.txt', 'r', errors='ignore', encoding='utf-8').readline()
rover = 'curiosity'
URL = "https://api.nasa.gov/mars-photos/api/v1/rovers/{0}/photos?earth_date=2019-2-14&api_key={1}".format(rover,key)
jsonFILE = json.loads(urllib.request.urlopen(URL).read())
pprint.pprint(jsonFILE)
print(rover + '\n' +
	  jsonFILE['photos'][0]['camera']['full_name'] + '\n' +
	  jsonFILE['photos'][0]['earth_date'])
webbrowser.open(jsonFILE['photos'][0]['img_src'])
