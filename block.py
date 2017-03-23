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
        this.binary_source = ""
        c = 0
        while (s[c] != LMD_BLOCK_END) and (c < len(s)):
            this.binary_source += s[c]
            c += 1
        # include block end character (terminator)
        this.binary_source += s[c]

    #
    # Returns size of this block
    # including terminator
    #
    def getSize(self):
        return len(this.binary_source)
