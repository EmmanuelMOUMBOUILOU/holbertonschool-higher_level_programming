#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 2]), 3)

    def test_max_at_start(self):
        self.assertEqual(max_integer([5, 3, 1]), 5)

    def test_one_element(self):
        self.assertEqual(max_integer([42]), 42)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_all_negative(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_mixed_positive_negative(self):
        self.assertEqual(max_integer([-10, 0, 10, -20]), 10)

    def test_floats(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3]), 3.3)

    def test_strings(self):
        self.assertEqual(max_integer(["a", "b", "c"]), "c")

    def test_string_in_list(self):
        self.assertEqual(max_integer("hello"), "o")

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3])
