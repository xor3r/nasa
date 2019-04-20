from parse_location import get_locations, write_to_file
from classes.map_class import Map
from classes.adt_class import Multiset, DynamicArray


def readfile():
    f = open('data/locations.csv', 'r', errors='ignore', encoding='utf-8')
    data = (tuple(line.strip().split(',')) for line in f)
    return data


def build_map(data):
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

    m.add_popup_image("https://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/02375/opgs/edr/ncam/NRB_608330915EDR_M0751386NCAM00591M_.JPG",
                      width=255, height=300, location_tuple=stored_locations[21757])

    m.save_map('templates/mars.html')

    return m


def main():
    generator = readfile()
    m = build_map(generator)
    need = m.need_to_update_map('data/locations.csv')
    if need:
        print('Updating the map..')
        locations = get_locations()
        write_to_file(locations)
        DATA = readfile()
        build_map(DATA)
    else:
        print('No update needed')
    return None


if __name__ == '__main__':
    main()
