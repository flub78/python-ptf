#!/usr/bin/python
# -*- coding:utf8 -*

""" CLI wrapper

An object to control a CLI tool
* launch it
* write on its standard input
* read stdout and stderr

"""

class CliWrapper:

    def __init__(self, cmd):
        """ Constructor """
        self._cmd = cmd
        
    def cmd(self):
        """ return the object command """
        return self._cmd
    
    
    