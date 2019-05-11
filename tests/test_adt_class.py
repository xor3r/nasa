from classes.adt_class import Node, Multiset, DynamicArray
from unittest import TestCase


class TestNode(TestCase):
    def setUp(self):
        self.node = Node('1')

    def tearDown(self):
        self.setUp()

    def test_str(self):
        self.node.next = Node('2')
        self.assertEqual(str(self.node), '1', 'Not the right item')
        self.assertEqual(str(self.node.next), '2', 'Not the right item')


class TestMultiset(TestCase):
    def setUp(self):
        self.ms = Multiset()
        self.ms.add('1')
        self.ms.add('2')

    def tearDown(self):
        self.setUp()

    def test_contains(self):
        self.assertEqual('1' in self.ms, True, 'Should contain!')

    def test_add(self):
        self.ms.add('3')
        self.assertEqual('3' in self.ms, True, 'Should have been added')

    def test_delete(self):
        self.ms.delete('1')
        self.assertEqual('1' in self.ms, False, 'Should have been deleted')

    def test_len(self):
        self.assertEqual(len(self.ms), 2, 'Should have contained 2 items')

    def test_remove_all(self):
        self.ms.remove_all()
        self.assertEqual(len(self.ms), 0, 'Should be 0')

    def test_str(self):
        self.assertEqual(str(self.ms), '{2, 1, }', 'Wrong')


class TestDynamicArray(TestCase):
    def setUp(self):
        self.da = DynamicArray()
        self.da.append('1')  # adds (1.0, )
        self.da.append('2')  # adds (2.0, )

    def tearDown(self):
        self.setUp()

    def test_len(self):
        self.assertEqual(len(self.da), 2, 'Should be 2')

    def test_append(self):
        self.da.append('3')
        self.assertEqual(self.da[2], (3.0,), 'Wrong')

    def test_insert(self):
        self.da.insert(2, '5')
        self.assertEqual(self.da[2], '5', 'Wrong')

    def test_remove(self):
        self.da.remove((2.0, ))
        self.assertEqual((2.0, ) in self.da, False, 'Should not contain')
