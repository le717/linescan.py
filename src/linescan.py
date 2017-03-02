#! /usr/bin/python
# -*- coding: utf-8 -*-
"""Effortlessly read a text file using counting numbers.

Created 2013-2017 Caleb Ely
<https://CodeTri.net>

Licensed under The MIT License
<http://opensource.org/licenses/MIT/>

"""

import locale


__all__ = ("LineScan")


class LineScan(object):
    """Main linescan class.

    Instance using linescan.LineScan()
    Primary entry point is scan() function.
    """

    def __init__(self):
        """Initialize private and public variables."""
        self.__enable_exceptions = False

        self.__file_name = ""
        self.__start_line = None
        self.__end_line = None
        self.__encoding = None

    # ------- Private Methods ------- #
    def __set_details(self, file_name, start_line, end_line, encoding):
        """Store scan details.

        @private
        """
        self.__file_name = file_name
        self.__start_line = start_line
        self.__end_line = end_line
        self.__encoding = encoding

    def __raise_exception(self, exc, generic=True):
        """Handle errors per exception option.

        @private
        """
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
        """Perform the actual scan.

        @private
        """
        try:
            # Since line numbers start at 0, get the starting line number.
            # No need to do the same for the ending line, as it is inclusive.
            start_line = self.__start_line - 1

            with open(self.__file_name, "rt", encoding=self.__encoding) as f:
                # The user wants to scan until the end of the file
                if self.__end_line == "end":
                    lines = f.readlines()[start_line:]

                # The user wants to scan one or more lines
                else:
                    lines = f.readlines()[start_line:self.__end_line]
            return "".join(lines)

        except Exception as exc:
            return self.__raise_exception(exc)

    # ------- Public Methods ------- #
    def show_errors(self, enable=False):
        """Enable exception raising instead of returning False on error.

        @param {Boolean} [enable=False] - Passing a value of True
                                          enables exception raising.
        """
        self.__enable_exceptions = bool(enable)

    def scan(self, file_name, start_line, end_line=None, encoding=None):
        """Scan lines with the option of using a different file encoding.

        filename (String): The desired file to scan.
        lineno (Integer): The line you wish to scan.
        endline (Optional, Integer, String): The last line to want to scan.
        Specify when scanning multiple lines. Specifying "end" will scan
        the file from lineno to the end of the file.
        encoding (Optional, String): Specify a file encoding to use.
        Defaults to default system encoding.
        @returns {String} The line(s) scanned.
        """
        # Use the system default encoding if one is not specified.
        if encoding is None:
            encoding = locale.getpreferredencoding(False)

        # If no ending line is given, default to a single line
        # TODO Write a test for this condition
        if end_line is None:
            end_line = start_line

        # Set the scan details for use in other methods.
        self.__set_details(file_name, start_line, end_line, encoding)

        # Perform the scan and store it only if it is valid.
        the_scan = self.__scanner()
        return the_scan
