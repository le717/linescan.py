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
import re

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


def _numOfScans():
    """Reveal the number of stored scans"""
    return len(_myScans)


def _checkBool(value):
    """Check if parameter `value` is True"""
    return value is True


def clearscans():
    """Clear any stored scans"""
    global _myScans
    _myScans = {}


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


def rescan(filename):
    """Rescan filename to update stored scans with file changes"""
    for key in _myScans.keys():

        # Ensure the pointer has been already used
        if filename in key:

            # An ending line number was not specified
            if len(key.split(",")) == 3:
                fileName, startLine, encode = key.split(",")

                # Only one line needs to be updated
                endLine = None

            # An ending line number (or "end" string) was specified
            else:
                fileName, startLine, endLine, encode = key.split(",")

            # Now that we have the proper information, preform the rescan
            newScan = _scanner(fileName, int(startLine), endLine,
                               re.sub(r"encode=", "", encode))

            # Update the stored scan with the new information
            _myScans[key] = newScan


def _createPointer(filename, encoding, lineno, endline=None):
    """Construct the comma-separated pointer for the specified file"""
    filePointer = "{0},{1}".format(filename, lineno)

    # Append the ending line if one is specified
    if endline is not None:
        filePointer = "{0},{1}".format(filePointer, endline)

    # An encoding is always specified even if the user did not provide one
    filePointer = "{0},encode={1}".format(filePointer, encoding)
    return filePointer


def scan(filename, lineno, endline=None, encoding=None):
    """
    filename (String): The desired file to scan.
    lineno (Integer): The line you wish to scan.
    endline (Optional, Integer, String): The last line to want to scan.
    Specify when scanning multiple lines. Specifing 'end' will scan
    the file from lineno to the end of the file.
    encoding (Optional, String): Specify a file encoding to use.
    Defaults to default system encoding.
    """
    # Automatically clear the stored scans unless it is disabled
    if _autoClearScans:
        if _numOfScans() >= _storedScans:
            clearscans()

    # Use the system default encoding if one is not specified.
    if encoding is None:
        encoding = locale.getpreferredencoding(False)

    # Create a file pointer
    filePointer = _createPointer(filename, encoding, lineno, endline)

    # If the pointer has been used already, return the stored value
    if filePointer in _myScans:
        return _myScans[filePointer]

    # The pointer could not be found, proceed to scan the file
    else:
        # Perform the actual scan
        theScan = _scanner(filename, lineno, endline, encoding)

        # Store the scan only if it is valid.
        if theScan:
            _myScans[filePointer] = theScan
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
