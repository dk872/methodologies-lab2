import unittest
from list_class import List


class TestListMethods(unittest.TestCase):
    def setUp(self):
        self.lst = List()

    def test_length_empty(self):
        """Checks that the length of an empty list is calculated correctly."""
        self.assertEqual(self.lst.length(), 0)

    def test_length_after_adding(self):
        """Checks that the length of the list is calculated correctly after adding elements."""
        self.lst.append('a')
        self.lst.append('b')
        self.assertEqual(self.lst.length(), 2)

    def test_length_after_removing(self):
        """Checks that the length of a list is calculated correctly after adding and removing elements."""
        self.lst.append('a')
        self.lst.append('b')
        self.lst.delete(0)
        self.assertEqual(self.lst.length(), 1)

    def test_append(self):
        """Checks that items are added to the list."""
        self.lst.append('a')
        self.lst.append('b')
        self.assertEqual(self.lst.get(0), 'a')
        self.assertEqual(self.lst.get(1), 'b')

    def test_insert_empty(self):
        """Checks for insertion of an element into the correct position of an empty list."""
        self.lst.insert('b', 0)
        self.assertEqual(self.lst.get(0), 'b')

    def test_insert_nonempty(self):
        """Checks for insertion of an element into the correct position of a populated list."""
        self.lst.append('a')
        self.lst.append('c')
        self.lst.insert('b', 1)

        self.assertEqual(self.lst.get(0), 'a')
        self.assertEqual(self.lst.get(1), 'b')
        self.assertEqual(self.lst.get(2), 'c')

    def test_insert_invalid_index(self):
        """Checks that an error occurs if the index is incorrect."""
        with self.assertRaises(IndexError):
            self.lst.insert('x', 5)

    def test_delete_valid_index(self):
        """Checks for deletion of an element at a correct index."""
        self.lst.append('a')
        self.lst.append('b')
        removed = self.lst.delete(0)

        self.assertEqual(removed, 'a')
        self.assertEqual(self.lst.get(0), 'b')

    def test_delete_empty(self):
        """Checks for an error call when trying to remove an item from an empty list."""
        with self.assertRaises(IndexError):
            self.lst.delete(0)

    def test_delete_invalid_index(self):
        """Checks for an error call when attempting to delete an element with an incorrect index."""
        self.lst.append('a')
        self.lst.append('b')
        with self.assertRaises(IndexError):
            self.lst.delete(2)
            