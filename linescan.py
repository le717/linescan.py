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

import locale

def scanline_no_encode(file, lineno):
    '''Reads a single line from a file.'''
    try:
        # Because Python starts line numbers at 0.
        lineno = lineno - 1
        # Use the recommended with handle.
        with open(file, "rt") as f:
            line = f.readlines()[lineno]
        # Send back the line
        return line

    # Quietly suppress any errors
    except Exception:
        return False

def scanline(file, lineno, encode=None):
    '''Reads a single line from a file using a specified encoding.
    Falls back to default system encoding if None is specified.'''

    try:
        # Because Python starts line numbers at 0.
        lineno = lineno - 1

        if encode == None:
            # If no encoding is specified, use encoding returned by
            # locale.getpreferredencoding(False)
            encode = locale.getpreferredencoding(False)

        # If an encoding is supplied, it will be used
        # (implied else clause here)

        # Debug to display encoding
        print(encode)

        # Use the recommended with handle.
        with open(file, "rt", encoding=encode) as f:
            # Read specified line number.
            line = f.readlines()[lineno]
            # Send back the line
        return line

    except Exception:
        # Return False if there is any error.
        return False


def scanlines_no_encode(file, startlineno, endlineno):
    '''Reads multiple lines from a file.'''
    # Because Python starts line numbers at 0.
    # Get starting line number.
    startlineno = startlineno - 1
    # Get ending line number.
    endlineno = endlineno - 1

    with open(file, "rt") as f:
        # Scan the lines, store in a list.
        lines =  f.readlines()[startlineno:endlineno]
        # Remove the list from the lines
        lines = "".join(lines)
    # Send back the lines
    return lines

def scanlines(file, startlineno, endlineno, encode=None):
    '''Reads multiple lines from a file.'''

    # Because Python starts line numbers at 0.
    # Get starting line number.
    startlineno = startlineno - 1
    # Get ending line number.
    endlineno = endlineno - 1

    if encode == None:
        # If no encoding is specified, use encoding returned by
        # locale.getpreferredencoding(False)
        encode = locale.getpreferredencoding(False)

    # If an encoding is supplied, it will be used
    # (implied else clause here)

    # Debug to display encoding
    print(encode)

    with open(file, "rt", encoding=encode) as f:
        # Scan the lines, store in a list.
        lines =  f.readlines()[startlineno:endlineno]
        # Remove the list from the lines
        lines = "".join(lines)
    # Send back the lines
    return lines

 #   try:
#        do whatever
#    except Exception:
        # Quietly suppress any errors.
 #       return False

if __name__ == "__main__":
    # TODO: Possibly add example runs
    raise SystemExit