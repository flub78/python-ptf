#!/usr/bin/python
# coding=utf-8
"""
Scan all files inside a directory.

And change their creation date. Windows only script.

./scan_dir.py --help
usage: scan_dir.py --older 10 dir
"""
import argparse
import os
import platform
import time
from datetime import datetime

# python -m pip install pywin32
import pywintypes, win32file, win32con

count = 0 # number of processed file

# Parse the CLI parameters
parser = argparse.ArgumentParser(description='Scan a directory.')

parser.add_argument('dirs', metavar='dir',  nargs='+', default=".",
                    help='an integer for the accumulator')

parser.add_argument('-r', '--recursive', action='store_true',
                    help='Also scan subdirectories')

parser.add_argument('-e', '--extension', 
                    help='Only looks for this extension')

parser.add_argument('--date', 
                    help='New file creation date, format: Aug 28 1999')

parser.add_argument('-o', '--older', 
                    help='Looks for files older than x days')

parser.add_argument('-de', '--del_empty', action='store_true',
                    help='Delete empty directories')

parser.add_argument("-v", "--verbose", help="increase output verbosity", action='store_true')

parser.add_argument('-a', '--action', 
                    help='Define the action to apply', choices=['display', 'delete', 'touch'])


def log(strg):
    """ simple log function
    """
    if (args.verbose):
        print(strg)
    
def changeFileCreationTime(fname, newtime):
    """
    Change a file creation time
    fname: file path
    newtime: new creation time in epoch
    """
    global count 
    
    count = count + 1
    wintime = pywintypes.Time(newtime + count * 60)
    winfile = win32file.CreateFile(fname, win32con.GENERIC_WRITE,
                                   win32con.FILE_SHARE_READ | 
                                   win32con.FILE_SHARE_WRITE | 
                                   win32con.FILE_SHARE_DELETE,
                                   None, 
                                   win32con.OPEN_EXISTING,
                                   win32con.FILE_ATTRIBUTE_NORMAL, 
                                   None)

    win32file.SetFileTime(      winfile,  wintime,  wintime,     wintime)
    winfile.close()
    # os.path.getctime returns a float, number of sec since Jan 1 1970
    # as time.time()
    log("\tcreated: %s" % time.ctime(os.path.getctime(fname)))

    
def process_dir(direct, newtime=0):
    """ process a directory
    """
    if (not os.path.isdir(direct)):
        log("\ndirectory " + direct +" not found")
        return
        
    # Loop across files in directory    
    for file in os.listdir(direct):
        fullpath = os.path.join(direct, file)
        
        # if an extension is set and a regular file does not match, just skip it
        if (not os.path.isdir(fullpath)): 
            # Does it match the extension ? For flexibility, just check for sub string
            if (args.extension and (not args.extension in fullpath)):
                # log(fullpath + " is not matching " + str(args.extension))
                break

        log(fullpath )
        
        # https://stackoverflow.com/questions/35124404/changing-directory-create-times-ctime-using-python-in-windows
        if (newtime and not os.path.isdir(fullpath)):
            changeFileCreationTime(fullpath, newtime)                

        if (os.path.isdir(fullpath) and args.recursive):
            process_dir(fullpath, newtime)
     
if __name__ == '__main__':

    args = parser.parse_args()

    if (platform.system() != "Windows"):  
        print("This script is only supported on Windows")
    else:   
        log ("parsing files and directories")
        log ("recursive=" + str(args.recursive))
        log ("extension=" + str(args.extension))

        if (args.date):                
            # TODO checks behavior for incorrect date formats
            dt = datetime.strptime(args.date, '%b %d %Y')
            t = time.mktime(dt.timetuple()) + dt.microsecond / 1E6
            t = t + 10 * 3600 # default hour is 10 am
        
        for d in args.dirs:
            process_dir(d, t)
        
        log ("done")

