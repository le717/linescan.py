#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
    linescan.py - Effortlessly read single lines from a text file
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

def scanline(file, lineno):
    '''Reads a single line from a file'''
    try:
        # Because Python starts line numbers at 0.
        lineno = lineno - 1
        # Use the recommended with handle.
        with open(file, "rt") as f:
            line = f.readlines()[lineno]
        #print(line)
        return line
    except Exception:
        # Quietly suppress any errors.
        pass

def scanline_encode(file, lineno, *encode):
    '''Reads a single line from a file using specified encoding'''
    # Because Python starts line numbers at 0.
    lineno = lineno - 1
    for arg in encode:
    # If no encoding is specified, use encoding returned by
    # sys.getdefaultencoding()
        if arg == None:
            arg == "".join(sys.getdefaultencoding())
            print(arg)
        # If encoding does not equal system encoding
        # MAY BE REMOVED
        elif arg != sys.getdefaultencoding():
            arg == "".join(encode)
            print(arg)
    # Use the recommended with handle.
        with open(file, "rt", encoding=arg) as f:
            # Read specified line number.
            line = f.readlines()[lineno]
            print(line)
    # return line

def scanlines(file, startlineno, endlineno):
    '''Reads multiple lines from a file'''
    # How many lines do we need to read?
    number_of_lines = len(endlineno - startlineno)
    # Because Python starts line numbers at 0.
    # Get starting line number.
    startlineno = startlineno - 1
    # Get ending line number.
    endlineno = endlineno - 1
    with open(file, "rt") as f:
        # Scan all lines, store in a list.
        lines =  f.readlines()[:]
        pass
 #   try:
#        pass
#    except Exception:
        # Quietly suppress any errors.
 #       pass
##print(sys.getdefaultencoding())
#scanline_encode("C:/temp/NyanMe20.PiP", 1, None)
scanline("C:/temp/NyanMe20.PiP", 1)