import urllib.request
import json
from modules.parse_location import get_locations, write_to_file
from classes.map_class import Map
from classes.adt_class import Multiset, DynamicArray
from classes.link_class import Array


def readfile():
    """
    Reads data from locations.csv file and returns it as a generator object.

    :return: generator object
    """
    f = open('../data/locations.csv', 'r', errors='ignore', encoding='utf-8')
    data = (tuple(line.strip().split(',')) for line in f)
    return data


def find_images():
    """
    Finds 20 images for displaying on map.

    :return: Array-class object
    """
    URL = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=mast&api_key=DEMO_KEY'
    link_storage = Array(20)
    response = urllib.request.urlopen(URL)
    data = json.loads(response.read())

    for i in range(20):
        link_storage[i] = data['photos'][i]['img_src']

    return link_storage


def build_map(data, links):
    """
    Builds map with folium and custom Map class.

    :param data: generator object
    :param links: Array-class object
    :return: Map-class object
    """
    m = Map(data)

    line_locations = Multiset()
    stored_locations = DynamicArray()
    for pair in data:
        line_locations.add(pair)
        stored_locations.append(pair)

    m.add_lines(line_locations)

    m.add_circle_marker(stored_locations[0], stored_locations[0],
                        'blue', 'red', 8)
    m.add_circle_marker(stored_locations[len(stored_locations)-1],
                        stored_locations[len(stored_locations)-1],
                        'blue', 'red', 8)

    loc = 100
    for link in links:
        m.add_popup_image(link,
                          width=200,
                          height=200,
                          location_tuple=stored_locations[loc])
        loc += 1000

    m.save_map('../templates/mars.html')

    return m


def main():
    """
    Main function which launches map creation and checks whether to update data
    file locations.csv.

    :return: None
    """
    generator = readfile()
    links = find_images()
    m = build_map(generator, links)
    need = m.need_to_update_map('../data/locations.csv')
    if need:
        print('Updating the map..')
        locations = get_locations()
        write_to_file(locations)
        DATA = readfile()
        build_map(DATA, links)
    else:
        print('No update needed')
    return None


if __name__ == '__main__':
    main()
