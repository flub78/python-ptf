#!/usr/bin/python
# -*- coding:utf8 -*
"""
Unit test for log analyzer
"""

import unittest
import sys
import os.path

# by convention the lib directory is at the same level than the tests directory
libpath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'lib'))
sys.path.append(libpath)

from log_analyzer import *

# def setUpModule():
#    print "setupModule, restore database into initial state"

# def tearDownModule():
#    print "Cleaning global mess"
    
class TestLogAnalyzer(unittest.TestCase):
        
    def test_invalid(self):
        """
        given a non existing log file
        when creating a log analyzer
        then an exception should be raised
        """
        logfile = "/dev/null/log"
        with self.assertRaises(Exception):
            la = LogAnalyzer(logfile)

        
    def test_basic(self):
        """
        given a log file
        when having a log analyzer
        then queries can be done on the log file
        """
        logfile = "access.log"
        la = LogAnalyzer(logfile)
        self.assertEqual(logfile, la.filename())
        
        la.lookfor('Apache')
        self.assertEqual(la.count(), 29, "Correct number of matches")
        self.assertEqual(la.size(), 240476, "Size of the log file")

if __name__ == '__main__':
    unittest.main()