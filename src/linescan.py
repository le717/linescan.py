#! /usr/bin/python
# -*- coding: utf-8 -*-
"""Effortlessly read a text file using counting numbers.

Created 2013-2017 Caleb Ely
<https://CodeTri.net>

Licensed under The MIT License
<http://opensource.org/licenses/MIT/>

"""

from __future__ import unicode_literals

import re
import sys
import locale


# Grab Python 3.0+ open() function
if sys.version_info[:2] < (3, 0):
    from io import open

__all__ = ("LineScan")


class LineScan(object):
    """Main linescan class.

    Instance using linescan.LineScan()
    Primary entry point is scan() function.
    """

    def __init__(self):
        """Initialize private and public variables."""
        self.__scans = {}
        self.__enable_exceptions = False

        self.start_line = None
        self.end_line = None
        self.encoding = None
        self.file_name = ""

    # ------- Private Methods ------- #
    def __len__(self):
        """Expose the total number of files scanned.

        @returns {Integer}
        """
        return len(self.__scans)

    def __setDetails(self, filename, lineno, endline, encoding):
        """Store scan details."""
        self.start_line = lineno
        self.end_line = endline
        self.encoding = encoding
        self.file_name = filename

    def __clearDetails(self):
        """Reset scan details."""
        self.start_line = None
        self.end_line = None
        self.encoding = None
        self.file_name = ""

    def __check_bool(self, value):
        """Used to check if various options should be enabled."""
        return value is True

    def __create_pointer(self):
        """Construct the comma-separated pointer for the specified file."""
        filePointer = "{0},{1}".format(self.file_name, self.start_line)

        # Append the ending line if one is specified
        if self.end_line is not None:
            filePointer = "{0},{1}".format(
                filePointer, self.end_line)

        # An encoding is always specified even if
        # the user did not provide one
        filePointer = "{0},encode={1}".format(filePointer, self.encoding)
        return filePointer

    def __raiseException(self, exc, generic=True):
        """Handle errors per exception option."""
        # Raise an exception if they are enabled
        if self.__enable_exceptions:
            # A "generic" exception should be raised
            if generic:
                raise exc

            # A rescaning error should be raised instead
            # Raise FileNotFoundError exception on Python 3.3+
            if sys.version_info[:2] >= (3, 3):
                raise FileNotFoundError(exc)  # noqa

            # Raise the old IOError on Python 3.2 and lower
            else:
                raise IOError(exc)

        # If exceptions have not been enabled, simply return False
        return False

    def __scanner(self):
        """Perform the actual scan."""
        try:
            # Since line numbers start at 0, get the starting line number.
            # No need to do the same for the ending line,
            # as it is not modified
            startLine = self.start_line - 1

            # Open the file for scanning using specified encoding
            with open(self.file_name, "rt", encoding=self.encoding) as f:

                # The user wants to scan only one line.
                if self.end_line is None:
                    lines = f.readlines()[startLine]

                # The user wants to scan until the end of the file.
                elif self.end_line == "end":
                    lines = f.readlines()[startLine:]

                # The user wants to scan multiple specified lines.
                else:
                    lines = f.readlines()[startLine:self.end_line]

            # Break the multiple lines from the returned list.
            lines = "".join(lines)

            return lines

        except Exception as exc:
            return self.__raiseException(exc)

    # ------- Public Methods ------- #
    def clearscans(self):
        """Clear any stored scans."""
        self.__scans = {}
        self.__clearDetails()

    def show_errors(self, error=False):
        """Enable exception raising instead of returning False on error.

        @param [error=False] Passing a value of True enables exception raising.
        """
        self.__enable_exceptions = self.__checkBool(error)

    def scan(self, filename, lineno, endline=None, encoding=None):
        """Scan both single and multiple lines with option of custom encoding.

        filename (String): The desired file to scan.
        lineno (Integer): The line you wish to scan.
        endline (Optional, Integer, String): The last line to want to scan.
        Specify when scanning multiple lines. Specifying 'end' will scan
        the file from lineno to the end of the file.
        encoding (Optional, String): Specify a file encoding to use.
        Defaults to default system encoding.
        """
        # Use the system default encoding if one is not specified.
        if encoding is None:
            encoding = locale.getpreferredencoding(False)

        # Store the scan details for use elsewhere
        self.__setDetails(filename, lineno, endline, encoding)

        # Create a file pointer
        filePointer = self.__createPointer()

        # If the pointer has been used already, return the stored value
        if filePointer in self.__scans:
            return self.__scans[filePointer]

        # The pointer could not be found, proceed to scan the file
        else:
            # Perform the actual scan
            theScan = self.__scanner()

            # Store the scan only if it is valid.
            if theScan:
                self.__scans[filePointer] = theScan
            return theScan

    def rescan(self, filename=None):
        """Rescan filename to update stored scans with file changes."""
        _filenames = []
        for pointer in self.__scans.keys():
            # A file was not specified, rescan all stored scans
            if filename is None:
                _filenames = list(self.__scans.keys())
                break
            # A file was specified and the pointer has been already be stored
            else:
                if filename in pointer:
                    _filenames = [pointer]
                    break

        # The file specified has not been scanned before
        if not _filenames:
            return self.__raiseException("{0} has not been previously scanned."
                                         .format(filename), False)

        # We have file(s) to rescan
        for _key in _filenames:
            _keySplit = _key.split(",")
            # An ending line number was not specified
            if len(_keySplit) == 3:
                fileName, startLine, encode = _keySplit

                # Only one line needs to be rescanned
                endLine = None

            # An ending line number (or "end" string) was specified
            else:
                fileName, startLine, endLine, encode = _keySplit

            # Trim encoding string for use,
            # convert `endLine` to an integer under proper conditions
            encode = re.sub(r"encode=", "", encode)
            if (endLine is not None and endLine != "end"):
                endLine = int(endLine)

            # Now that we have the proper data, preform the rescan
            self.__setDetails(fileName, int(startLine), endLine, encode)
            _newScan = self.__scanner()

            # Update the stored scan with the new scan
            self.__scans[_key] = _newScan
            return _newScan
