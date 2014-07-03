#! /usr/bin/python
# -*- coding: utf-8 -*-
"""Effortlessly read a text file using counting numbers.

Created 2013-2014 Triangle717
<http://Triangle717.WordPress.com/>

Licensed under The MIT License
<http://opensource.org/licenses/MIT/>

"""

import sys
import locale
# import re

# Get open() function if this is not Python 3.0 or higher
if sys.version_info[:2] < (3, 0):
    from io import open

# Restrict what can be imported using `from linescan import *`
# __all__ = ["clearscans", "debug", "rescan", "scan", "showerrors"]
# __all__ = ["linescan", "rescan", "scan"]
__all__ = ("LineScan")


class LineScan(object):

    def __init__(self):

        self.__myScans = {}
        self.__showErrors = False
        self.__storedScans = 10
        self.__autoClearScans = True

        self.filename = ""
        self.lineno = None
        self.endline = None
        self.encoding = None
        self.errorvalue = False
        self.cleanscans = False

    # ------- Public Methods ------- #
    def clearscans(self):
        """Clear any stored scans."""
        self.__myScans = {}

    def cleanscans(self, cleanscan):
        """Set value to remove new line characters from both ends of a line."""
        self.cleanscans = self.__showErrors = self._checkBool(cleanscan)

    def showerrors(self, errorvalue=False):
        """
        Set value to raise exception upon error.
        False (default): Do not raise exception.
        True: Raise exception.
        """
        # Returned value will become the setting value.
        self.__showErrors = self._checkBool(errorvalue)

    def scan(self, filename, lineno, endline=None, encoding=None):
        """
        filename (String): The desired file to scan.
        lineno (Integer): The line you wish to scan.
        endline (Optional, Integer, String): The last line to want to scan.
        Specify when scanning multiple lines. Specifying 'end' will scan
        the file from lineno to the end of the file.
        encoding (Optional, String): Specify a file encoding to use.
        Defaults to default system encoding.
        """
        # Store the scan details for use elsewhere
        self._setDetails(filename, lineno, endline, encoding)

        # Automatically clear the stored scans unless it is disabled
        if self.__autoClearScans:
            if self._numOfScans() >= self.__storedScans:
                self.clearscans()

        # Use the system default encoding if one is not specified.
        if encoding is None:
            encoding = locale.getpreferredencoding(False)

        # Create a file pointer
        _filePointer = self._createPointer()

        # If the pointer has been used already, return the stored value
        if _filePointer in self.__myScans:
            return self.__myScans[_filePointer]

        # The pointer could not be found, proceed to scan the file
        else:
            # Perform the actual scan
            theScan = self._scanner()

            # Store the scan only if it is valid.
            if theScan:
                self.__myScans[_filePointer] = theScan
            return theScan

    def debug(self, scannum=False, storednum=False, autoclear=True):
        """Expose available debug values."""
        # Check if parameters are activated
        scannum = self._checkBool(scannum)
        self.__autoClearScans = self._checkBool(autoclear)

        # Check if `storednum` is an integer, signifying the
        # number of stored scans is to be changed from the default (10)
        if type(storednum) == int:
            self.__storedScans = storednum
        else:
            self.__storedScans = 10

        # The user wishes to know how many stored scans there are.
        if scannum:
            return self._numOfScans()

    def rescan(self, filename=None):
        """Rescan filename to update stored scans with file changes."""
        _filenames = []
        for pointer in self.__myScans.keys():
            # A file was not specified, rescan all stored scans
            if filename is None:
                _filenames = list(self.__myScans.keys())
                break
            # A file was specified and the pointer has been already be stored
            else:
                if filename in pointer:
                    _filenames = [pointer]
                    break

        # The file specified has not been scanned before
        if not _filenames:
            # Raise an exception if they are enabled
            if self.__showErrors:
                # Raise FileNotFoundError exception on Python 3.3+
                if sys.version_info[:2] >= (3, 3):
                    raise FileNotFoundError(  # noqa
                        "{0} has not been previously scanned".format(filename))
                # Raise the old IOError on Python 3.2 and lower
                elif sys.version_info[:2] <= (3, 2):
                    raise IOError("{0} has not been previously scanned"
                                  .format(filename))
            # Exceptions are not to be raised
            return False

    # ------- Private Methods ------- #
    def _setDetails(self, filename, lineno, endline, encoding):
        """Store scan details."""
        self.filename = filename
        self.lineno = lineno
        self.endline = endline
        self.encoding = encoding

    def _clearDetails(self):
        """Reset scan details."""
        self.filename = ""
        self.lineno = None
        self.endline = None
        self.encoding = None

    def _numOfScans(self):
        """Expose the number of stored scans."""
        return len(self.__myScans)

    def _checkBool(self, value):
        """Used to check if various options should be enabled."""
        return value is True

    def _createPointer(self):
        """Construct the comma-separated pointer for the specified file."""
        _filePointer = "{0},{1}".format(self.filename, self.lineno)

        # Append the ending line if one is specified
        if self.endline is not None:
            _filePointer = "{0},{1}".format(
                _filePointer, self.endline)

        # An encoding is always specified even if
        # the user did not provide one
        _filePointer = "{0},encode={1}".format(_filePointer, self.encoding)
        return _filePointer

    def _scanner(self):
        """Perform the actual scan."""
        try:
            # Since line numbers start at 0, get the starting line number.
            # No need to do the same for the ending line,
            # as it is not modified
            _startLine = self.lineno - 1

            # Open the file for scanning using specified encoding
            with open(self.filename, "rt", encoding=self.encoding) as f:

                # The user wants to scan only one line.
                if self.endline is None:
                    lines = f.readlines()[_startLine]

                # The user wants to scan until the end of the file.
                elif self.endline == "end":
                    lines = f.readlines()[_startLine:]

                # The user wants to scan multiple specified lines.
                else:
                    lines = f.readlines()[_startLine:self.endline]

            # Break the multiple lines from the returned list.
            # TODO Shouldn't this be indented one level?
            lines = "".join(lines)

            # Remove any trailing new lines and return the text.
            if self.cleanscans:
                lines = lines.strip()
            return lines

        except Exception as exc:
            # Raise an exception rather than returning False
            # if the user enabled that option.
            if self.__showErrors:
                raise exc

            # Otherwise, exceptions are not to be raised.
            else:
                return False

# def rescan(filename=None):
    # """Rescan filename to update stored scans with file changes."""
    # filenames = []
    # for pointer in _myScans.keys():
        ## A file was not specified, rescan all stored scans
        # if filename is None:
            # filenames = list(_myScans.keys())
            # break

        ## A file was specified and the pointer has been already be stored
        # else:
            # if filename in pointer:
                # filenames = [pointer]
                # break

    ## The file specified has not been scanned before
    # if not filenames:

        ## Raise an exception if they are enabled
        # if showErrors:
            ## Raise FileNotFoundError exception on Python 3.3+
            # if sys.version_info[:2] >= (3, 3):
                # raise FileNotFoundError("{0} has not been previously scanned"  # noqa
                                        # .format(filename))

            ## Raise the old IOError on Python 3.2 and lower
            # elif sys.version_info[:2] <= (3, 2):
                # raise IOError("{0} has not been previously scanned".format(
                              # filename))

        ## Exceptions are not to be raised
        # else:
            # return False

    ## We have file(s) to rescan
    # for key in filenames:
        ## An ending line number was not specified
        # if len(key.split(",")) == 3:
            # fileName, startLine, encode = key.split(",")

            ## Only one line needs to be rescanned
            # endLine = None

        ## An ending line number (or "end" string) was specified
        # else:
            # fileName, startLine, endLine, encode = key.split(",")

        ## Trim encoding string for use,
        ## convert `endLine` to an integer under proper conditions
        # encode = re.sub(r"encode=", "", encode)
        # if (endLine is not None and endLine != "end"):
            # endLine = int(endLine)

        ## Now that we have the proper data, preform the rescan
        # newScan = _scanner(fileName, int(startLine), endLine, encode)

        ## Update the stored scan with the new scan
        # _myScans[key] = newScan
