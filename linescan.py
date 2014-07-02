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
#__all__ = ["clearscans", "debug", "rescan", "scan", "showerrors"]
#__all__ = ["linescan", "rescan", "scan"]


class LineScan(object):

    def __init__(self):
        self.__myScans = {}
        self._showErrors = False
        self.__storedScans = 10
        self.__autoClearScans = True
        self.__filePointer = ""

        self.filename = ""
        self.lineno = None
        self.endline = None
        self.encoding = None
        self.errorvalue = False

    # ------- Public Methods ------- #
    def clearscans(self):
        """Clear any stored scans"""
        self.__myScans = {}

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
        ## Automatically clear the stored scans unless it is disabled
        #if _autoClearScans:
            #if self._numOfScans() >= self._storedScans:
                #self.clearscans()

        # Use the system default encoding if one is not specified.
        if encoding is None:
            encoding = locale.getpreferredencoding(False)

        # Create a file pointer
        filePointer = self._createPointer(self.filename, self.encoding,
            self.lineno, self.endline)

        # If the pointer has been used already, return the stored value
        if filePointer in self.__myScans:
            return self.__myScans[filePointer]

        # The pointer could not be found, proceed to scan the file
        else:
            # Perform the actual scan
            theScan = self._scanner()

            # Store the scan only if it is valid.
            if theScan:
                _myScans[filePointer] = theScan
            return theScan

    # ------- Private Methods ------- #
    def _setDetails(self, filename, lineno, endline, encoding, errorvalue):
        self.filename = filename
        self.lineno = lineno
        self.endline = endline
        self.encoding = encoding
        self.errorvalue = errorvalue

     def _clearDetails(self):
        self.filename = ""
        self.lineno = None
        self.endline = None
        self.encoding = None
        self.errorvalue = False

    def _numOfScans(self):
        """Reveal the number of stored scans"""
        return len(self.__myScans)

    def _checkBool(self, value):
        """Check if parameter `value` is True"""
        return value is True

    def _createPointer(self):
        """Construct the comma-separated pointer for the specified file"""
        self.__filePointer = "{0},{1}".format(self.encoding, self.lineno)

        # Append the ending line if one is specified
        if self.endline is not None:
            self.__filePointer = "{0},{1}".format(
                self.__filePointer, self.endline)

        # An encoding is always specified even if
        # the user did not provide one
        self.__filePointer = "{0},encode={1}".format(
            self.__filePointer, self.encoding)

    def _scanner(self):
        """Perform the actual scan"""
        try:
            # Since line numbers start at 0,
            # get the starting line number.
            self.startLine -= 1

            # Open the file for scanning using specified encoding
            with open(self.filename, "rt", encoding=self.encoding) as f:

                # The user wants to scan only one line.
                if self.endLine is None:
                    lines = f.readlines()[self.startLine]

                # The user wants to scan until the end of the file.
                elif self.endLine == "end":
                    lines = f.readlines()[self.startLine:]

                # The user wants to scan multiple specified lines.
                else:
                    lines = f.readlines()[self.startLine:self.endLine]

            # Break the multiple lines from the returned list.
            lines = "".join(lines)

            # Remove any trailing new lines and return the text.
            lines = lines.strip()
            return lines

        except Exception as exc:
            # Raise an exception rather than returning False
            # if the user enabled that option.
            if self.showErrors:
                raise exc

            # Otherwise, exceptions are not to be raised.
            else:
                return False


#def showerrors(errorvalue=False):
    #"""
    #Set value to raise exception upon error.
    #False (default): Do not raise exception.
    #True: Raise exception.
    #"""
    #global showErrors
    ## Check if parameter is True.
    ## Returned value will be the value of `showErrors`.
    #showErrors = _checkBool(errorvalue)


#def debug(scannum=False, storednum=False, autoclear=True):
    #"""Expose available debug values"""
    ## Check if parameters are True, meaning they are activated
    #scannum = _checkBool(scannum)
    #global _autoClearScans
    #_autoClearScans = _checkBool(autoclear)

    ## Check if `storednum` is an integer, signifying the
    ## number of stored scans is to be changed from the default (10)
    #global _storedScans
    #if type(storednum) == int:
        #_storedScans = storednum
    #else:
        #_storedScans = 10

    ## The user wishes to know how many stored scans there are.
    #if scannum:
        #return _numOfScans()


#def rescan(filename=None):
    #"""Rescan filename to update stored scans with file changes"""
    #filenames = []
    #for pointer in _myScans.keys():
        ## A file was not specified, rescan all stored scans
        #if filename is None:
            #filenames = list(_myScans.keys())
            #break

        ## A file was specified and the pointer has been already be stored
        #else:
            #if filename in pointer:
                #filenames = [pointer]
                #break

    ## The file specified has not been scanned before
    #if not filenames:

        ## Raise an exception if they are enabled
        #if showErrors:
            ## Raise FileNotFoundError exception on Python 3.3+
            #if sys.version_info >= (3, 3):
                #raise FileNotFoundError("{0} has not been previously scanned"  # noqa
                                        #.format(filename))

            ## Raise the old IOError on Python 3.2 and lower
            #elif sys.version_info <= (3, 2):
                #raise IOError("{0} has not been previously scanned".format(
                              #filename))

        ## Exceptions are not to be raised
        #else:
            #return False

    ## We have file(s) to rescan
    #for key in filenames:
        ## An ending line number was not specified
        #if len(key.split(",")) == 3:
            #fileName, startLine, encode = key.split(",")

            ## Only one line needs to be rescanned
            #endLine = None

        ## An ending line number (or "end" string) was specified
        #else:
            #fileName, startLine, endLine, encode = key.split(",")

        ## Trim encoding string for use,
        ## convert `endLine` to an integer under proper conditions
        #encode = re.sub(r"encode=", "", encode)
        #if (endLine is not None and endLine != "end"):
            #endLine = int(endLine)

        ## Now that we have the proper data, preform the rescan
        #newScan = _scanner(fileName, int(startLine), endLine, encode)

        ## Update the stored scan with the new scan
        #_myScans[key] = newScan

if __name__ != "__main__":
    linescan = LineScan()
