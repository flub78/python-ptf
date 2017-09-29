#!/usr/bin/python
# -*- coding:utf8 -*
#
# Simple python test
#
# to run it
# python test.py
#
import unittest
import os.path
                
class TestPath(unittest.TestCase):

    def test_path(self):
        "test __FILE__"
        print '__FILE__', __file__
        print 'abspath', os.path.abspath(__file__)
        print 'dirname', os.path.dirname(__file__)
        self.assertEqual(os.path.basename(__file__), 'test_failed.py', 'basename = ' + os.path.basename(__file__))

        path = os.path.abspath(__file__)
        libpath = os.path.abspath(os.path.join(path, os.pardir, 'lib'))
        print "libpath = ", libpath

if __name__ == '__main__':
    unittest.main()
