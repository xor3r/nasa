import folium


def readfile():
	f = open('data/locations.csv', 'r', errors='ignore', encoding='utf-8')
	data = (tuple(line.strip().split(',')) for line in f)
	return data


def build_map(data):

	ATTR ='<a href="https://github.com/openplanetary/opm/wiki/OPM-Basemaps" target="blank">OpenPlanetaryMap</a>'
	TILE = 'https://cartocdn-gusc.global.ssl.fastly.net/opmbuilder/api/v1/map/named/opm-mars-basemap-v0-1/all/{z}/{x}/{y}.png'

	m = folium.Map(attr=f'NASA/MOLA |{ATTR}',
				   location=(-4.58946695213448, 137.441633498919),
				   min_zoom=1,
				   max_zoom=20,
				   tiles=TILE,
				   zoom_start=12,
				   prefer_canvas=False)

	locations = [tuple(map(float, pair)) for pair in data]
	folium.PolyLine(locations).add_to(m)

	m.add_child(folium.CircleMarker(
		location=locations[0],
		popup=str(locations[0]),
		fill_color='blue',
		color='red',
		radius=8))
	m.add_child(folium.CircleMarker(
		location=locations[-1],
		popup=str(locations[-1]),
		fill_color='blue',
		color='red',
		radius=8))

	m.save('templates/mars.html')


if __name__ == '__main__':
	DATA = readfile()
	build_map(DATA)
