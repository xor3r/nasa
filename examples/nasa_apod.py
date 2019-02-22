import json
import urllib.request
import pprint
import webbrowser


URL = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
jsonFILE = json.loads(urllib.request.urlopen(URL).read())
pprint.pprint(jsonFILE)
webbrowser.open(jsonFILE['url'])
