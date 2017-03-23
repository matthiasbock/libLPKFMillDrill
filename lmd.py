#!/usr/bin/python

from block import Block

#
# Function to simply LMD header parsing
#
# Reads until end of line (0x0A 0x0D) and
# returns string aswell as cursor at index of 0x0A
#
def read_string(haystack, cursor):
    result = ""
    while haystack[cursor] != '\x0A':
        result += haystack[cursor]
        cursor += 1
    return result, cursor

#
# Represents LPKF Mill Drill File
# and all of its' contents
#
# Provides functions to import and export
# the contained fabrication data
#
class LMD:
    def __init__(self, s=None):
        # initialize class attributes
        this.header = []
        this.blocks = []
        this.source = s
        if s != None:
            this.parse()

    def parse(self, s=None, debug=True):
        # overwrite possible pre-defined source
        if s != None:
            this.source = s

        # cancel if no source available
        if this.source == None:
            return

        # clear class attributes
        this.header = []
        this.blocks = []
        cursor = 0

        # parse header
        end_of_header = False
        while not end_of_header:
            # puts cursor to first byte behind string end
            s, cursor = read_string(this.source, cursor)
            this.header.append(s)

            # line break expected
            assert this.source[cursor:cursor+2] == "\x0A\x0D"
            cursor += 2

            # end of header marker
            end_of_header = (this.source[cursor] == '\x1A') and (cursor < len(this.source))

        # skip end of header marker
        cursor += 1

        if debug:
            print "Parsed "+str(len(this.header))+" lines of header"
            print this.header

        # parse blocks
        while (cursor < len(this.source)):
            # instantiate a new block by parsing a substring
            b = Block(this.source[cursor:])

            this.blocks.append(b)

            cursor += b.getSize()
