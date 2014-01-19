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
    line = linescan.scan(testFile, 5, "utf_8")
    print(line)
    lines = linescan.scanlines(testFile, 8, 12, "cp1252")
    print(lines)
    thisshouldbefalse = linescan.scan(testFile, 55)
    print(thisshouldbefalse)
