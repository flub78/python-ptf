#!/usr/bin/python
# -*- coding:utf8 -*

""" Telnet client

a client to send an receive lines from a telnet server

"""

class TelnetClient:

    def __init__(self, host, port):
        """ Constructor """
        self._host = host
        self._port = port
        
    def connect(self):
        """ Connect to the server """
        return self._port
    
    
    