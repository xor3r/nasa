from xml.dom import minidom
import urllib.request


locs = 'http://mars.jpl.nasa.gov/msl-raw-images/locations.xml'

data = urllib.request.urlopen(locs).read()
xmldoc = minidom.parseString(data)
lon = xmldoc.getElementsByTagName('lon')
lat = xmldoc.getElementsByTagName('lat')
featureCollection = list()

print(lon[0].firstChild.nodeValue)
print(lat[0].firstChild.nodeValue)
print(len(lat), len(lon))


