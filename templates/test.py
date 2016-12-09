#!/usr/bin/python
# -*- coding:utf8 -*
#
# Simple python test
#
# to run it
# python test.py
#
# to run all the tests in a directory
# python -m unittest discover <directory>
#
# or if you are in the directory
# python -m unittest discover
#
# To run the tests and generate Junit xml test results
# py.test --junitxml results.xml test*.py
#
# Scenario ID: 42
# Given: no preconditions
# When: executing the script
# Then: no error should be reported
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        "test string upper function"
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()