import json
import urllib.request
import pprint
import webbrowser


URL = "https://mars.jpl.nasa.gov/msl-raw-images/image/images_sol2320.json"
jsonFILE = json.loads(urllib.request.urlopen(URL).read())
#pprint.pprint(jsonFILE)

camera = jsonFILE['images'][0]['cameraModelType']
sol = jsonFILE['images'][0]['sol']
link = jsonFILE['images'][0]['urlList']

print('Camera type: {0}, Sol #{1}'.format(camera, sol))
webbrowser.open(link)
