#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
    linescan.py - Effortlessly read lines from a text file using any encoding
    Created 2013-2014 Triangle717
    <http://Triangle717.WordPress.com/>

    Licensed under The MIT License
    <http://opensource.org/licenses/MIT/>
"""

from __future__ import print_function
import sys
import locale

# Get open() function if this is not Python 3.0 or higher
if sys.version_info < (3, 0):
    from io import open

# Store the user's scans for later retrieval
myScans = {}


def clearscans():
    """Clear any stored scans"""
    global myScans
    myScans = {}


def scan(myFile, startLine, endLine=None, encode=None):
    """
    myFile: the file to read.
    startLine: The line you wish to read.
    endLine (optional): The last line to want to read.
    Specify when reading multiple lines.
    encode (optional): Specify an file encoding to use.
    Defaults to default system encoding.
    """

    # Construct the comma-separated pointer for this file,
    filePointer = "{0},{1}".format(myFile, startLine)

    # Append the ending line if the user specifies one
    if endLine is not None:
        filePointer = "{0},{1}".format(filePointer, endLine)
    #print("DEBUG:", filePointer)

    # If the pointer has been been used, return the stored value
    if filePointer in myScans:
        return myScans[filePointer]

    # The pointer could not be found, proceed to read the file
    else:
        #print("DEBUG: Pointer not found")

        # Use the system default encoding, if one is not specified.
        if encode is None:
            encode = locale.getpreferredencoding(False)

        if endLine is None:
            theScan = _scanline(myFile, startLine, endLine, encode)
        else:
            #theScan = _scanlines(myFile, startLine, endLine)
            print("DEBUG: _scanlines()")

        myScans[filePointer] = theScan
        return theScan


def _scanline(myFile, startLine, endLine, encode):
    """Reads a single line from a file using a specified encoding.
    Falls back to default system encoding if None is specified."""
    try:
        # Since line numbers start at 0,
        # get the starting line number.
        startLine -= 1

        with open(myFile, "rt", encoding=encode) as f:
            if endLine is None:
                # Read only one line
                lines = f.readlines()[startLine]
            # Read multiple lines
            else:
                lines = f.readlines()[startLine:endLine]

        if endLine is not None:
            # Break the multiple lines from the list
            lines = "".join(lines)

        # Remove any trailing new lines.
        lines = lines.strip()
        return lines

    # Return False if there is any error.
    except Exception:
        return False


def scanlines(myfile, startlineno, endlineno, encode=None):
    """Reads multiple lines from a file."""
    try:
        # Since line numbers start at 0,
        # get the starting line number.
        startlineno -= 1

        if encode is None:
            # If no encoding is specified, use the default encoding;
            # Otherwise, use specified encoding
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

# Upon module import, clear stored scans if need be
if __name__ != "__main__":
    # 10 stored scans should be more than enough here,
    # considering this is targeted toward beginner programmers.
    if len(myScans) >= 10:
        clearscans()

if __name__ == "__main__":
    print('''
linescan.py - Effortlessly read lines from a text file using any encoding
Created 2013-2014 Triangle717
<http://Triangle717.WordPress.com/>

Licensed under The MIT License
<http://opensource.org/licenses/MIT/>

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
