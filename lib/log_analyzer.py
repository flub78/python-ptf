#!/usr/bin/python
# -*- coding:utf8 -*

""" Log analyzer

Mainly an object to count and extract the occurences of a pattern inside a log file.

Simple implementation, the file is relodead for every query, works on a single file,
do not support log rotation or compressing

"""
import os.path
import re

class LogAnalyzer:

    def __init__(self, logfile):
        """ Constructor """
        self._logfile = logfile
        self._matches = []
        if not os.path.isfile(logfile):
            raise Exception("Log file not found")
        
    def filename(self):
        return self._logfile
    
    def lookfor(self, pattern):
        with open(self._logfile) as log:
            for line in log:
                if re.match(pattern, line):
                    print line
                else:
                    print "no match", pattern, " : ", line
        
    
    