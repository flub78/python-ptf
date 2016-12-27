#!/usr/bin/python
# -*- coding:utf8 -*
#
# Unit test for log analyzer
#

import unittest
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
        logfile = "/var/log/apache2/access.log.1"
        la = LogAnalyzer(logfile)
        self.assertEqual(logfile, la.filename())
        
        la.lookfor('toto')

#    def tearDown(self):
#        print "tearDown, cleaning local mess"

if __name__ == '__main__':
    unittest.main()