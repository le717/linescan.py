#! /usr/bin/python
# -*- coding: utf-8 -*-
"""Effortlessly read a text file using counting numbers.

Created 2013-2017 Caleb Ely
<https://CodeTri.net>

Licensed under The MIT License
<http://opensource.org/licenses/MIT/>

"""

from __future__ import unicode_literals
import locale


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
    def __str__(self):
        """Get information about currently scanned files.

        @returns {String}
        """
        return "TODO Write me!"

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
            raise FileNotFoundError(exc)

        # If exceptions have not been enabled, simply return False
        return False

    def __scanner(self):
        """Perform the actual scan."""
        try:
            # Since line numbers start at 0, get the starting line number.
            # No need to do the same for the ending line, as it is inclusive.
            start_line = self.__start_line - 1

            with open(self.__file_name, "rt", encoding=self.__encoding) as f:
                # The user wants to scan only one line.
                if self.__end_line == "single":
                    lines = f.readlines()[start_line]

                # The user wants to scan until the end of the file.
                elif self.__end_line == "end":
                    lines = f.readlines()[start_line:]

                # The user wants to scan multiple specified lines.
                else:
                    lines = f.readlines()[start_line:self.__end_line]
            return "".join(lines)

        except Exception as exc:
            return self.__raise_exception(exc)

    # ------- Public Methods ------- #
    def clear(self, file_name=None):
        """Clear any stored scans.

        @param {NoneType|String} [file_name=None] -
            Pass `None` to clear all scans.
            Giving a file name will attempt
            to clear all cached lines from
            that file.
        @returns {Boolean} Always returns True.
        """
        # We want to clear the whole cache.
        if file_name is None:
            self.__scans = {}
            return True

        # We only want to clear one file.
        for k in list(self.__scans):
            if file_name in k:
                # We found the file, clear it from the cache.
                del self.__scans[k]
                self.__clear_details()
        return True

    def show_errors(self, enable=False):
        """Enable exception raising instead of returning False on error.

        @param {Boolean} [enable=False] - Passing a value of True
                                          enables exception raising.
        """
        self.__enable_exceptions = enable

    def scan(self, file_name, start_line, end_line="single", encoding=None):
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

        # Set the scan details for use in other methods.
        self.__set_details(file_name, start_line, end_line, encoding)

        # If our pointer has been used already, return the cached scan.
        pointer = self.__create_pointer()
        if pointer in self.__scans:
            return self.__scans[pointer]

        # The pointer could not be found, proceed to scan the file.
        else:
            # Perform the scan and store it only if it is valid.
            the_scan = self.__scanner()
            if the_scan:
                self.__scans[pointer] = the_scan
            return the_scan

    def rescan(self, file_name=None):
        """Rescan filename to update stored scans with file changes."""
        _filenames = []
        for pointer in self.__scans.keys():
            # A file was not specified, rescan all stored scans.
            if file_name is None:
                _filenames = list(self.__scans.keys())
                break
            # A file was specified and the pointer has been already be stored.
            else:
                if file_name in pointer:
                    _filenames = [pointer]
                    break

        # The file specified has not been scanned before.
        if not _filenames:
            return self.__raise_exception(
                "{0} has not been previously scanned.".format(file_name),
                False
            )

        # We have file(s) to rescan.
        for _key in _filenames:
            _key_split = _key.split(",")
            file_name, start_line, end_line, encode = _key_split

            # Convert the ending line to an integer if needed
            if end_line.isnumeric():
                end_line = int(end_line)

            # Now that we have the proper data, preform the rescan.
            self.__set_details(file_name, int(start_line), end_line, encode)
            new_scan = self.__scanner()

            # Update the stored scan with the new scan.
            self.__scans[_key] = new_scan
            return new_scan
