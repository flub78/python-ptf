#!/usr/bin/python
# -*- coding:utf8 -*
"""
Simple python script

./script.py --help
usage: script.py [-h] [--sum] N [N ...]

Simple Python script with arguments.

positional arguments:
  N           an integer for the accumulator

optional arguments:
  -h, --help  show this help message and exit
  --sum       sum the integers (default: find the max)

"""
import argparse

parser = argparse.ArgumentParser(description='Simple Python script with arguments.')

parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')

parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

if __name__ == '__main__':

    args = parser.parse_args()
    print args.accumulate(args.integers)

    print "bye"

