import json
import urllib.request
import pprint
import webbrowser


key = open('KEY.txt', 'r', errors='ignore', encoding='utf-8').readline()
URL = "https://api.nasa.gov/planetary/apod?api_key={0}".format(key)
jsonFILE = json.loads(urllib.request.urlopen(URL).read())
pprint.pprint(jsonFILE)
webbrowser.open(jsonFILE['url'])
