#!/usr/bin/python
# -*- coding:utf8 -*
#
# Another simple python test
# to make a suite
#
# Scenario ID: 43
# Given: no preconditions
# When: executing the script
# Then: no error should be reported

import unittest

def setUpModule():
    print "setupModule, restore database into initial state"

def tearDownModule():
    print "Cleaning global mess"
    
class TestStringMethods(unittest.TestCase):


    def setUp(self):
        print "Setup, preparing for testing"
        
        
    def test_equal(self):
        self.assertEqual('FOO', 'FOO')

    def test_integer_equal(self):
        self.assertEqual(6, 2 * 3, "testing integer arithmetic")
        
        
    def tearDown(self):
        print "tearDown, cleaning local mess"

if __name__ == '__main__':
    unittest.main()