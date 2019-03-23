# nasa
Project for analyzing data from NASA's API (mainly rovers on Mars) and creating a VR experience using it.

![](https://img.shields.io/badge/-status:wip-5319e7.svg)
![](https://img.shields.io/github/license/damoklov/nasa.svg)
![](https://img.shields.io/github/languages/code-size/damoklov/nasa.svg)
![](https://img.shields.io/github/last-commit/damoklov/nasa.svg)

> _"One, remember to look up at the stars and not down at your feet. Two, never give up work. Work gives you meaning and purpose and life is empty without it. Three, if you are lucky enough to find love, remember it is there and don’t throw it away." - Stephen Hawking_

![GIF](https://media.giphy.com/media/xT0xezQXGJl8nRthny/source.gif)


# Virtual Journey on Mars

This project is in development as a part of my coursework from Programming course.
It makes you able to visit a website, where you can:
1. Download an app on your Android phone, which gives you an opportunity to take a journey through Martian fields.
2. Have a look on a map of Curiosity rover's movement since the very beginning of its life on Mars.
3. Look on some photos of Mars based on your choice.

## Getting Started

You can manually download this project and run __flask_app.py__ to locally open a website or run __make_map.py__ to see how I created a folium-based HTML map. You can also clone this repo by typing into your terminal: `git clone <repo's_link>` \
See deployment for notes on how to deploy the project on a live system.

### Prerequisites (chapter is in progress)

You do not need any special tools for running my project except for Python 3 and certain packages

```
Examples will be here soon!
```

### Installing (chapter is in progress)

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Examples will be here soon!
```

And repeat

```
Examples will be here soon!
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests (chapter is in progress)

Explain how to run the automated tests for this system

### Break down into end to end tests (chapter is in progress)

Explain what these tests test and why

```
Examples will be here soon!
```

### And coding style tests (chapter is in progress)

Explain what these tests test and why

```
Examples will be here soon!
```

## Deployment (chapter is in progress)

Add additional notes about how to deploy this on a live system

## Built With (chapter is in progress)

* [Feature1](link) - description
* [Feature2](link) - description
* [Feature3](link) - description

## Contributing (chapter is in progress)

Please read [CONTRIBUTING.md](link) for details on our code of conduct, and the process for submitting pull requests to me.

## Versioning (chapter is in progress)

Version 0.1 (Alpha) - 21.02.2019
Version 0.2 (Alpha) - 23.03.2019

## Authors

* **Mykhailo Pazyniuk** - [damoklov](https://github.com/damoklov/)

See also the list of [contributors](link) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments 

* I used this wonderful README.md template made by [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* Inspiration
* etc

## Brief explanation of API functions
### Main features
https://api.nasa.gov/index.html
***

#### **Mars Rover Photos**

This, provided by NASA, API helps to gather information from **'Curiosity', 'Opportunity' and 'Spirit'** rovers, what makes it more easy for scientists and developers to access it.\
This API is currently monitored by _Chris Cerami_.\
Each rover has its own cameras, photos from which are stored in a DB.\
There are several possible API requests. The photos are organized using the SOL attribute (Mars' unit of the day) when they were made.\
For example, photos taken at the 1,000th Martian day will have the _sol=1000_ attribute.\
The size of the recording is given, the results can also be filtered by the camera with which they were made.\
Requests that must return more than 25 photos will be divided into several pages, which can be accessed by adding to the record _page_.\
Each camera has a unique feature and perspective.\
Example of entry on 06/06/2015 (https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2015-6-3&api_key=DEMO_KEY)
***

## Coursework description problem
### Idea
Space is the endless, separate world for exploration, where each one of us can find something for him or her.\
My research topic is based on the info, providede by the National Aeronautics and Space Administration (NASA):
* Photos from the rovers
* Locations of the rovers and their coordinates on Mars

In my opinion, the biggest problem of our time is the reluctance to explore something beyond our daily lives.\
NASA also provides an opportunity for anyone wishing to use their APIs - to contribute to space exploration and to disseminate information on the advancement of research activities for nearest ones (such as Mars) and the most distant (other galaxies) corners of our universe.

> The National Aeronautics and Space Administration (NANA) is a US government agency founded in 1958 for Aeronautics and Space Exploration. NASA headquarters is located in Washington; The main platform is Cape Canaveral at the Kennedy Space Center in Florida. The first NASA space program began with the launch of the Pioneer spacecraft in 1958, which collected information for further manned flights, the most famous of which was the flight to the Apollo 11 moon on July 16-24, 1969.
<p align="center">
  <img src='https://www.logodesignlove.com/images/bad/nasa-logo-meatball.jpg'>
</p>

***
### Why Mars?
Nasa engineers have a lot of projects, but the study of the surface of Mars is currently one of the most promising in the short term, since very little time left before the flight of the first people to the Martian spaces!\
NASA provides free access to the data from the 'Curiosity' roaming coordinates during one or another period of its stay on a distant planet.
> The 'Curiosity' was launched from Cape Canaveral on November 26, 2011, at 10:02 aboard the Martian Scientific Laboratory (MSL) spacecraft and landed at Aeolis Palus in the Gale Mars Crater August 6, 2012, at 5:17. The  Bradbury Landing site is located less than 2.4 km (1.5 miles) from the Marshall landing point after a 563 million-kilometers-long (350 million-mile) trip.

This rover also makes daily photos and sends them here.\
This allows you to view the surface of Mars from a variety of angles, as well as obtain information on the relief, types of soils and possible forms of life.\
Curiosity also explores the peculiarities of climate in order to be able to assess the probability of survival of cultivated plants (or perhaps even humans) on Mars.\
He had already discovered that this planet had favorable conditions for the development of microbial life forms. This rover was successful in completing its stay for 687 Earth days (1 Martian year), but now it continues its journey and mission.
> MSL has four main goals:
> * Find out if there was ever life on Mars.
> * Get detailed information about the climate of Mars.
> * Get detailed information about Mars planetology.
> * To prepare for the landing of man on Mars.

> To achieve these goals, eight main tasks are faced with MSL:
> * Identify and establish the nature of Martian organic carbon compounds.
> * Identify the substances necessary for the life of life: carbon, hydrogen, nitrogen, oxygen, phosphorus, sulfur.
> * Identify possible traces of the course of biological processes.
> * Determine the chemical composition of the Martian surface.
> * Establish the process of formation of Martian stones and soil.
> * Evaluate the evolution of the Martian atmosphere in the long run.
> * Determine the current state, distribution and cycle of water and carbon dioxide.
> * Set the spectrum of radioactive radiation on the surface of Mars.

There are several cameras installed on the 'Curiosity' rover, photos from 7 of them are available for now.

| ID |          Full name          | State |
| ------- | ----------------------------- | ---- |
|FHAZ     | Front Hazard Avoidance Camera |  ✔  |
|RHAZ     | Rear Hazard Avoidance Camera  |  ✔  |
|MAST     | Mast Camera                   |  ✔  |
|CHEMCAM  | Chemistry and Camera Complex  |  ✔  |
|MAHLI    | Mars Hand Lens Imager         |  ✔  |
|MARDI    | Mars Descent Imager           |  ✔  |
|NAVCAM   | Navigation Camera             |  ✔  |

***

### Summary
#### Concept
The concept of the program is that it, with the resources provided by NASA, will do the following:
1. Access the necessary photos from the rooftop cameras
2. Processing information from database files with coordinates of the rover during the entire stay on Mars
3. Make a map of 'Curiosity' travel on the surface of the planet

These features are only the initial ones that I expect to complete before the deadline of this coursework.\
I also plan to gradually expand the functionality, which will differentiate my program from analogues on the network.

***

## System requirements
|                              **System Requirements**                            |
| ----------------------------------------------------------------------------- |
| **Project Sponsor:** Michael Pazyniuk |
| **Business need:** This project was created for the public's apparent need for information on space exploration and Mars in particular. The project also focuses on the need of the international organization (NASA) to expand the horizons of disseminating information on the state of its research.|
| **Business requirements:** Using an app or a web page, users will be able to see a rendered page of the 'Curiosity' roaming map of the planet, as well as view photos taken by it throughout its stay on Mars and every day in particular. Features of the product that is manufactured are: <ul><li>View a convenient map of moving the rover.</li><li>Accessing photos from the rover at the selected days </li><li>Selecting a specific roaming camera</li></ul>|
| **Business value:** I expect that the product that I will manufacture in the next few months will interest as many users as possible. I do not expect to receive a profit from this product, since it is classified as an _open-source_. I also hope to prepare a functional that will provide convenient and clear access to the necessary information.|
| **Special issues or constraints:** <ul><li>The coursework must be accomplished until 25th of May</li><li>I expect to provide additional functionality until the deadline</li><li>New functions will be added if possible</li></ul>|
