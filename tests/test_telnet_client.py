#!/usr/bin/python
# -*- coding:utf8 -*
#
# Unit test for the Telnet client
#

import unittest
import sys
import os.path

# by convention the lib directory is at the same level than the tests directory
libpath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'lib'))
sys.path.append(libpath)

from telnet_client import *

# def setUpModule():
#    print "setupModule, restore database into initial state"

# def tearDownModule():
#    print "Cleaning global mess"
    
class TestTelnetClient(unittest.TestCase):


#    def setUp(self):
#        print "Setup, preparing for testing"
        
                
    def test_basic(self):
        """
        given a telnet client
        when not connected
        then connection should not return an error
        """
        cli = TelnetClient('localhost', 7)
        self.assertEqual(7, cli.connect(), "Connect")
        
#    def tearDown(self):
#        print "tearDown, cleaning local mess"

if __name__ == '__main__':
    unittest.main()