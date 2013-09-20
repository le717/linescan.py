#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
    linescan.py - Effortlessly read lines from a text file using any encoding
    Created 2013 Triangle717
    <http://Triangle717.WordPress.com/>

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

from __future__ import print_function
import sys
import locale

# Get open() function if this is not Python 3.0 or higher
if sys.version_info < (3, 0):
    from io import open

#TODO: Store and retrieve scans so they are not lost upon a new scan.


def scanline(myfile, lineno, encode=None):
    """Reads a single line from a file using a specified encoding.
    Falls back to default system encoding if None is specified."""
    try:
        # Since line numbers start at 0,
        # get the starting line number.
        lineno = lineno - 1

        if encode is None:
            # If no encoding is specified, use the default encoding;
            # Otherwise, use speficied encoding
            encode = locale.getpreferredencoding(False)

        # Using the recommended with handle, read the specified line number,
        with open(myfile, "rt", encoding=encode) as f:
            line = f.readlines()[lineno]

        # and remove the trailing new line.
        line = line.strip()
        return line

    # Return False if there is any error.
    except Exception:
        return False


def scanlines(myfile, startlineno, endlineno, encode=None):
    """Reads multiple lines from a file."""
    try:
        # Since line numbers start at 0,
        # get the starting line number.
        startlineno = startlineno - 1

        if encode is None:
            # If no encoding is specified, use the default encoding;
            # Otherwise, use speficied encoding
            encode = locale.getpreferredencoding(False)

        # Using the recommended with handle, read the specified lines.
        with open(myfile, "rt", encoding=encode) as f:
            lines = f.readlines()[startlineno:endlineno]

        # Next, we break the lines from the list,
        lines = "".join(lines)
        # and remove the trailing new line.
        lines = lines.strip()
        return lines

    # Return False if there is any error.
    except Exception:
        return False

if __name__ == "__main__":
    print('''
linescan.py Created 2013 Triangle717
<http://Triangle717.WordPress.com/>
Released under the GNU General Public License version 3
<http://www.gnu.org/licenses/>.

Example linescan.py usage:

from __future__ import print_function
import linescan

# Read a single line using UTF-8 encoding
myline = linescan.scanline("MyFile.txt", 5, "utf-8")
print(mylines)

# Read multiple lines using system default encoding
mytwolines = linescan.scanline("MyFile.txt", 2, 5)
print(mytwolines)
''')
    sys.exit(0)
