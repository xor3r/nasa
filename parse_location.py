from xml.dom import minidom
import urllib.request


def get_locations():
    locs = 'http://mars.jpl.nasa.gov/msl-raw-images/locations.xml'
    data = urllib.request.urlopen(locs).read()
    xmldoc = minidom.parseString(data)
    lon = xmldoc.getElementsByTagName('lon')
    lat = xmldoc.getElementsByTagName('lat')
    featureCollection = list()

    for i in range(len(lat)):
        featureCollection.append((lat[i].firstChild.nodeValue,
                                  lon[i].firstChild.nodeValue))

    return featureCollection


def write_to_file(locations, attr='w'):
    f = open('data/locations.csv', attr, encoding='utf-8', errors='ignore')
    for pair in locations:
        f.write(str(pair[0]) + ',' + str(pair[1]) + '\n')
    f.close()


if __name__ == '__main__':
    locations = get_locations()
    write_to_file(locations)
