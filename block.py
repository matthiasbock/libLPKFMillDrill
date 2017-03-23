#!/usr/bin/python

from constants import *

#
# Represents one block
# in the array of blocks
# inside a LPKF Mill Drill file
#
class Block:
    #
    # Initialize new block
    # by parsing from string
    #
    def __init__(self, s):
        self.binary_source = ""
        if s == None:
            return
        c = 0
        while (c < len(s)) and (s[c] != LMD_BLOCK_END):
            self.binary_source += s[c]
            c += 1
        # include block end character (terminator)
        self.binary_source += s[c]

    #
    # Returns size of self block
    # including terminator
    #
    def getSize(self):
        return len(self.binary_source)
