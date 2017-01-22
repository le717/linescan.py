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

        self.__file_name = ""
        self.__start_line = None
        self.__end_line = None
        self.__encoding = None

    # ------- Private Methods ------- #
    def __len__(self):
        """Expose the total number of files scanned.

        @returns {Integer}
        """
        return len(self.__scans)

    def __set_details(self, file_name, start_line, end_line, encoding):
        """Store scan details."""
        self.__file_name = file_name
        self.__start_line = start_line
        self.__end_line = end_line
        self.__encoding = encoding

    def __clear_details(self):
        """Reset scan details."""
        self.__file_name = ""
        self.__start_line = None
        self.__end_line = None
        self.__encoding = None

    def __check_bool(self, value):
        """Used to check if various options should be enabled."""
        return value is True

    def __create_pointer(self):
        """Construct the comma-separated pointer for the specified file."""
        return "{0},{1},{2},{3}".format(
            self.__file_name,
            self.__start_line,
            self.__end_line,
            self.__encoding
        )

    def __raise_exception(self, exc, generic=True):
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
            startLine = self.__start_line - 1

            # Open the file for scanning using specified encoding
            with open(self.__file_name, "rt", encoding=self.__encoding) as f:

                # The user wants to scan only one line.
                if self.__end_line is None:
                    lines = f.readlines()[startLine]

                # The user wants to scan until the end of the file.
                elif self.__end_line == "end":
                    lines = f.readlines()[startLine:]

                # The user wants to scan multiple specified lines.
                else:
                    lines = f.readlines()[startLine:self.__end_line]

            # Break the multiple lines from the returned list.
            lines = "".join(lines)

            return lines

        except Exception as exc:
            return self.__raise_exception(exc)

    # ------- Public Methods ------- #
    def clearscans(self):
        """Clear any stored scans."""
        self.__scans = {}
        self.__clear_details()

    def show_errors(self, error=False):
        """Enable exception raising instead of returning False on error.

        @param [error=False] Passing a value of True enables exception raising.
        """
        self.__enable_exceptions = self.__check_bool(error)

    def scan(self, file_name, start_line, end_line=None, encoding=None):
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

        # Store the scan details for use in other methods
        self.__set_details(file_name, start_line, end_line, encoding)

        # Create a unique pointer for this scan
        pointer = self.__create_pointer()

        # If the pointer has been used already, return the cached scan
        if pointer in self.__scans:
            return self.__scans[pointer]

        # The pointer could not be found, proceed to scan the file
        else:
            # Perform the actual scan
            theScan = self.__scanner()

            # Store the scan only if it is valid.
            if theScan:
                self.__scans[pointer] = theScan
            return theScan

    def rescan(self, file_name=None):
        """Rescan filename to update stored scans with file changes."""
        _filenames = []
        for pointer in self.__scans.keys():
            # A file was not specified, rescan all stored scans
            if file_name is None:
                _filenames = list(self.__scans.keys())
                break
            # A file was specified and the pointer has been already be stored
            else:
                if file_name in pointer:
                    _filenames = [pointer]
                    break

        # The file specified has not been scanned before
        if not _filenames:
            return self.__raise_exception(
                "{0} has not been previously scanned.".format(file_name),
                False
            )

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
            if endLine is not None and endLine != "end":
                endLine = int(endLine)

            # Now that we have the proper data, preform the rescan
            self.__set_details(fileName, int(startLine), endLine, encode)
            _newScan = self.__scanner()

            # Update the stored scan with the new scan
            self.__scans[_key] = _newScan
            return _newScan
