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
    
class TestCliWrapper(unittest.TestCase):


    def test_basic(self):
        """
        given a wrapper initialized with ls
        when calling cmd then expect to get the command back
        when calling read then expect the output of ls
        """
  
        cmd = "ls -ltr"
        wrp = CliWrapper(cmd)
        self.assertEqual(cmd, wrp.cmd(), "It is possible to get the command back")
        
        result = wrp.read()
        print "=====\n", result, "=====" 
        self.assertNotEqual("", result, "expected result for ls\n===\n" + str(result)
                         + "\n==="  )
                
    def test_interactive(self):
        """
        given a wrapper initialized with ftp
        when calling sendline_expectprompt
        then expect the output of the ftp command
        """
        cmd = "ftp"
        wrp = CliWrapper(cmd)
        prompt = "ftp> "
        
        wrp.expect (prompt) # initial prompt
        
        res = wrp.sendline_expectprompt('help', prompt)
        print res
        
        res = wrp.sendline_expectprompt('ls', prompt)
        print  (">>>", res, "<<<")        
        self.assertEqual("ls\r\nNot connected.\r\n", res, "ftp answer when not connected")

        wrp.sendline ('quit')

        print "end of test"
      
if __name__ == '__main__':
    unittest.main()