from urllib.request import urlopen
from json import load


def search_images(date, camera):
    if date:
        date = '&earth_date=' + date
    if camera:
        camera = '&camera=' + camera
    URL = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?api_key=DEMO_KEY{0}{1}'.format(date, camera)
    json_file = load(urlopen(URL))
    photo_links = set()
    if json_file['photos'] != list():
        for i in range(len(json_file['photos'])):
            photo_links.add(json_file['photos'][i]['img_src'])
        return photo_links
    else:
        return None
