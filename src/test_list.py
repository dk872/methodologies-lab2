import unittest
from list_class import List


class TestList(unittest.TestCase):
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

    '''def test_delete_all_two_elements(self):
        """Checks for deletion of all occurrences of two elements in a non-empty list."""
        self.lst.append('a')
        self.lst.append('b')
        self.lst.append('a')
        self.lst.delete_all('a')
        self.assertEqual(self.lst.get(0), 'b')

    def test_delete_all_one_element(self):
        """Checks for deletion of one element in a non-empty list."""
        self.lst.append('a')
        self.lst.append('b')
        self.lst.append('a')
        self.lst.delete_all('b')

        self.assertEqual(self.lst.get(0), 'a')
        self.assertEqual(self.lst.get(1), 'a')

    def test_delete_all_no_element(self):
        """Checks for immutability of the list if no items to delete are found."""
        self.lst.append('c')
        self.lst.append('a')
        self.lst.append('a')
        self.lst.delete_all('b')

        self.assertEqual(self.lst.get(0), 'c')
        self.assertEqual(self.lst.get(1), 'a')
        self.assertEqual(self.lst.get(2), 'a')'''

    def test_get_nonempty(self):
        """Checks for getting of an element into the correct position of a non-empty list."""
        self.lst.append('a')
        self.lst.append('x')
        self.lst.append('b')
        self.assertEqual(self.lst.get(1), 'x')

    def test_get_empty(self):
        """Checks that an error occurs if the list is empty."""
        with self.assertRaises(IndexError):
            self.lst.get(0)

    def test_get_invalid_index(self):
        """Checks that an error occurs if the index is incorrect."""
        self.lst.append('a')
        self.lst.append('x')
        self.lst.append('b')
        with self.assertRaises(IndexError):
            self.lst.get(3)

    def test_clone(self):
        """Checks that cloning creates a new list with the same contents and
        changes to the original list do not affect the cloned one."""
        self.lst.append('a')
        self.lst.append('b')
        self.lst.append('c')
        cloned_list = self.lst.clone()

        self.assertEqual(cloned_list.get(0), 'a')
        self.assertEqual(cloned_list.get(1), 'b')
        self.assertEqual(cloned_list.get(2), 'c')
        self.assertIsNot(cloned_list, self.lst)

        self.lst.append('x')
        self.lst.append('y')
        self.lst.delete(0)

        self.assertEqual(cloned_list.get(0), 'a')
        self.assertEqual(cloned_list.get(1), 'b')
        self.assertEqual(cloned_list.get(2), 'c')

        self.assertEqual(self.lst.get(0), 'b')
        self.assertEqual(self.lst.get(1), 'c')
        self.assertEqual(self.lst.get(2), 'x')
        self.assertEqual(self.lst.get(3), 'y')

    def test_reverse_nonempty(self):
        """Checks that the list is correctly reversed."""
        self.lst.append('c')
        self.lst.append('b')
        self.lst.append('b')
        self.lst.reverse()

        self.assertEqual(self.lst.get(0), 'b')
        self.assertEqual(self.lst.get(1), 'b')
        self.assertEqual(self.lst.get(2), 'c')

    def test_reverse_empty(self):
        """Checks that nothing happens with an empty list."""
        self.lst.reverse()
        self.assertEqual(self.lst.length(), 0)

    def test_find_first_two_elements(self):
        """Checks for the first occurrence of an element when there are two such elements in the list."""
        self.lst.append('a')
        self.lst.append('b')
        self.lst.append('c')
        self.lst.append('b')
        self.assertEqual(self.lst.find_first('b'), 1)

    def test_find_first_one_element(self):
        """Checks for the first occurrence of an element when there is only one such element in the list."""
        self.lst.append('a')
        self.lst.append('b')
        self.lst.append('c')
        self.lst.append('b')
        self.assertEqual(self.lst.find_first('c'), 2)

    def test_find_first_no_element(self):
        """Checks that if the element is not found, -1 is returned."""
        self.lst.append('a')
        self.lst.append('c')
        self.assertEqual(self.lst.find_first('b'), -1)

    def test_find_last_two_elements(self):
        """Checks for the last occurrence of an element when there are two such elements in the list."""
        self.lst.append('a')
        self.lst.append('b')
        self.lst.append('c')
        self.lst.append('b')
        self.assertEqual(self.lst.find_last('b'), 3)

    def test_find_last_one_element(self):
        """Checks for the last occurrence of an element when there is only one such element in the list."""
        self.lst.append('a')
        self.lst.append('b')
        self.lst.append('c')
        self.lst.append('b')
        self.assertEqual(self.lst.find_last('a'), 0)

    def test_find_last_no_element(self):
        """Checks that if the element is not found, -1 is returned."""
        self.lst.append('a')
        self.lst.append('c')
        self.assertEqual(self.lst.find_last('b'), -1)

    '''def test_clear_nonempty(self):
        """Checks that the list is cleared correctly."""
        self.lst.append('a')
        self.lst.append('b')
        self.lst.clear()
        self.assertEqual(self.lst.length(), 0)

    def test_clear_empty(self):
        """Checks that nothing happens with an empty list."""
        self.lst.clear()
        self.assertEqual(self.lst.length(), 0)

    def test_extend(self):
        """Checks that a list is properly extended by another list and that changes
        to the second list do not affect the first."""
        another_list = List()
        another_list.append('x')
        another_list.append('y')

        self.lst.append('a')
        self.lst.append('b')
        self.lst.extend(another_list)

        self.assertEqual(self.lst.get(0), 'a')
        self.assertEqual(self.lst.get(1), 'b')
        self.assertEqual(self.lst.get(2), 'x')
        self.assertEqual(self.lst.get(3), 'y')

        another_list.append('c')
        another_list.append('d')
        another_list.delete(0)

        self.assertEqual(self.lst.get(0), 'a')
        self.assertEqual(self.lst.get(1), 'b')
        self.assertEqual(self.lst.get(2), 'x')
        self.assertEqual(self.lst.get(3), 'y')

        self.assertEqual(another_list.get(0), 'y')
        self.assertEqual(another_list.get(1), 'c')
        self.assertEqual(another_list.get(2), 'd')'''
