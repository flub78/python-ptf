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
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        """
        test string upper function
        given a constant string
        when calling upper
        then expect the string in upper case
        """
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        """
        test string isupper function
        given constant strings
        when calling isupper
        then expect true when the string is in upper case
        """
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        """
        test string split function
        given a constant strings containing spaces
        expect a list of token when called with default separators
        expect an error when called with a non string separator 
        """
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()