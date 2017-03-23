#!/usr/bin/python

from sys import argv
from lmd import LMD

if len(argv) < 2:
    print "Usage "+argv[0]+" <filename.LMD>"
    exit()
infile = argv[1]

# read input file
s = open(infile, 'r').read()

l = LMD(s)
print l
