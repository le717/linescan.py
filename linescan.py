#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
    linescan.py
    Effortlessly read a text file using counting numbers.

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

# Restrict what can be imported using `from linescan import *`
__all__ = ["scan", "showerrors", "clearscans"]

# Store the user's scans for later retrieval
myScans = {}

# Do not raise an exception by default
showErrors = False


def showerrors(errorValue=False):
    """
    Set value to raise exception upon error.
    False (default): Do not raise exception.
    True: Raise exception.
    """
    global showErrors
    # Ensure only boolean values are given.
    # If they are not, assume default behavior.
    if type(errorValue) != bool:
        showErrors = False
    showErrors = errorValue


def clearscans():
    """Clear any stored scans"""
    global myScans
    myScans = {}


def scan(filename, lineno, endLine=None, encoding=None):
    """
    myFile: String of file to read.
    startLine: Integer of line you wish to read.
    endLine (optional): Integer of last line to want to read.
    Specify when reading multiple lines.
    encoding (optional): Specify a string file encoding to use.
    Defaults to default system encoding.
    """
    # 10 stored scans should be more than enough here,
    # considering this is targeted toward beginner programmers.
    if len(myScans) >= 10:
        clearscans()

    # Construct the comma-separated pointer for this file
    filePointer = "{0},{1}".format(filename, lineno)

    # Append the ending line if the user specifies one
    if endLine is not None:
        filePointer = "{0},{1}".format(filePointer, endLine)

    # If the pointer has been been used already, return the stored value
    if filePointer in myScans:
        return myScans[filePointer]

    # The pointer could not be found, proceed to read the file
    else:

        # Use the system default encoding if one is not specified.
        if encoding is None:
            encoding = locale.getpreferredencoding(False)

        # Perform the actual scan
        theScan = _scanner(filename, lineno, endLine, encoding)

        # Store the scan only if it is valid.
        if theScan:
            myScans[filePointer] = theScan

        # Send scan result back to the user
        return theScan


def _scanner(filename, startLine, endLine, encode):
    """Perform the actual scan for both single and multiple lines"""
    try:
        # Since line numbers start at 0,
        # get the starting line number.
        startLine -= 1

        # Open the file for reading using specified encoding
        with open(filename, "rt", encoding=encode) as f:

            # The user wants to read only one line.
            if endLine is None:
                lines = f.readlines()[startLine]

            # The user wants to read multiple lines.
            else:
                lines = f.readlines()[startLine:endLine]

                # Break the multiple lines from the returned list.
                lines = "".join(lines)

        # Remove any trailing new lines and return the text.
        lines = lines.strip()
        return lines

    except Exception as exc:

        # Raise an exception rather than returning False
        # if the user enabled that option.
        if showErrors:
            raise exc

        # Exceptions are not to be raised.
        return False
