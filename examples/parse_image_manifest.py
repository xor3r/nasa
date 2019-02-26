<<<<<<< Updated upstream
import json
import urllib.request
import pprint


URL = "https://mars.jpl.nasa.gov/msl-raw-images/image/image_manifest.json"
jsonFILE = json.loads(urllib.request.urlopen(URL).read())
#pprint.pprint(jsonFILE)

latest_sol = jsonFILE['latest_sol']
most_recent = jsonFILE['most_recent'][:10]
esol_url = jsonFILE['sols'][-1]['catalog_url']
esol_num_images = jsonFILE['sols'][-1]['num_images']
esol_num = jsonFILE['sols'][-1]['sol']

print("Last sol is: ", latest_sol)
print("Last update was on: ", most_recent)
print("Sol #{0}, Image link: {1}, Total images: {2}".format(str(esol_num),
														  str(esol_url),
=======
import json
import urllib.request
import pprint


URL = "https://mars.jpl.nasa.gov/msl-raw-images/image/image_manifest.json"
jsonFILE = json.loads(urllib.request.urlopen(URL).read())
#pprint.pprint(jsonFILE)

latest_sol = jsonFILE['latest_sol']
most_recent = jsonFILE['most_recent'][:10]
esol_url = jsonFILE['sols'][-1]['catalog_url']
esol_num_images = jsonFILE['sols'][-1]['num_images']
esol_num = jsonFILE['sols'][-1]['sol']

print("Last sol is: ", latest_sol)
print("Last update was on: ", most_recent)
print("Sol #{0}, Image link: {1}, Total images: {2}".format(str(esol_num),
														  str(esol_url),
>>>>>>> Stashed changes
														  str(esol_num_images)))