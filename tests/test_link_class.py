from classes.link_class import Array
from unittest import TestCase


class TestArray(TestCase):
    def setUp(self):
        self.arr = Array(3)
        for i in range(3):
            self.arr[i] = i

    def tearDown(self):
        self.setUp()

    def test_len(self):
        self.assertEqual(len(self.arr), 3, 'Should be 3')

    def test_clear(self):
        self.arr.clear(None)
        self.assertEqual(any([i for i in range(3)]) in self.arr, False, 'Fail')
