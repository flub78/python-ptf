#!/usr/bin/python
# -*- coding:utf8 -*

""" CLI wrapper

An object to control a CLI tool
* launch it
* write on its standard input
* read stdout and stderr

The implementaiton is mainly an encapsulation of a pexpect spawned process.

It is better to have a class around it anyway to create more business oriented
methods to group sending messages to the CLI tool, getting and analyzing the results and
processing the errors.

"""
import pexpect

class CliWrapper:

    def __init__(self, cmd):
        """ Constructor """
        self._cmd = cmd
        self._process = pexpect.spawn (cmd)
        
    def cmd(self):
        """ return the object command """
        return self._cmd
    
    def expect(self, regexp):
        """ wait for a pattern from the CLI command """
        return self._process.expect(regexp)
        
    def sendline(self, line):
        """ Send character to the tool """
        return self._process.sendline(line)
    
    def sendline_expectprompt(self, line, pattern):
        """ send a line, wait for the prompt, return the result """
        self.sendline(line)
        self.expect(pattern)
        return self.before()
           
    def before(self):
        """ return character sent before the match """
        return self._process.before
    
    def read(self):
        """ match until EOF """
        self.expect(pexpect.EOF)
        return self.before()
            
        