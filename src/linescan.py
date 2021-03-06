#! /usr/bin/python
# -*- coding: utf-8 -*-
"""Effortlessly read a text file using counting numbers.

Created 2013-2018 Caleb Ely
<https://CodeTri.net>

Licensed under The MIT License
<http://opensource.org/licenses/MIT/>

"""

import locale


__all__ = ("show_errors", "scan")


LINESCAN_OPTIONS = {
    "enable_exceptions": False
}


# ------- Private Methods ------- #
def __raise_exception(exc: Exception) -> False:
    """Handle errors according to exception raising option.

    @private
    @param {Exception} exc - The exception to raise.
    @returns {Boolean} - Returns if `self.__enable_exceptions == True`,
                         return value is `False`.
    """
    # Raise an exception if they are enabled
    if LINESCAN_OPTIONS["enable_exceptions"]:
        raise exc

    # If exceptions have not been enabled, simply return False
    return False


def __scanner(
    file_name: str,
    start_line: int,
    end_line: int,
    _encoding: str
) -> str or False:
    """Perform the actual scan.

    @private
    @param {String} file_name - The file to be scanned.
    @param {Integer} start_line - The line number where to begin scanning.
    @param {Integer|String} end_line - The line number where to end
                                        scanning. Passing the string "end"
                                        will scan from `start_line`
                                        to the end of the file.
    @param {String} [_encoding=None] - Specify a file encoding to use.
                                        Defaults to default system encoding
                                        if set to `None`.
    @returns {String|Boolean} - The lines scanned or `False` if an error
                                was raised and exceptions are not enabled.
    """
    # Since line numbers start at 0, get the starting line number
    # No need to do the same for the ending line, as it is inclusive
    start_line -= 1

    # Use the system default encoding if one is not specified
    if _encoding is None:
        _encoding = locale.getpreferredencoding(do_setlocale=False)

    try:
        with open(file_name, "rt", encoding=_encoding) as f:
            # The user wants to scan until the end of the file
            if end_line == "end":
                lines = f.readlines()[start_line:]

            # The user wants to scan one or more lines
            else:
                lines = f.readlines()[start_line:end_line]
        return "".join(lines)

    except FileNotFoundError as exc:
        return __raise_exception(exc)


# ------- Public Methods ------- #
def show_errors(enable: bool=False):
    """Enable exception raising instead of returning `False` on error.

    @param {Boolean} [enable=False] - Passing a value of `True`
                                      enables exception raising.
    """
    LINESCAN_OPTIONS["enable_exceptions"] = bool(enable)


def scan(
    file_name: str,
    start_line: int,
    end_line: int="end",
    encoding: str=None
) -> str or False:
    """Scan lines with the option of using a different file encoding.

    @param {String} file_name - The file to be scanned.
    @param {Integer} start_line - The line number where to begin scanning.
    @param {Integer|String} [end_line="end"] - The line number where to end
                                        scanning. Passing the string "end"
                                        will scan from `start_line`
                                        to the end of the file.
    @param {String} [encoding=None] - Specify a file encoding to use.
                                        Defaults to default system encoding
                                        if set to `None`.
    @returns {String|Boolean} - The lines scanned or `False` if an error
                                was raised and exceptions are not enabled.
    """
    # Perform the scan
    return __scanner(file_name, start_line, end_line, encoding)
