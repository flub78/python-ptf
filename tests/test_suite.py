#!/usr/bin/python
# -*- coding:utf8 -*
#
# Some experiment to create a test suite.
# not completed yet, as it is easy to run all the tests from a directory 
#
import unittest
import test_1
import test_2

def suite():
    tests = ['first', 'second']
    
if __name__ == '__main__':
    print "main test suite"
    # unittest.main()
