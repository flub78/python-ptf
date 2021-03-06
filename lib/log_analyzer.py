#!/usr/bin/python
# -*- coding:utf8 -*

""" Log analyzer

Mainly an object to count and extract the occurences of a pattern inside a log file.

Simple implementation, the file is relodead for every query, works on a single file,
do not support log rotation or compressing

"""
import os.path
import os
import re

class LogAnalyzer:

    def __init__(self, logfile):
        """ Constructor """
        self._logfile = logfile
        self._matches = []
        if not os.path.isfile(logfile):
            raise Exception("Log file not found")
        
    def filename(self):
        """ geter for log filen name """
        return self._logfile
    
    def lookfor(self, pattern):
        """ look for a pattern and fill an array of matching lines"""
        regexp = re.compile(pattern)
        with open(self._logfile) as log:
            for line in log:
                if regexp.search(line):
                    self._matches.append(line)
#                    print "match    ", pattern, " ", line
#                else:
#                    print "no match ", pattern, " ", line
        
    def count(self):
        """ returns the number of matches of the previous search"""
        return len(self._matches)
    
    def size(self):
        """ size of the log file in bytes """
        return os.stat(self._logfile).st_size
    
    