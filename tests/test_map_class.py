from classes.map_class import Map
from unittest import TestCase


class TestMap(TestCase):
    def setUp(self):
        self.map_object = Map(['link1', 'link2', 'link3'])

    def tearDown(self):
        self.setUp()
