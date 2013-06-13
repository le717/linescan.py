#! /usr/bin/python
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
import sys

# Get open() function if this is not Python 3.0 or higher
if sys.version_info < (3,0):
    from io import open
# Block running on Python 2.5 or lower
if sys.version_info <= (2,5):
    sys.stdout.write('''\n\nYou are running Python {0}.
You must have Python 2.6 or newer to use linescan.py'''.format(sys.version[0:5]))
    exit()

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
        sys.stdout.write(encode + "\n")

        # Use the recommended with handle.
        with open(file, "rt", encoding=encode) as f:
            # Read specified line number.
            line = f.readlines()[lineno]
            line = line.rstrip()
            # Send back the line
        return line

    except Exception:
        # Return False if there is any error.
        return False

def scanlines(file, startlineno, endlineno, encode=None):
    '''Reads multiple lines from a file.'''

    # Because Python starts line numbers at 0.
    # Get starting line number.
    startlineno = startlineno - 1

    if encode == None:
        # If no encoding is specified, use encoding returned by
        # locale.getpreferredencoding(False)
        encode = locale.getpreferredencoding(False)

    # If an encoding is supplied, it will be used
    # (implied else clause here)

    # Debug to display encoding
    sys.stdout.write(encode + "\n")

    with open(file, "rt", encoding=encode) as f:
        # Scan the lines, store in a list.
        lines =  f.readlines()[startlineno:endlineno]
        # Remove the list from the lines
        lines = "".join(lines)
        # Remove trailing new line
        lines = lines.rstrip()
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