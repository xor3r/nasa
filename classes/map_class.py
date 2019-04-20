import folium
from modules.parse_location import get_locations


class Map:
    ATTR = '<a href="https://github.com/openplanetary/opm/wiki/OPM-Basemaps" target="blank">OpenPlanetaryMap</a>'
    TILE = 'https://cartocdn-gusc.global.ssl.fastly.net/opmbuilder/api/v1/map/named/opm-mars-basemap-v0-1/all/{z}/{x}/{y}.png'

    def __init__(self, data):
        self.data = data
        self.m = folium.Map(attr=f'NASA/MOLA |{Map.ATTR}',
                            location=(-4.58946695213448, 137.441633498919),
                            min_zoom=1,
                            max_zoom=20,
                            tiles=Map.TILE,
                            zoom_start=12,
                            prefer_canvas=False)

    def add_lines(self, data):
        folium.PolyLine([tuple(map(float, pair)) for pair in data]).add_to(self.m)

    def add_circle_marker(self, location, popup, fill_color, color, radius):
        self.m.add_child(folium.CircleMarker(
            location=location,
            popup=str(popup),
            fill_color=fill_color,
            color=color,
            radius=radius))

    def save_map(self, filename):
        self.m.save(filename)

    def add_popup_image(self, img_link, width, height, location_tuple):
        iframe = folium.IFrame(
            '<img src={}>'.format(img_link),
            width=width,
            height=height)
        popup = folium.Popup(iframe, max_width=2500)
        folium.Marker(location_tuple, popup=popup).add_to(self.m)

    @staticmethod
    def need_to_update_map(filename):
        f = open(filename, 'r', errors='ignore', encoding='utf-8')
        first_locations = tuple(f.readline().strip().split(','))
        locations = get_locations()
        if locations[0] == first_locations:
            return False
        else:
            return True
