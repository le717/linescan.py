# /usr/bin/python3
# -*- coding: utf-8 -*-

"""
linescan.py Test Script for Travis CI
"""
import linescan
import sys

text = '''This is a line of text.
...
"The Brickster, the most dangerous man on the Island, is in jail now, but for how long?"
5
HELLO MY BABY, HELLO MY HONEY! HELLO MY RAG TIME GAL!
SEND ME A KISS BY WIRE, BABY MY HEART'S ON FIRE!
*changes channel*
"New! Hear LEGO minifigures talk for the first time in a LEGO Game!"
:| HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA
HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA
HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA
*finds different YT video*
"BOO!"
"AAAAAAAHHHHHHHHH!!!!!!!!!!"
"Ha ha, I scared you! You owe me a soda! Heheh"
'''

if __name__ == "__main__":
    command = sys.argv[1]

    # The command to write the test file
    if command == "write":
        with open("Thisisafile.txt", "wt") as f:
            f.write(text)

    # The command to scan the test file
    elif command == "scanme":
        line = linescan.scanline("Thisisafile.txt", 3, None)
        print(line)
        lines = linescan.scanlines("Thisisafile.txt", 5, 8, "cp1252")
        print(lines)
        thisshouldbefalse = linescan.scanline("Thisisafile.txt", 16, None)
        print(thisshouldbefalse)
