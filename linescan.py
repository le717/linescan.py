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

import sys
import locale

# Get open() function if this is not Python 3.0 or higher
if sys.version_info < (3, 0):
    from io import open


def scanline(file, lineno, encode=None):
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
        with open(file, "rt", encoding=encode) as f:
            line = f.readlines()[lineno]

        # and remove the trailing new line.
        line = line.strip()

        # Send back the line
        return line

    except Exception:
        # Return False if there is any error.
        return False


def scanlines(file, startlineno, endlineno, encode=None):
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
        with open(file, "rt", encoding=encode) as f:
            lines = f.readlines()[startlineno:endlineno]

        # Next, we break the lines from the list,
        lines = "".join(lines)
        # and remove the trailing new line.
        lines = lines.strip()

        # Send back the lines
        return lines

    except Exception:
       # Return False if there is any error.
        return False

if __name__ == "__main__":
    # TODO: Possibly add example runs
    sys.exit(0)
