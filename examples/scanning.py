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
from __init__ import (linescan, testFile)


def main():

    LineScan = linescan.LineScan()
    # Scan a single line
    line = LineScan.scan(testFile, 5, encoding="utf_8")
    print("\nExample #1:\n{0}".format(line))

    # Scan multiple lines.
    lines = LineScan.scan(testFile, 8, 12, encoding="cp1252")
    print("\nExample #2:\n{0}".format(lines))

    try:
        raw_input("\nPress Enter to close.")
    except NameError:
        input("\nPress Enter to close.")
    raise SystemExit(0)

if __name__ == "__main__":
    main()
