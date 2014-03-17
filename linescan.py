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

import sys
import locale

# Get open() function if this is not Python 3.0 or higher
if sys.version_info < (3, 0):
    from io import open

# Restrict what can be imported using `from linescan import *`
__all__ = ["clearscans", "debug", "scan", "showerrors"]

# Store the user's scans for later retrieval
_myScans = {}

# Do not raise an exception by default
showErrors = False

# Default number of scans to store
_storedScans = 10

# Automatically clear stored scans
_autoClearScans = True


def showerrors(errorvalue=False):
    """
    Set value to raise exception upon error.
    False (default): Do not raise exception.
    True: Raise exception.
    """
    global showErrors
    # Check if parameter is True.
    # Returned value will be the value of `showErrors`.
    showErrors = _checkBool(errorvalue)


def clearscans():
    """Clear any stored scans"""
    global _myScans
    _myScans = {}


def debug(scannum=False, storednum=False, autoclear=True):
    """Expose available debug values"""
    # Check if parameters are True, meaning they are activated
    scannum = _checkBool(scannum)
    global _autoClearScans
    _autoClearScans = _checkBool(autoclear)

    # Check if storednum is an integer, signifying the
    # number of stored scans is to be changed from the default (10)
    global _storedScans
    if type(storednum) == int:
        _storedScans = storednum
    else:
        _storedScans = 10

    # The user wishes to know how many stored scans there are.
    if scannum:
        return _numOfScans()


def _numOfScans():
    """Reveal the number of stored scans"""
    return len(_myScans)


def _checkBool(value):
    """Check if parameter `value` is True"""
    return value is True


def scan(filename, lineno, endline=None, encoding=None):
    """
    myFile (String): The desired file to scan.
    startLine (Integer): The line you wish to scan.
    endLine (Optional, Integer): The last line to want to scan.
    Specify when scanning multiple lines.
    encoding (Optional, String): Specify a file encoding to use.
    Defaults to default system encoding.
    """
    # Automatically clear the stored scans unless it is disabled
    if _autoClearScans:
        if _numOfScans() >= _storedScans:
            clearscans()

    # Construct the comma-separated pointer for this file
    filePointer = "{0},{1}".format(filename, lineno)

    # Append the ending line if the user specifies one
    if endline is not None:
        filePointer = "{0},{1}".format(filePointer, endline)

    # If the pointer has been been used already, return the stored value
    if filePointer in _myScans:
        return _myScans[filePointer]

    # The pointer could not be found, proceed to read the file
    else:
        # Use the system default encoding if one is not specified.
        if encoding is None:
            encoding = locale.getpreferredencoding(False)

        # Perform the actual scan
        theScan = _scanner(filename, lineno, endline, encoding)

        # Store the scan only if it is valid.
        if theScan:
            _myScans[filePointer] = theScan

        # Send scan result back to the user
        return theScan


def _scanner(fileName, startLine, endLine, encode):
    """Perform the actual scan"""
    try:
        # Since line numbers start at 0,
        # get the starting line number.
        startLine -= 1

        # Open the file for scanning using specified encoding
        with open(fileName, "rt", encoding=encode) as f:

            # The user wants to scan only one line.
            if endLine is None:
                lines = f.readlines()[startLine]

            # The user wants to scan until the end of the file.
            elif endLine == "end":
                lines = f.readlines()[startLine:]

            # The user wants to scan multiple specified lines.
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

        # Otherwise, exceptions are not to be raised.
        return False
