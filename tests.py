#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
    linescan.py - Effortlessly read lines from a text file using any encoding
    Created 2013-2014 Triangle717
    <http://Triangle717.WordPress.com/>

    Licensed under The MIT License
    <http://opensource.org/licenses/MIT/>
"""

from __future__ import print_function
import os

import linescan

testFile = os.path.join("test", "testfile.txt")

if __name__ == "__main__":
    # Scan a single line
    line = linescan.scan(testFile, 5, encode="utf_8")
    print(line)

    # Scan the same line as above, returns the previous reading
    lineRepeat = linescan.scan(testFile, 5, encode="utf_8")
    print(lineRepeat)

    # Scan multiple lines
    lines = linescan.scan(testFile, 8, 12, encode="cp1252")
    print(lines)

    # Perform an invalid reading
    thisIsFalse = linescan.scan(testFile, 55)
    print(thisIsFalse)
