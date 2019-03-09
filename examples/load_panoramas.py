import urllib.request
import json
import wget
from pprint import pprint


def search():
	url = "https://images-api.nasa.gov/search?q=mars%20360&media_type=image&center=JPL"
	json_file = json.load(urllib.request.urlopen(url))
	return json_file


def create_datasets(jsonFILE):
	dataset = list()
	for data in jsonFILE['collection']['items']:
		dataset.append((data['data'][0]['nasa_id'],
						data['data'][0]['date_created'],
						data['href']))
	return dataset


def load_metadata(dataset):
	for item in dataset:
		url = item[2]
		json_file = json.load(urllib.request.urlopen(url))


def load_panorama(collection_url, number):
	url = json.load(urllib.request.urlopen(collection_url))[0]
	wget.download(url, '/COURSES/CS_course/Coursework/nasa/media/PIA{}.jpg'.format(str(number)))


def main():
	jsonFILE = search()
	dataset = create_datasets(jsonFILE)
	for i in range(len(dataset)):
		print(i)
		load_panorama(dataset[i][2], i)
	return


if __name__ == '__main__':
	main()
