#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
    linescan.py Test Script for Travis CI

    linescan.py - Effortlessly read lines from a text file using any encoding
    Created 2013 Triangle717
    <http://triangle717.wordpress.com/>

    linescan.py is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    linescan.py is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with linescan.py. If not, see <http://www.gnu.org/licenses/>.
"""

import sys
import linescan


text = '''This is a line of text.
...
"Welcome to LEGO Island!"
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
"Ha ha, I scared you! You owe me a soda! Heheh"\n
'''

if __name__ == "__main__":

    try:
        # The command to write the test file
        command = sys.argv[1]
        if command == "write":
            with open("Thisisafile.txt", "wt") as f:
                f.write(text)
            sys.stdout.write("Thisisafile.txt has been written.")

    # Then scan it
    except IndexError:
        line = linescan.scanline("Thisisafile.txt", 5, "utf-8")
        sys.stdout.write(line)
        lines = linescan.scanlines("Thisisafile.txt", 8, 12, "cp1252")
        sys.stdout.write(lines)
        thisshouldbefalse = linescan.scanline("Thisisafile.txt", 55, "mbcs")
        sys.stdout.write(str(thisshouldbefalse))
