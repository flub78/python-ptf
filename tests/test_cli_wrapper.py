#!/usr/bin/python
# -*- coding:utf8 -*
#
# Unit test for the CLI wrapper
#

import unittest
import sys
import os.path

# by convention the lib directory is at the same level than the tests directory
libpath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'lib'))
sys.path.append(libpath)

from cli_wrapper import *

# def setUpModule():
#    print "setupModule, restore database into initial state"

# def tearDownModule():
#    print "Cleaning global mess"
    
class TestCliWrapper(unittest.TestCase):


#    def setUp(self):
#        print "Setup, preparing for testing"
        
                
    def test_basic(self):
        cmd = "ls -ltr"
        wrp = CliWrapper(cmd)
        self.assertEqual(cmd, wrp.cmd(), "It is possible to get the command back")
        
#    def tearDown(self):
#        print "tearDown, cleaning local mess"

if __name__ == '__main__':
    unittest.main()