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
    '''Reads a single line from a file.'''
    try:
        # Because Python starts line numbers at 0.
        lineno = lineno - 1
        # Use the recommended with handle.
        with open(file, "rt") as f:
            line = f.readlines()[lineno]
        return line
    except Exception:
        # Quietly suppress any errors.
        pass

def scanline_encode(file, lineno, *encode):
    '''Reads a single line from a file using a specified encoding.
    Falls back to default system encoding if None is specified.'''
    try:
        # Because Python starts line numbers at 0.
        lineno = lineno - 1

        for value in encode:
        # If no encoding is specified, use encoding returned by
        # sys.getdefaultencoding().
            if value == None:
               value = sys.getdefaultencoding()
            # Encoding was specified, use it.
            # "".join() allows input such as sys.getdefaultencoding()
            # if you REALLY wanted to make sure it uses it.
            else:
             value = "".join(encode)
            ##print(value)

        # Use the recommended with handle.
        with open(file, "rt", encoding=value) as f:
            # Read specified line number.
            line = f.readlines()[lineno]
        return line
    except Exception:
        # Quietly suppress any errors
        pass


def scanlines(file, startlineno, endlineno):
    '''Reads multiple lines from a file.'''
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

if __name__ == "__main__":
    # TODO: Possibly add example runs
    raise SystemExit

##print(sys.getdefaultencoding())
##scanline("NyanMe20.PiP", 1)
##scanline("NyanMe20.PiP", 1)
scanline_encode("NyanMe20.PiP", 16, None)
