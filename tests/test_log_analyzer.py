#!/usr/bin/python
# -*- coding:utf8 -*
#
# Unit test for log analyzer
#

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


#    def setUp(self):
#        print "Setup, preparing for testing"
        
        
    def test_invalid(self):
        logfile = "/dev/null/log"
        with self.assertRaises(Exception):
            la = LogAnalyzer(logfile)

        
    def test_basic(self):
        logfile = "access.log"
        la = LogAnalyzer(logfile)
        self.assertEqual(logfile, la.filename())
        
        la.lookfor('Apache')
        self.assertEqual(la.count(), 29, "Correct number of matches")
        self.assertEqual(la.size(), 240476, "Size of the log file")

#    def tearDown(self):
#        print "tearDown, cleaning local mess"

if __name__ == '__main__':
    unittest.main()